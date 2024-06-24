def main():
    while True:
        print("\nOptions:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to end the program")
        
        choice = input("Enter operation choice: ").lower()
        
        if choice == "quit":
            print("Goodbye!")
            break
        
        if choice in ("add", "subtract", "multiply", "divide"):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == "add":
                    result = add(num1, num2)
                elif choice == "subtract":
                    result = subtract(num1, num2)
                elif choice == "multiply":
                    result = multiply(num1, num2)
                elif choice == "divide":
                    result = divide(num1, num2)
                
                print(f"Result: {result}")
            
            except ValueError:
                print("Invalid input. Please enter numeric values.")
            
            except Exception as e:
                print(f"Error: {str(e)}")
            
        else:
            print("Invalid input. Please enter a valid operation choice.")

if __name__ == "__main__":
    main()
