def calculator():
    print("Pick from : (a)add, (s)subtract, (m)multiply, (d)divide")
    print("Type 'exit' to quit.")
    
    while True:
        operation = input("\nEnter operation (a, s, m, d): ").lower()
        
        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        
        if operation not in ['a', 's', 'm', 'd']:
            print("Invalid operation. Please try again.")
            continue
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            if operation == 'a':
                result = num1 + num2
                print(f"The result is: {result}")
            elif operation == 's':
                result = num1 - num2
                print(f"The result is: {result}")
            elif operation == 'm':
                result = num1 * num2
                print(f"The result is: {result}")
            elif operation == 'd':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result is: {result}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
calculator()
