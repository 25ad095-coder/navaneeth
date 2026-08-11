# Simple Calculator

print("===== CALCULATOR =====")

# Get two numbers
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        print("Invalid choice. Please select 1-4.")

except ValueError:
    print("Error: Please enter valid numbers.")
