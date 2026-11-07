
# Python Lab - 03

**Name:** Aasi Mishra  
**Roll Number:** IC-2K24-03  

---

## Activity: Time and Space Complexity Analysis

**File:** `solution.txt`

**Aim:**  
To analyze different Python programs and determine their time complexity and space complexity using Big-O notation. Understand how the execution time and memory requirements of algorithms change with the input size.

---

## Practical 1: Finding the Largest Element

**Program:** `largest_value()`

**Aim:**  
To find the largest element in a given list of numbers.

**Logic:**
- Initialize the first element as the largest value.
- Traverse the remaining elements using a loop.
- Compare each element with the current largest value.
- Update the largest value whenever a greater element is found.
- Return the largest element.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`

**Explanation:**  
The program visits every element once, resulting in linear time complexity. It uses only a fixed number of variables, so the auxiliary space complexity is constant.

---

## Practical 2: Checking for Duplicate Elements

**Program:** `contains_repeat()`

**Aim:**  
To check whether a list contains any duplicate elements.

**Logic:**
- Find the size of the list.
- Use two nested loops to compare elements.
- Compare each element with all the elements that follow it.
- Return `True` if a duplicate is found.
- Return `False` if no duplicate exists.

**Time Complexity:** `O(n²)`

**Space Complexity:** `O(1)`

**Explanation:**  
The nested loops compare elements in pairs. In the worst case, the number of comparisons grows quadratically with the input size. No additional data structure is used.

---

## Practical 3: Calculating the Sum of Digits

**Program:** `digit_total()`

**Aim:**  
To calculate the sum of all digits of a number using recursion.

**Logic:**
- Check whether the number is zero.
- Extract the last digit using the modulus operator (`%`).
- Remove the last digit using integer division (`//`).
- Recursively calculate the sum of the remaining digits.
- Add the extracted digit to the recursive result.

**Time Complexity:** `O(log n)`

**Space Complexity:** `O(log n)`

**Explanation:**  
Each recursive call removes one digit by dividing the number by 10. Therefore, the number of calls depends on the number of digits. The recursion stack requires logarithmic space.

---

## Practical 4: Generating All Possible Pairs

**Program:** `create_pairs()`

**Aim:**  
To generate all possible ordered pairs from a given list.

**Logic:**
- Find the size of the input list.
- Create an empty list to store pairs.
- Use two nested loops to traverse the elements.
- Append each possible combination of two elements to the result list.
- Return the list containing all pairs.

**Time Complexity:** `O(n²)`

**Space Complexity:** `O(n²)`

**Explanation:**  
Both loops execute n times, generating n × n pairs. Since all pairs are stored in a separate list, the space complexity is also quadratic.

---

## Practical 5: Binary Search

**Program:** `locate_value()`

**Aim:**  
To search for a particular element in a sorted list using the Binary Search algorithm.

**Logic:**
- Initialize the starting and ending positions.
- Calculate the middle position.
- Compare the middle element with the required key.
- If both are equal, return the middle index.
- If the key is greater, search the right half.
- Otherwise, search the left half.
- Repeat until the element is found or the search range becomes empty.

**Time Complexity:** `O(log n)`

**Space Complexity:** `O(1)`

**Explanation:**  
Binary Search eliminates half of the remaining search elements in every iteration. Therefore, the execution time is logarithmic. Only a fixed number of variables are used.

---

## Practical 6: Matrix Multiplication

**Program:** `multiply_matrices()`

**Aim:**  
To multiply two square matrices using nested loops.

**Logic:**
- Determine the dimension of the matrices.
- Create a result matrix initialized with zeros.
- Use three nested loops to access rows, columns, and corresponding elements.
- Multiply the corresponding elements.
- Add the products to the appropriate position in the result matrix.
- Return the resulting matrix.

**Time Complexity:** `O(n³)`

**Space Complexity:** `O(n²)`

**Explanation:**  
Three nested loops execute n times each, resulting in cubic time complexity. The result matrix contains n × n elements, requiring quadratic space.

---

## Practical 7: Converting a Matrix into Sparse Form

**Program:** `extract_nonzero_cells()`

**Aim:**  
To extract all non-zero elements from a matrix and store their row index, column index, and value.

**Logic:**
- Initialize an empty list to store non-zero elements.
- Determine the number of rows and columns.
- Traverse every element of the matrix using nested loops.
- Check whether the current element is non-zero.
- Append its row index, column index, and value to the result list.
- Return the list of non-zero elements.

**Time Complexity:** `O(m × n)`

**Space Complexity:** `O(k)`

**Explanation:**  
Every element in the matrix is examined once. The program stores only non-zero elements, so the additional space depends on k, the number of non-zero elements.

---

## Practical 8: Processing Elements and Their Pairs

**Program:** `display_items_and_pairs()`

**Aim:**  
To display individual elements of a list and generate all possible pairs of its elements.

