# Calculator

import Calculator_art

# Add

def add(n_1, n_2):
    """Takes to number as input, then adds them together and returns the result."""
    return n_1 + n_2

# Subtract

def subtract(n_1, n_2):
    """Takes to number as input, then subtracts them and returns the result."""
    return n_1 - n_2

# Multiply

def multiply(n_1, n_2):
    """Takes to number as input, then multiplies them and returns the result."""
    return n_1 * n_2

# Divide

def divide(n_1, n_2):
    """Takes to number as input, then divides them and returns the result."""
    return n_1 / n_2

operations = {

    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}

def calculator():

    print(Calculator_art.logo)

    number_1 = float(input("What is the first number?:\n"))

    continue_calculation = "yes"

    while continue_calculation == "yes":

        for operator in operations:
            print(operator)

        operation_type = input("Pick an operation from the lines above:\n")

        number_2 = float(input("What is the next number?:\n"))

        function = operations[operation_type]
        result = function(number_1, number_2)
        print(f"{number_1} {operation_type} {number_2} = {result} ")

        continue_calculation = input(f"Type 'yes' to continue the calculation with {result}?, type 'no' to start a new calculation or type 'stop' to exit.\n")
        number_1 = result
    
    if continue_calculation == "no":
        calculator() # Recursion: calling a function inside it's own definition

calculator()