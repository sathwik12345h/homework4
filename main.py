from calculator.calculator import Calculator

def main():
    while True:
        print("\nAvailable commands: add, subtract, multiply, divide, menu, exit")
        command = input("Enter operation: ").strip().lower()

        if command == "exit":
            print("Exiting Calculator. Goodbye!")
            break
        elif command == "menu":
            print("Commands available:", ", ".join(Calculator.commands.keys()))
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            result = Calculator.execute(command, a, b)
            print(f"The result of {a} {command} {b} is {result}")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except ZeroDivisionError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
