def basic_calculator():
    print("\n=== BASIC CALCULATOR ===")
    print("Available operations: + (addition), - (subtraction), * (multiplication), / (division)")
    print("Type 'quit' to exit the program\n")
    
    while True:
        try:
            # Get first number
            num1_input = input("Enter first number (or 'quit' to exit): ")
            if num1_input.lower() == 'quit':
                print("Exiting calculator. Goodbye!")
                break
            
            num1 = float(num1_input)
            
            # Get operation
            operation = input("Enter operation (+, -, *, /): ").strip()
            if operation not in ['+', '-', '*', '/']:
                print("Invalid operation! Please use one of: +, -, *, /")
                continue
                
            # Get second number
            num2 = float(input("Enter second number: "))
            
            # Perform calculation
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                result = num1 / num2
            
            # Display result with 2 decimal places for cleaner output
            print(f"\nResult: {num1} {operation} {num2} = {result:.2f}\n")
            
            # Ask if user wants to continue
            continue_calc = input("Perform another calculation? (yes/no): ").lower()
            if continue_calc != 'yes':
                print("Exiting calculator. Goodbye!")
                break
                
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user. Exiting...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Run the calculator
if __name__ == "__main__":
    basic_calculator()