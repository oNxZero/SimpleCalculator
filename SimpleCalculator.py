# Simple Calculator
# Author: oNxZero

# List of allowed arithmetic operations
allowed_operations = ['*', '-', '+', '/']

# Display start message
print("-" * 78)
print("Start Calculator ? ")
print("-" * 78)

# Main loop to start or exit the calculator
while True:
    try:
        # Prompt user to start or exit
        want_to_start = input("Enter 'Y'es or 'N'o : ").upper()
        print("-" * 78)

        if want_to_start == 'Y':
            # Start the calculator
            print("Starting Calculator")
            print("-" * 78)
        elif want_to_start == 'N':
            # Exit the calculator
            print("Exiting Calculator")
            print("-" * 78)
            exit()
        else:
            # Handle invalid input
            print("Invalid Answer")
            print("-" * 78)
            continue

        # Input the first number
        number_1 = float(input("Number 1 : "))

        # Input the arithmetic operation
        operation = None
        while operation not in allowed_operations:
            operation = input("Operation (+, -, *, /): ")
            if operation not in allowed_operations:
                # Handle invalid operation
                print("-" * 78)
                print("Invalid Operation")
                print("-" * 78)

        # Input the second number
        while True:
            try:
                number_2 = float(input("Number 2 : "))
                break
            except ValueError:
                # Handle invalid input for number 2
                print("-" * 78)
                print("Invalid input. Please enter a valid number for Number 2.")
                print("-" * 78)

        # Check for division by zero
        if operation == "/" and (number_1 == 0 or number_2 == 0):
            print("-" * 78)
            if number_1 == 0:
                # Handle division by zero for number 1
                print("Number 1 Is Invalid")
            if number_2 == 0:
                # Handle division by zero for number 2
                print("Number 2 Is Invalid")
            print("Cannot Divide By Zero")
            print("-" * 78)
            continue

        # Display the configuration
        print("-" * 78)
        print("Your Configuration : ")
        print(f"Operation : {number_1} {operation} {number_2}")
        print("-" * 78)

        # Proceed with calculation
        while True:
            print("Proceed with Calculation ?")
            print("-" * 78)
            want_to_calculate = input("Enter 'Y'es or 'N'o : ").upper()

            if want_to_calculate == 'Y':
                # Perform the calculation
                print("-" * 78)
                print(f"Calculating Results Of : {number_1} {operation} {number_2}")
                result = eval(str(number_1) + operation + str(number_2))
                print(F"Result : {result}")
                print("-" * 78)
                print("Proceed With New Calculation ? ")
                print("-" * 78)
                break

            elif want_to_calculate == 'N':
                # Exit the calculator
                print("-" * 78)
                print("-" * 78)
                break

            else:
                # Handle invalid input
                print("-" * 78)
                print("Invalid Answer!")
                print("-" * 78)
    except ValueError:
        # Handle invalid input for number 1
        print("-" * 78)
        print("Invalid input. Please enter a valid number for Number 1.")
        print("-" * 78)
