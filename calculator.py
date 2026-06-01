print("===== SIMPLE CALCULATOR =====")

while True:

    num1 = float(input("\nEnter first number: "))
    operator = input("Enter operator (+, -, *, /, %, **, //): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result =", num1 + num2)

    elif operator == "-":
        print("Result =", num1 - num2)

    elif operator == "*":
        print("Result =", num1 * num2)

    elif operator == "/":
        if num2 != 0:
            print("Result =", num1 / num2)
        else:
            print("Error: Cannot divide by zero!")

    elif operator == "%":
        if num2 != 0:
            print("Result =", num1 % num2)
        else:
            print("Error: Cannot divide by zero!")

    elif operator == "**":
        print("Result =", num1 ** num2)

    elif operator == "//":
        if num2 != 0:
            print("Result =", num1 // num2)
        else:
            print("Error: Cannot divide by zero!")

    else:
        print("Invalid operator!")

    choice = input("\nDo you want to perform another calculation? (yes/no): ")

    if choice.lower() == "no":
        print("\nThank you for using the calculator! 👋")
        break