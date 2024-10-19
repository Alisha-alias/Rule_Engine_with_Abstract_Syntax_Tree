# **Rule Engine with Abstract Syntax Tree**
Developing a simple 3-tier rule engine application (Simple UI, API, and Backend, Data) to determine user eligibility based on attributes like age, department, income, spend, etc. The system can use Abstract Syntax Tree (AST) to represent conditional rules and allow for dynamic creation, combination, and modification of these rules.

## **Rule Engine Application**
This repository contains a Rule Engine application built with Flask. The application evaluates user-defined rules based on provided input data and stores evaluation results in a SQLite database.

## **Table of Contents**
- [Features](#features)
  - [User-Friendly Interface](#user-friendly-interface)
  - [Rule Evaluation](#rule-evaluation)
  - [Data Persistence](#data-persistence)
- [Technologies Used](#technologies-used)
  - [Backend](#backend)
  - [Frontend](#frontend)
  - [Database](#database)
- [Build Instructions](#build-instructions)
  - [1. Cloning the Repository](#1-cloning-the-repository)
  - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
  - [3. Install the Dependencies](#3-install-the-dependencies)
  - [4. Run the Application](#4-run-the-application)
  - [5. Access the Application](#5-access-the-application)
- [Design Choices](#design-choices)
  - [Architecture](#architecture)
  - [Rule Evaluation Logic](#rule-evaluation-logic)
  - [Database Design](#database-design)
  - [User Interface](#user-interface)
- [Usage](#usage)
  - [Input Fields](#input-fields)
  - [Evaluating Rules](#evaluating-rules)
  - [Viewing Results](#viewing-results)


## **Features**

### **User-Friendly Interface**
Intuitive web form for users to input rules and relevant data.
Clear instructions and placeholders guide users in entering correct values.

### **Rule Evaluation**
Supports defining complex rules using logical operators.
Evaluates rules based on the provided data and displays the results dynamically.

### **Data Persistence**
Evaluation results are stored in a SQLite database for future reference.
Easy retrieval of evaluation data for analysis or debugging.


## **Technologies Used**

### **Backend**
**Python:** The primary language used to build the application.
**Flask:** A lightweight web framework for building the web application.

### **Frontend**
**HTML/CSS:** Markup and styling languages used to create the user interface.
**JavaScript:** For handling form submissions and updating results dynamically without reloading the page.

### **Database**
**SQLite:** A lightweight, serverless database used to store evaluation results.

## **Build Instructions**

### **1. Cloning the Repository**
    ```bash
     git clone https://github.com/Alisha-alias/Rule_Engine_with_Abstract_Syntax_Tree
     

### **2. Create a Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate
    
### **3. Install the Dependencies**
    ```bash
    pip install Flask

### **4. Run the Application**
    ```bash
    python app.py
     
### **5. Access the Application**
Open your web browser and go to http://127.0.0.1:5000/.


## **Design Choices**

### **Architecture**

**MVC Pattern:** The application follows a simple Model-View-Controller (MVC) architecture to separate concerns and improve maintainability.

### **Rule Evaluation Logic**
**Abstract Syntax Tree (AST):** The application uses AST for parsing and evaluating rules. This allows for complex expressions and combinations of rules to be handled easily.

### **Database Design**
**SQLite:** A lightweight database was chosen for simplicity. The application creates a table to store evaluations, allowing for easy querying and retrieval of data.

### **User Interface**
**Responsive Design:** The front-end is designed to be responsive, providing a good user experience on various devices. Custom CSS styles improve the aesthetics of the form and result display.


## **Usage**
### **Input Fields**
**Rule 1:** Enter the first rule for evaluation.

**Rule 2:** Enter the second rule for evaluation.

**Age:** Enter the user's age.

**Department:** Enter the user's department.

**Salary:** Enter the user's salary.

**Experience:** Enter the user's years of experience.

### **Evaluating Rules**
Fill out the form with the required information and rules. Click the "Evaluate" button to submit the data.

### **Viewing Results**
After submission, the results will be displayed below the form, showing whether each rule and the combined rule were satisfied.

 


