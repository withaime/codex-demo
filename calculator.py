def calculate(num1, num2, operator):
    """Perform arithmetic operation based on the operator."""
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return num1 / num2
    raise ValueError("Invalid operator")


def main():
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        result = calculate(num1, num2, operator)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
