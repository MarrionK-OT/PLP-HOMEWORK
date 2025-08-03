def get_number(prompt):
    """
    Get a valid number from user input.
    
    Args:
        prompt (str): The prompt message to display to the user
        
    Returns:
        float: The number entered by the user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number!")

def get_operation():
    """
    Get a valid operation from user input.
    
    Returns:
        str: The operation symbol (+, -, *, /)
    """
    valid_operations = ['+', '-', '*', '/']
    
    while True:
        operation = input("Enter operation (+, -, *, /): ").strip()
        if operation in valid_operations:
            return operation
        else:
            print("Please enter a valid operation (+, -, *, /)")

def perform_calculation(num1, num2, operation):
    """
    Perform the calculation based on the operation.
    
    Args:
        num1 (float): First number
        num2 (float): Second number  
        operation (str): Operation to perform
        
    Returns:
        tuple: (result, operation_name) or (None, error_message)
    """
    if operation == '+':
        return num1 + num2, "addition"
    elif operation == '-':
        return num1 - num2, "subtraction"
    elif operation == '*':
        return num1 * num2, "multiplication"
    elif operation == '/':
        if num2 == 0:
            return None, "Error: Division by zero is not allowed!"
        return num1 / num2, "division"

def format_result(num1, num2, operation, result):
    """
    Format the result for display.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation symbol
        result (float): Calculation result
        
    Returns:
        str: Formatted result string
    """
    # Format numbers to remove unnecessary decimal places
    if num1.is_integer():
        num1 = int(num1)
    if num2.is_integer():
        num2 = int(num2)
    if isinstance(result, float) and result.is_integer():
        result = int(result)
    
    return f"{num1} {operation} {num2} = {result}"

def main():
    """
    Main function that runs the calculator program.
    """
    print("=" * 40)
    print("     BASIC CALCULATOR PROGRAM")
    print("=" * 40)
    print("This calculator performs basic arithmetic operations.")
    print("Data types used: integers, floats, strings, booleans")
    print("-" * 40)
    
    # Variables demonstration - different data types
    program_name = "Basic Calculator"  # String
    version = 1.0  # Float
    operations_count = 0  # Integer
    is_running = True  # Boolean
    
    print(f"Program: {program_name}")
    print(f"Version: {version}")
    print(f"Type of program_name: {type(program_name).__name__}")
    print(f"Type of version: {type(version).__name__}")
    print("-" * 40)
    
    while is_running:
        try:
            # Get user input
            print("\nEnter your calculation:")
            num1 = get_number("First number: ")
            num2 = get_number("Second number: ")
            operation = get_operation()
            
            # Perform calculation
            result, operation_name = perform_calculation(num1, num2, operation)
            
            # Display result
            if result is not None:
                formatted_result = format_result(num1, num2, operation, result)
                print(f"\nResult: {formatted_result}")
                
                # Additional information about data types
                print(f"\nData type information:")
                print(f"num1 ({num1}): {type(num1).__name__}")
                print(f"num2 ({num2}): {type(num2).__name__}")
                print(f"result ({result}): {type(result).__name__}")
                print(f"operation ('{operation}'): {type(operation).__name__}")
                
                operations_count += 1
                print(f"Operations performed so far: {operations_count}")
            else:
                print(f"\n{operation_name}")
            
            # Ask if user wants to continue
            print("\n" + "-" * 40)
            continue_choice = input("Do you want to perform another calculation? (y/n): ").lower().strip()
            
            if continue_choice not in ['y', 'yes']:
                is_running = False
                print(f"\nThank you for using {program_name}!")
                print(f"Total calculations performed: {operations_count}")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            print("Please try again.")

# Example usage and testing
def run_examples():
    """
    Function to demonstrate the calculator with preset examples.
    """
    print("\n" + "=" * 50)
    print("         EXAMPLE CALCULATIONS")
    print("=" * 50)
    
    examples = [
        (10, 5, '+'),
        (15, 3, '-'),
        (4, 7, '*'),
        (20, 4, '/'),
        (10, 0, '/'),  # Division by zero example
    ]
    
    for num1, num2, op in examples:
        result, operation_name = perform_calculation(num1, num2, op)
        
        if result is not None:
            formatted = format_result(num1, num2, op, result)
            print(f"Example: {formatted}")
        else:
            print(f"Example: {num1} {op} {num2} = {operation_name}")

if __name__ == "__main__":
    # Run examples first to demonstrate functionality
    run_examples()
    
    # Run the main interactive calculator
    main()
