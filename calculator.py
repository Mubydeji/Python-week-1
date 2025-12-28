def safe_number(value):
    """
    Convert a value to float or int.
    """
    try:
        num = float(value)
        return int(num) if num.is_integer() else num
    except ValueError:
        raise ValueError(f"Invalid number: '{value}'")


def calculate(a, operator, b):
    """
    Perform arithmetic operation with error handling.
    """
    a = safe_number(a)
    b = safe_number(b)

    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b
    else:
        raise ValueError(f"Invalid operator: '{operator}'")


def evaluate_expression(expression):
    """
    Evaluate expressions like '12.5 * 3' after validation.
    """
    tokens = expression.strip().split()

    if len(tokens) != 3:
        raise ValueError(
            "Invalid expression format. Use: <number> <operator> <number>"
        )

    a, operator, b = tokens
    return calculate(a, operator, b)


def calculator():
    """
    Main calculator interface.
    """
    print("ROBUST CALCULATOR")
    print("1. Enter operands and operator separately")
    print("2. Enter full expression (e.g., 12.5 * 3)")

    choice = input("Choose mode (1 or 2): ").strip()

    try:
        if choice == "1":
            a = input("Enter first number: ")
            operator = input("Enter operator (+, -, *, /): ")
            b = input("Enter second number: ")
            result = calculate(a, operator, b)

        elif choice == "2":
            expr = input("Enter expression: ")
            result = evaluate_expression(expr)

        else:
            print("Invalid mode selected.")
            return

        print("Result:", result)

    except ZeroDivisionError as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)


# Run calculator
calculator()
