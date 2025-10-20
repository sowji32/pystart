print("Welcome to the Simple Calculator!")

while True:
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Thanks for using the calculator. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
