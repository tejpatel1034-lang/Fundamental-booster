# PR. 1 – Fundamental Booster  
## Interactive Personal Data Collector 

###  Project Overview
The Interactive Personal Data Collectors is a beginner-level Python program designed to demonstrate core Python fundamentals.  
The program collects personal information from the user, processes it using basic Python concepts, and displays the results in a structured and readable format.

This project focuses on understanding:
- Input and output operations
- Data types and variables
- Type casting
- Arithmetic operations
- Built-in functions like `type()` and `id()`

---

###  Objective
To create an interactive Python application that:
- Collects user data using `input()`
- Processes data using operators and type conversion
- Displays variable details including value, data type, and memory address
- Demonstrates clean program flow and formatted output

---

###  Concepts Used
- `print()` and `input()`
- Variables and Data Types (`str`, `int`, `float`)
- Type Casting (`int()`, `float()`)
- Arithmetic Operators (`+`, `-`, `*`)
- Built-in Functions: `type()`, `id()`
- Formatted output using f-strings

---

### Information Collected
The program collects the following details from the user:
- Name (String)
- Age (Integer)
- Height in meters (Float)
- Favourite number (Integer)

---

### Data Processing
- The program calculates the **approximate birth year** using the formula:  
  `birth_year = current_year - age`
- Each variable’s:
  - Value
  - Data type
  - Memory address  
  is displayed using `type()` and `id()` functions.

---

### Example Output
    -Welcome to the Interactive Personal Data Collector!

    Please enter your name: Tej
    Please enter your age: 21
    Please enter your height in meters: 1.51
    Please enter your favourite number: 1 

    Thank you! Here is the information we collected:

    Name: Tej (Type: <class 'str'>,
    Memory Address: 2426054860960)
    Age: 21 (Type: <class 'int'>,
    Memory Address: 140713338369784)
    Height: 1.51 (Type: <class 'float'>,
    Memory Address: 2426054597840)
    Favourite Number: 1 (Type: <class 'int'>,
    Memory Address: 140713338369144)

    Your birth year is approximately:
    2005 (based on your age of 21)

    Thank you for using the Personal Data Collector. Goodbye!

### File Structure
         Fundamental-Booster/
                 │
                 ├── main.py
                 ├── README.md

### Author
Name: Patel Tej
