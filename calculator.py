import math


def calculator(expression):
    try:
        # Replace ^ with ** for powers
        expression = expression.replace("^", "**")

        # Factorial: 10! → factorial(10)
        while "!" in expression:
            position = expression.index("!")

            # Find the number before !
            start = position - 1

            while start >= 0 and (expression[start].isdigit() or expression[start] == "."):
                start -= 1

            number = expression[start + 1:position]

            if not number:
                return "Invalid factorial"

            expression = (
                expression[:start + 1]
                + f"math.factorial({number})"
                + expression[position + 1:]
            )

        # Scientific functions
        expression = expression.replace("sqrt", "math.sqrt")
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("log", "math.log10")
        expression = expression.replace("ln", "math.log")

        # Constants
        expression = expression.replace("pi", "math.pi")
        expression = expression.replace("e", "math.e")

        # Calculate
        answer = eval(expression, {"__builtins__": {}}, {"math": math})

        return answer

    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

    except ValueError:
        return "Error: Invalid mathematical value"

    except Exception:
        return "Error: Invalid expression"


print("=" * 45)
print("          SCIENTIFIC CALCULATOR")
print("=" * 45)
print("Type 'exit' to close the calculator.")
print()
print("Examples:")
print("  1 + 2")
print("  10 * 5")
print("  2^5")
print("  10!")
print("  sqrt(25)")
print("  sin(30)")
print("  cos(60)")
print("  log(100)")
print("  pi * 5^2")
print("=" * 45)


while True:

    expression = input("\nEnter calculation: ")

    if expression.lower() == "exit":
        print("Calculator closed.")
        break

    result = calculator(expression)

    print("Answer =", result)