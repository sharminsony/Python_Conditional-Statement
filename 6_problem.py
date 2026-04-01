##Simple Calculator: Input two numbers and an operator (+, -, *, /).Use if-elif to perform the operation and print the result. Handle division by zero using conditions.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

if operator == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"The result is: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result is: {result}")
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator.")