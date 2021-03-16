def add(a, b):
    
    x = a + b
    return x

def subtract(a, b):
    
    x = a - b
    return x

def multiply(a, b):
    
    x = a * b
    return x

def divide(a, b):
    
    x = a / b
    return x

on = ""

cont = "n"

result = None

while on == "":
    
    if cont == "y":
        first_number = result
        print(f"Your first number is: {result}.")
    else:
        first_number = float(input("What's the first number?: "))

    print("+\n-\n*\n/")

    operation = input("Pick an operation: ")

    second_number = float(input("What's the second number?: "))

    if operation == "+":
        result = add(first_number, second_number)
        print(f"{first_number} + {second_number} = {result}")

    elif operation == "-":
        result = subtract(first_number, second_number)
        print(f"{first_number} - {second_number} = {result}")

    elif operation == "*":
        result = multiply(first_number, second_number)
        print(f"{first_number} * {second_number} = {result}")

    elif operation == "/":
        result = divide(first_number, second_number)
        print(f"{first_number} / {second_number} = {result}")

    else:
        print("You did not enter a valid operator.")

    cont = input(f"Type 'y' to continue calculating with {result}, or "
                 "type 'n' to start a new calculation: ")

    on = input("Enter any input to exit the program, otherwise just hit the enter key: ")