**Logic:**
- Find the length of the input list.
- Use a loop to print each individual element.
- Use two nested loops to generate every possible pair.
- Print each pair of elements.

**Time Complexity:** `O(n²)`

**Space Complexity:** `O(1)`

**Explanation:**  
The first loop takes O(n) time, while the nested loops take O(n²) time. The quadratic operation dominates the overall time complexity. No additional collection is created.

---

## Practical 9: Checking Against the First Ten Integers

**Program:** `matches_small_number()`

**Aim:**  
To check whether a list contains any element matching an integer between 0 and 9.

**Logic:**
- Traverse each element of the input list.
- For every element, check the integers from 0 to 9.
- Compare the current element with each candidate.
- Return `True` if a match is found.
- Return `False` if no matching element exists.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`

**Explanation:**  
The inner loop always executes ten times, which is constant work. The outer loop processes n elements, resulting in linear time complexity.

---

## Practical 10: Reversing an Array Using a New List

**Program:** `make_reversed_copy()`

**Aim:**  
To reverse the elements of a list by creating a new list.

**Logic:**
- Initialize an empty output list.
- Traverse the original list from the last index to the first.
- Append each element to the new list.
- Return the reversed list.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

**Explanation:**  
Every element is visited once and copied into a new list. Therefore, both execution time and additional memory grow linearly with the input size.

---

## Practical 11: Reversing an Array In-Place

**Program:** `reverse_values()`

**Aim:**  
To reverse a list without creating another list.

**Logic:**
- Initialize two pointers: one at the beginning and one at the end.
- Compare the positions of the two pointers.
- Swap the elements at both positions.
- Move the left pointer forward and the right pointer backward.
- Continue until both pointers meet or cross.
- Return the modified list.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`

**Explanation:**  
The two pointers move towards each other, processing the list in linear time. Since the original list is modified directly, no additional list is required.

---

## Practical 12: Factorial Using Recursion

**Program:** `calculate_factorial()`

**Aim:**  
To calculate the factorial of a number using recursion.

**Logic:**
- Check whether the value is less than or equal to 1.
- Return 1 if the base condition is satisfied.
- Otherwise, call the same function with the value decreased by 1.
- Multiply the current value by the recursive result.
- Return the final factorial.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

**Explanation:**  
The function makes one recursive call for each decreasing value until it reaches the base condition. The recursion stack stores these calls, resulting in linear space complexity.

---

## Practical 13: Fibonacci Series Using Recursion

**Program:** `fibonacci_value()`

**Aim:**  
To calculate a Fibonacci number using recursion.

**Logic:**
- Check whether the given index is less than or equal to 1.
- Return the index if the base condition is satisfied.
- Recursively calculate the Fibonacci value at index - 1.
- Recursively calculate the Fibonacci value at index - 2.
- Add both results and return the final value.

**Time Complexity:** `O(2ⁿ)`

**Space Complexity:** `O(n)`

**Explanation:**  
Each non-base recursive call generates two additional recursive calls, causing exponential growth in execution time. The maximum recursion depth is proportional to n, resulting in linear space complexity.

---

## Practical 14: Counting Pairs Having a Given Sum

**Program:** `count_matching_pairs()`

**Aim:**  
To count the number of pairs whose sum is equal to a given target value.

**Logic:**
- Create an empty set to store previously visited values.
- Initialize a pair counter to zero.
- Traverse each element of the input list.
- Calculate the required complementary value.
- Check whether the complementary value exists in the set.
- Increase the counter if a matching value is found.
- Add the current element to the set.
- Return the total pair count.

**Time Complexity:** `O(n)` on average

**Space Complexity:** `O(n)`

**Explanation:**  
The list is traversed once. Set insertion and lookup operations take constant time on average. In the worst case, the set can store n elements, requiring linear space.

---

## Practical 15: Generating All Possible Subsets

**Program:** `show_subsets()`

**Aim:**  
To generate all possible subsets of a given list using bit manipulation.

**Logic:**
- Calculate the total number of elements.
- Generate all possible bit masks from 0 to 2ⁿ - 1.
- Create an empty list for each subset.
- Check each bit position using bitwise AND.
- Append the corresponding element when the bit is set.
- Print each generated subset.

**Time Complexity:** `O(n × 2ⁿ)`

**Auxiliary Space Complexity:** `O(n)`

**Explanation:**  
A list containing n elements has 2ⁿ possible subsets. Each subset requires checking n bit positions, resulting in O(n × 2ⁿ) time complexity. The temporary subset requires at most O(n) additional space.

---

## Practical 16: Merging Two Sorted Arrays

**Program:** `combine_sorted_lists()`

**Aim:**  
To merge two sorted lists into a single sorted list.

**Logic:**
- Create an empty list to store the merged result.
- Initialize two pointers for the input lists.
- Compare the elements at both pointer positions.
- Append the smaller element to the result list.
- Move the corresponding pointer forward.
- Append any remaining elements from either list.
- Return the merged sorted list.

