
# Python Lab - 02

**Name:** Aasi Mishra  
**Roll Number:** IC-2K24-03  

---

## Practical 1: Inverse Triangle Pattern

**File:** `inverse_triangle.py`

**Aim:**  
To write a Python program to print an inverted right-angle triangle pattern using asterisks (`*`).

**Logic:**
- Accept the number of rows from the user.
- Use a `for` loop that starts from the entered number and decreases up to 1.
- Print the required number of asterisks in each row using string multiplication.

**Sample Input / Output:**

```text
Enter how many rows you want: 5
* * * * *
* * * *
* * *
* *
*
```

---

## Practical 2: Rhombus Pattern

**File:** `rhombus.py`

**Aim:**  
To write a Python program to print a rhombus pattern using asterisks (`*`).

**Logic:**
- Accept the number of rows from the user.
- Use a `for` loop to iterate through each row.
- Print spaces before the asterisks to create the required alignment.
- Print the same number of asterisks in every row.

**Sample Input / Output:**

```text
Enter how many rows you want: 5
    * * * * *
   * * * * *
  * * * * *
 * * * * *
* * * * *
```

---

## Practical 3: Right Triangle Pattern

**File:** `right_triangle.py`

**Aim:**  
To write a Python program to print a right-angle triangle pattern using asterisks (`*`).

**Logic:**
- Accept the number of rows from the user.
- Use a `for` loop starting from 1 and continuing up to the entered number.
- Print asterisks equal to the current row number.
- Increase the number of asterisks in each successive row.

**Sample Input / Output:**

```text
Enter how many rows you want: 5
*
* *
* * *
* * * *
* * * * *
```

---

## Practical 4: Square Pattern

**File:** `square.py`

**Aim:**  
To write a Python program to print a square pattern using nested `for` loops.

**Logic:**
- Accept the number of rows from the user.
- Use an outer `for` loop to control the rows.
- Use an inner `for` loop to print asterisks in each row.
- Use `end=""` to print asterisks on the same line.
- Use `print()` after the inner loop to move to the next line.

**Sample Input / Output:**

```text
Enter how many rows you want: 5
 *  *  *  *  *
 *  *  *  *  *
 *  *  *  *  *
 *  *  *  *  *
 *  *  *  *  *
```

---

## Practical 5: Triangle Pattern

**File:** `triangle.py`

**Aim:**  
To write a Python program to print a centered triangle (pyramid) pattern using asterisks (`*`).

**Logic:**
- Accept the number of rows from the user.
- Use a `for` loop to iterate from 1 to the entered number.
- Print spaces before the asterisks to center the pattern.
- Calculate the number of asterisks using the formula `2 * i - 1`.
- Increase the number of asterisks in each row to form a pyramid.

**Sample Input / Output:**

```text
Enter number of rows: 5
    *
   ***
  *****
 *******
*********
```

---

## Folder Structure

```text
Lab2/
│
├── inverse_triangle.py
├── rhombus.py
├── right_triangle.py
├── square.py
├── triangle.py
└── placeholder
```

---

**Language Used:** Python 3

**Concepts Covered:**
- Input and Output
- Variables
- For Loops
- Nested For Loops
- String Multiplication
- Pattern Printing
- Basic Logic Building

---
