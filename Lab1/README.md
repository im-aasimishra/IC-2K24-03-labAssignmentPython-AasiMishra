
# Python Lab - 01

**Name:** Aasi Mishra  
**Roll Number:** IC-2K24-03  

---

## Section A: Basic Python Concepts

**File:** `sectionA.txt`

**Aim:**  
To understand the fundamental concepts of Python programming and its basic syntax.

**Topics Covered:**
1. Use of the `input()` function and its return type.
2. Checking data types using the `type()` function.
3. Type conversion using `int()` and `float()`.
4. Arithmetic operators such as `**` and `//`.
5. Modulus operator (`%`).
6. Single-line comments using `#`.
7. Rules for naming variables and identifiers.

---

## Section B: Expressions and Output

### Practical 1: Expression Evaluation

**File:** `SectionB.txt`

**Aim:**  
To understand Python expressions, operators, data types, string slicing, and escape sequences by evaluating different statements.

**Logic:**
- Evaluate arithmetic expressions using operators.
- Understand operator precedence.
- Perform modulus and exponentiation operations.
- Evaluate comparison expressions.
- Check data types using `type()`.
- Extract characters using string slicing.
- Understand escape sequences such as `\t` and `\n`.

**Sample Input / Output:**

```text
13
5
True
<class 'float'>
yth
Hi    There
Bye
```

### Practical 2: Python Expression Program

**File:** `SectionB.py`

**Aim:**  
To write a Python program that evaluates different expressions and displays their results.

**Logic:**
- Use arithmetic operators to perform calculations.
- Apply modulus and exponentiation operators.
- Evaluate a Boolean comparison expression.
- Display the data type of a division result.
- Perform string slicing.
- Use tab (`\t`) and newline (`\n`) escape sequences.

**Sample Input / Output:**

```text
13
5
True
<class 'float'>
yth
Hi    There
Bye
```

---

## Section C: Python Practical Programs

### Practical 1: Variables and Identifiers

**File:** `variableIdentifier.py`

**Aim:**  
To write a Python program to demonstrate variables, identifiers, and basic data types.

**Logic:**
- Declare variables to store student details.
- Store name, age, height, and student status.
- Use the `type()` function to identify the data type of each variable.
- Display the values along with their respective data types.

**Sample Input / Output:**

```text
Student Name: Aasi Mishra | Type: <class 'str'>
Age: 24 | Type: <class 'int'>
Height: 165 cm | Type: <class 'int'>
Student Status: True | Type: <class 'bool'>
```

---

### Practical 2: Greeting Program

**File:** `greetingsP.py`

**Aim:**  
To write a Python program that accepts a user's name, age, and city and displays a personalized greeting using an f-string.

**Logic:**
- Accept the user's name as a string.
- Accept age as an integer.
- Accept the city as a string.
- Use an f-string to combine all the entered details into a greeting message.
- Display the final greeting.

**Sample Input / Output:**

```text
Please Enter your name : Aasi
Enter your Age Please : 21
Enter your City Please : Indore
Greetings to Mr.Aasi. You entered your age 21 years old and you belong to Indore.  Greetings! Nice to Meet you.
```

---

### Practical 3: Arithmetic Operations

**File:** `arethematicOp.py`

**Aim:**  
To write a Python program to perform basic arithmetic operations on two numbers.

**Logic:**
- Accept two numbers from the user using the `float()` function.
- Calculate their sum, difference, and product.
- Check whether the second number is zero before performing division.
- If the second number is not zero, calculate quotient and remainder.
- Display the results.

**Sample Input / Output:**

```text
Enter first number: 15
Enter second number: 4

Arithmetic Operations:
Sum = 19.0
Difference = 11.0
Product = 60.0
Quotient = 3.75
Remainder = 3.0
```

---

### Practical 4: Celsius to Fahrenheit Conversion

**File:** `tempConversion.py`

**Aim:**  
To write a Python program to convert temperature from Celsius to Fahrenheit.

**Logic:**
- Accept temperature in Celsius from the user.
- Convert the entered value into a floating-point number.
- Apply the conversion formula:

  `Fahrenheit = (Celsius * 9 / 5) + 32`

- Display both Celsius and Fahrenheit temperatures.

**Sample Input / Output:**

```text
Enter Celsius temperature: 25

Temperature Conversion
Celsius    : 25.0 °C
Fahrenheit : 77.0 °F
```

---

### Practical 5: String Manipulation

**File:** `stringManipulation.py`

**Aim:**  
To write a Python program to perform different string manipulation operations.

**Logic:**
- Accept the full name from the user.
- Convert the string into uppercase using `upper()`.
- Convert the string into lowercase using `lower()`.
- Reverse the string using slicing `[::-1]`.
- Calculate the total number of characters using `len()`.

**Sample Input / Output:**

```text
Please enter your full name: Aasi Mishra

--- String Details ---
Uppercase : AASI MISHRA
Lowercase : aasi mishra
Reverse   : arhsiM isaaA
Length    : 11
```

---

### Practical 6: Escape Sequence Practice

**File:** `escapeSequence`

**Aim:**  
To write a Python program to display a formatted product bill using escape sequences.

**Logic:**
- Store product names in separate variables.
- Use the tab escape sequence (`\t`) to arrange product details into columns.
- Display product names, prices, and quantities in a formatted manner.

**Sample Input / Output:**

```text
Product         Price           Quantity
Notebook        80              2
Pen             20              5
Water Bottle    250             1
```

---

### Practical 7: Menu-Driven Calculator

**File:** `calculator2.py`

**Aim:**  
To write a menu-driven calculator program that performs addition, subtraction, multiplication, and division.

**Logic:**
- Use an infinite `while` loop to display the calculator menu repeatedly.
- Accept the user's choice from the available options.
- If the user selects an arithmetic operation, accept two numbers.
- Use conditional statements to perform the selected operation.
- Handle division by zero to avoid errors.
- Exit the program when the user selects option 5.
- Display an error message for invalid selections.

**Sample Input / Output:**

```text
--- Calculator Menu ---

1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Select an option (1-5): 1
Enter first number: 10
Enter second number: 5
Result: 15.0

--- Calculator Menu ---

1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit

Select an option (1-5): 5
Exiting calculator. Goodbye!
```

---

## Folder Structure

```text
Lab1/
│
├── SectionB.py
├── SectionB.txt
├── arethematicOp.py
├── calculator2.py
├── escapeSequence
├── greetingsP.py
├── sectionA.txt
├── stringManipulation.py
├── tempConversion.py
├── variableIdentifier.py
└── README.md
```

---

## Concepts Covered

- Python Variables and Identifiers
- Basic Data Types
- Input and Output Functions
- Type Conversion
- Arithmetic Operators
- Expressions and Operator Precedence
- Conditional Statements
- Loops (`while` and `for`)
- String Manipulation and Slicing
- Escape Sequences
- Formatted Strings (f-strings)
- Menu-Driven Programming

---

**Language Used:** Python 3

## Conclusion

Lab 1 covers the fundamentals of Python programming through theoretical questions and practical programs. It provides hands-on experience with variables, data types, operators, input/output operations, strings, escape sequences, and basic problem-solving techniques.
