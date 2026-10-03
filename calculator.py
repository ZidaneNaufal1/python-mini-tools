# 🧮 Python Mini Tools - Calculator

def calculator():
    print("=" * 32)
    print("       PYTHON CALCULATOR")
    print("=" * 32)

    try:
        first_number = float(input("First number: "))
        operator = input("Operator (+, -, *, /): ")
        second_number = float(input("Second number: "))

        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "*":
            result = first_number * second_number

        elif operator == "/":
            if second_number == 0:
                print("Error: Cannot divide by zero.")
                return

            result = first_number / second_number

        else:
            print("Error: Invalid operator.")
            return

        print(f"\nResult: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")


if __name__ == "__main__":
    calculator()