**Time Complexity:** `O(n + m)`

**Space Complexity:** `O(n + m)`

**Explanation:**  
Each element from both lists is processed once. The resulting list stores all elements from both input lists, requiring O(n + m) additional space.

---

## Practical 17: Checking Whether a String Is a Palindrome

**Program:** `check_palindrome()`

**Aim:**  
To check whether a given string reads the same forward and backward.

**Logic:**
- Accept a string as input to the function.
- Reverse the string using slicing (`[::-1]`).
- Compare the original string with the reversed string.
- Return `True` if both strings are equal.
- Otherwise, return `False`.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

**Explanation:**  
Reversing the string requires processing its characters, taking linear time. A separate reversed string is created, requiring linear additional space.

---

## Practical 18: Converting a Matrix into a Single List

**Program:** `convert_to_list()`

**Aim:**  
To convert a two-dimensional matrix into a single-dimensional list.

**Logic:**
- Initialize an empty list.
- Traverse each row of the matrix.
- Traverse each element within the current row.
- Append every element to the result list.
- Return the flattened list.

**Time Complexity:** `O(m × n)`

**Space Complexity:** `O(m × n)`

**Explanation:**  
The nested loops visit every element in the matrix once. Since all elements are copied into a new list, both time and additional space complexity are O(m × n).

---

## Practical 19: Calculating Power Using Recursion

**Program:** `calculate_power()`

**Aim:**  
To calculate the power of a number using recursion.

**Logic:**
- Check whether the exponent is zero.
- Return 1 if the base condition is satisfied.
- Otherwise, multiply the base value by the result of a recursive call.
- Decrease the exponent by 1 in each recursive call.
- Return the final result.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

**Explanation:**  
The exponent decreases by one in every recursive call until it reaches zero. Therefore, the function makes a linear number of calls and requires linear recursion stack space.

---

## Practical 20: Fast Power Calculation

**Program:** `efficient_power()`

**Aim:**  
To calculate the power of a number efficiently using the exponentiation by squaring technique.

**Logic:**
- Check whether the exponent is zero.
- Return 1 if the base condition is satisfied.
- Recursively calculate the power using half of the exponent.
- If the exponent is even, multiply the partial result by itself.
- If the exponent is odd, multiply the squared result by the base value.
- Return the final result.

**Time Complexity:** `O(log n)`

**Space Complexity:** `O(log n)`

**Explanation:**  
The algorithm divides the exponent by two in every recursive call instead of decreasing it by one. This reduces the number of recursive calls to logarithmic time. The recursion stack also requires logarithmic space.

---

## Practical 21: Checking Common Elements in Two Arrays

**Program:** `share_an_element()`

**Aim:**  
To check whether two lists contain at least one common element.

**Logic:**
- Traverse the first list using a loop.
- For every element in the first list, traverse the second list.
- Compare the current elements of both lists.
- Return `True` if a common element is found.
- Return `False` if no common element exists.

**Time Complexity:** `O(n × m)`

**Space Complexity:** `O(1)`

**Explanation:**  
In the worst case, every element of the first list is compared with every element of the second list. This results in n × m comparisons. Only a fixed number of variables are used.

---

## Practical 22: Creating a Frequency Dictionary

**Program:** `make_frequency_table()`

**Aim:**  
To count the frequency of each element in a list using a dictionary.

**Logic:**
- Create an empty dictionary to store frequencies.
- Traverse each element of the input list.
- Check whether the element already exists in the dictionary.
- If it exists, increase its frequency by one.
- Otherwise, add the element with an initial frequency of one.
- Return the frequency dictionary.

**Time Complexity:** `O(n)` on average

**Space Complexity:** `O(n)`

**Explanation:**  
The program traverses the list once and updates the dictionary for each element. Dictionary operations take constant time on average. If all elements are unique, the dictionary may store n entries, requiring linear space.

---

## Folder Structure

```text
lab3/
│
├── solution.txt
├── placeholder
└── README.md
```

---

## Concepts Covered

- Big-O Notation
- Time Complexity Analysis
- Space Complexity Analysis
- Constant and Linear Complexity
- Quadratic and Cubic Complexity
- Logarithmic Complexity
- Exponential Complexity
- Arrays and Lists
- Nested Loops
- Searching Algorithms
- Binary Search
- Matrix Operations
- Recursion
- String Manipulation
- Set and Dictionary Operations
- Bit Manipulation
- Two-Pointer Technique
- Array Reversal and Merging
- Subset Generation

---

**Language Used:** Python 3

## Conclusion

This lab activity provides an understanding of time and space complexity through 22 different Python programs. It demonstrates how different programming techniques, including loops, recursion, searching, matrix operations, and data structures, affect algorithm efficiency and memory usage.
