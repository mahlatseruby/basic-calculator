def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: Cannot divide by zero!")
        return None
    return x / y

def clear_screen():
    # Clear terminal screen
    print("\n" * 50)

def calculator():
    while True:
        clear_screen()
        print("=== PyCalc - Basic Calculator ===\n")
        
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit\n")

        choice = input("Choose an operation (1-5): ")

        if choice == "5":
            print("\nThank you for using PyCalc! Goodbye.")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == "2":
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == "3":
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif choice == "4":
                result = divide(num1, num2)
                if result is not None:
                    print(f"\n{num1} / {num2} = {result}")
            else:
                print("Invalid choice! Please select 1-5.")

        except ValueError:
            print("Error: Please enter valid numbers only!")
        except Exception:
            print("Something went wrong. Please try again.")

        input("\nPress Enter to continue...")

# Start the calculator
if __name__ == "__main__":
    calculator()