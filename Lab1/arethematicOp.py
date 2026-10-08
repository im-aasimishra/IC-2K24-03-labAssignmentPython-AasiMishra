# Section C: Programs to Write
# 3. Arithmetic Operations

# Taking two numbers as input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nArithmetic Operations:")
print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Product =", num1 * num2)

# Avoiding division by zero
if num2 == 0:
    print("Quotient and remainder cannot be calculated.")
else:
    print("Quotient =", num1 / num2)
    print("Remainder =", num1 % num2)

# Output:
# Enter first number: 15
# Enter second number: 4
#
# Arithmetic Operations:
# Sum = 19.0
# Difference = 11.0
# Product = 60.0
# Quotient = 3.75
# Remainder = 3.0
