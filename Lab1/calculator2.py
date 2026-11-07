while True:
    print("\n--- Calculator Menu ---\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    option = input("Select an option (1-5): ")

    if option == "5":
        print("Exiting calculator. Goodbye!")
        break

    elif option in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if option == "1":
            answer = num1 + num2
        elif option == "2":
            answer = num1 - num2
        elif option == "3":
            answer = num1 * num2
        else:
            answer = num1 / num2 if num2 != 0 else None

        if option == "4" and num2 == 0:
            print("Error: Division by zero.")
        else:
            print(f"Result: {answer}")

    else:
        print("Invalid selection. Try again.")
