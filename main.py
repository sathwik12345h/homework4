from calculator.calculator import Calculator


def main():
    while True:
        try:
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            op = input("Enter operation (add, subtract, multiply, divide): ").strip()

            # Try converting a and b to float early for error checking
            a_float = float(a)
            b_float = float(b)

            if op == 'add':
                result = Calculator.add(a_float, b_float)
            elif op == 'subtract':
                result = Calculator.subtract(a_float, b_float)
            elif op == 'multiply':
                result = Calculator.multiply(a_float, b_float)
            elif op == 'divide':
                result = Calculator.divide(a_float, b_float)
            else:
                print(f"Unknown operation: {op}")
                cont = input("Perform another calculation? (y/n): ").strip().lower()
                if cont != 'y':
                    print("Exiting Calculator. Goodbye!")
                    break
                continue

            print(f"The result of {a_float} {op} {b_float} is equal to {result}")

        except ValueError:
            print(f"Invalid number input: {a} or {b} is not a valid number.")
        except ZeroDivisionError as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

        cont = input("Perform another calculation? (y/n): ").strip().lower()
        if cont != 'y':
            print("Exiting Calculator. Goodbye!")
            break


if __name__ == '__main__':
    main()
