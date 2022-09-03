# Calculator

import Calculator_art # imports the module: Calculator_art

# Add

def add(n_1, n_2): # Defines a function called add() with the two parameter n_1 and n_2
    """Takes to number as input, then adds them together and returns the result."""
    return n_1 + n_2

# Subtract

def subtract(n_1, n_2): # Defines a function called subtract with the two parameter n_1 and n_2
    """Takes to number as input, then subtracts them and returns the result."""
    return n_1 - n_2

# Multiply

def multiply(n_1, n_2): # Defines a function called multiply with the two parameter n_1 and n_2
    """Takes to number as input, then multiplies them and returns the result."""
    return n_1 * n_2

# Divide

def divide(n_1, n_2): # Defines a function called divide with the two parameter n_1 and n_2
    """Takes to number as input, then divides them and returns the result."""
    return n_1 / n_2

operations = { # Dictionary called operations that stores the key (which are the operatios) and the value which is the name of each function

    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}

def calculator(): # Defines a function called calculator()

    print(Calculator_art.logo) # prints out the calculator logo

    number_1 = float(input("What is the first number?:\n")) # Asks the user for an input and stores in the variable number_1 as a float 

    continue_calculation = "yes"

    while continue_calculation == "yes": # While loop until continue_calculation is not "yes"

        for operator in operations: # for loop for the dictionary operations
            print(operator)

        operation_type = input("Pick an operation from the lines above:\n") # Asks the user to pick an operation and stores the string inside the variable operation_type

        number_2 = float(input("What is the next number?:\n")) # Asks the user for the second number and stores it in the variable number_2 as a float

        function = operations[operation_type] # takes the string stored in the variable operation_type and uses this a the key for the dicitionary operations and assigns this value to the variable function
        result = function(number_1, number_2) # executes the function (because gets replaced with the function name), has the positional arguments number_1 and number_2, stores the output in te variable result

        print(f"{number_1} {operation_type} {number_2} = {result} ")

        continue_calculation = input(f"Type 'yes' to continue the calculation with {result}?, type 'no' to start a new calculation or type 'stop' to exit.\n") # Asks the user if he/she/it wants to continue the calculation with the current value, start a new calculation or exit the program
        number_1 = result
    
    if continue_calculation == "no": # Checks if continue_calculation is "no"
        calculator() # Recursion: calling a function inside it's own definition

calculator() # Calls the calculator() function