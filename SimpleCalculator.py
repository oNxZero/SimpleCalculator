# Simple Calculator
# Author: oNxZero

# List of allowed arithmetic operations
allowed_operations = ['*', '-', '+', '/']

print("-" * 78)
print("Start Calculator ? ")
print("-" * 78)


while True:
    try:

        want_to_start = input("Enter 'Y'es or 'N'o : ").upper()
        print("-" * 78)

        if want_to_start == 'Y':

            print("Starting Calculator")
            print("-" * 78)
        elif want_to_start == 'N':

            print("Exiting Calculator")
            print("-" * 78)
            exit()
        else:

            print("Invalid Answer")
            print("-" * 78)
            continue


        number_1 = float(input("Number 1 : "))


        operation = None
        while operation not in allowed_operations:
            operation = input("Operation (+, -, *, /): ")
            if operation not in allowed_operations:

                print("-" * 78)
                print("Invalid Operation")
                print("-" * 78)


        while True:
            try:
                number_2 = float(input("Number 2 : "))
                break
            except ValueError:

                print("-" * 78)
                print("Invalid input. Please enter a valid number for Number 2.")
                print("-" * 78)


        if operation == "/" and (number_1 == 0 or number_2 == 0):
            print("-" * 78)
            if number_1 == 0:

                print("Number 1 Is Invalid")
            if number_2 == 0:

                print("Number 2 Is Invalid")
            print("Cannot Divide By Zero")
            print("-" * 78)
            continue


        print("-" * 78)
        print("Your Configuration : ")
        print(f"Operation : {number_1} {operation} {number_2}")
        print("-" * 78)


        while True:
            print("Proceed with Calculation ?")
            print("-" * 78)
            want_to_calculate = input("Enter 'Y'es or 'N'o : ").upper()

            if want_to_calculate == 'Y':

                print("-" * 78)
                print(f"Calculating Results Of : {number_1} {operation} {number_2}")
                result = eval(str(number_1) + operation + str(number_2))
                print(F"Result : {result}")
                print("-" * 78)
                print("Proceed With New Calculation ? ")
                print("-" * 78)
                break

            elif want_to_calculate == 'N':

                print("-" * 78)
                print("-" * 78)
                break

            else:

                print("-" * 78)
                print("Invalid Answer!")
                print("-" * 78)
    except ValueError:

        print("-" * 78)
        print("Invalid input. Please enter a valid number for Number 1.")
        print("-" * 78)
