import json
import re
import sqlite3
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.type = node_type  # "operator" or "operand"
        self.left = left       # Left child
        self.right = right     # Right child
        self.value = value     # Value for operand nodes

class RuleEngine:
    def __init__(self):
        self.rules = []
        self.create_database()

    def create_database(self):
        conn = sqlite3.connect('rule_engine.db')
        cursor = conn.cursor()

        # Create a table for storing rules and evaluations
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS evaluations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            age INTEGER,
            department TEXT,
            salary REAL,
            experience INTEGER,
            rule1_satisfied TEXT,
            rule2_satisfied TEXT,
            combined_rule_satisfied TEXT
        )
        ''')

        conn.commit()
        conn.close()

    def create_rule(self, rule_string):
        tokens = self.tokenize(rule_string)
        ast = self.build_ast(tokens)
        return ast

    def tokenize(self, rule_string):
        # Basic tokenization
        return re.findall(r'\w+|[<>=!]+|\(|\)', rule_string)

    def build_ast(self, tokens):
        # Build AST using a simple parser
        def parse_expression(tokens):
            token = tokens.pop(0)
            if token == '(':
                left = parse_expression(tokens)
                operator = tokens.pop(0)
                right = parse_expression(tokens)
                tokens.pop(0)  # pop ')'
                return Node('operator', left, right, operator)
            else:
                # Must be an operand (condition)
                op = token
                operator = tokens.pop(0)  # e.g., >, <, =, etc.
                value = tokens.pop(0)      # the value to compare against
                if operator == '=':
                    operator = '=='
                return Node('operand', value=op + " " + operator + " " + value)

        return parse_expression(tokens)

    def combine_rules(self, rules, combine_type='OR'):
        combined_ast = None
        for rule in rules:
            ast = self.create_rule(rule)
            if combined_ast is None:
                combined_ast = ast
            else:
                combined_ast = Node('operator', combined_ast, ast, combine_type)  # Use combine_type for flexibility
        return combined_ast

    def evaluate_rule(self, ast, data):
        if ast.type == 'operand':
            condition = ast.value.split(" ")
            attribute = condition[0]
            operator = condition[1]
            value = condition[2].strip("'")  # Remove quotes for string comparisons

            user_value = data.get(attribute)

            if user_value is None:
                return False

            # Debugging output
            print(f"Evaluating: {attribute} {operator} {value} (User value: {user_value})")

            # Handle numeric comparisons
            try:
                user_value = float(user_value)
                value = float(value) if value.replace('.', '', 1).isdigit() else value  # Convert if possible
            except ValueError:
                pass

            # Perform comparison
            if operator == '>':
                return user_value > value
            elif operator == '<':
                return user_value < value
            elif operator == '>=':
                return user_value >= value
            elif operator == '<=':
                return user_value <= value
            elif operator == '==':
                return str(user_value) == str(value)
            elif operator == '!=':
                return str(user_value) != str(value)

        elif ast.type == 'operator':
            left_eval = self.evaluate_rule(ast.left, data)
            right_eval = self.evaluate_rule(ast.right, data)
            print(f"Evaluating: {left_eval} {ast.value} {right_eval}\n")
            if ast.value == 'AND':
                return left_eval and right_eval
            elif ast.value == 'OR':
                return left_eval or right_eval
        return False

    def store_evaluation(self, data, rule1_satisfied, rule2_satisfied, combined_rule_satisfied):
        conn = sqlite3.connect('rule_engine.db')
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO evaluations (age, department, salary, experience, rule1_satisfied, rule2_satisfied, combined_rule_satisfied)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (data['age'], data['department'], data['salary'], data['experience'], rule1_satisfied, rule2_satisfied, combined_rule_satisfied))

        conn.commit()
        conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate():
    rule_engine = RuleEngine()

    rule1 = request.form.get('rule1')
    rule2 = request.form.get('rule2')
    user_data = {
        'age': int(request.form.get('age')),
        'department': request.form.get('department'),
        'salary': float(request.form.get('salary')),
        'experience': int(request.form.get('experience'))
    }

    # Create AST for rules
    ast_rule1 = rule_engine.create_rule(rule1)
    ast_rule2 = rule_engine.create_rule(rule2)

    # Combine rules
    combined_rule = rule_engine.combine_rules([rule1, rule2], combine_type='OR')

    rule1_satisfied = rule_engine.evaluate_rule(ast_rule1, user_data)
    rule2_satisfied = rule_engine.evaluate_rule(ast_rule2, user_data)
    combined_rule_satisfied = rule_engine.evaluate_rule(combined_rule, user_data)

    # Store evaluation results in the database
    rule_engine.store_evaluation(user_data, "Yes" if rule1_satisfied else "No",
                                 "Yes" if rule2_satisfied else "No",
                                 "Yes" if combined_rule_satisfied else "No")

    return jsonify({
        'rule1_satisfied': "Yes" if rule1_satisfied else "No",
        'rule2_satisfied': "Yes" if rule2_satisfied else "No",
        'combined_rule_satisfied': "Yes" if combined_rule_satisfied else "No"
    })

if __name__ == "__main__":
    app.run(debug=True)
