# You can also create functions that have more than one input:

def greet_with(name, location):
    print(f"Hello {name}, I see you are in {location}.")

greet_with("Joel", "Berlin") # Positional argument -> looks at the position and assign them to the parameters in the function in order
# Example:

# def my_function(a,b,c):
    # Do this with a 
    # Do this with b
    # Do this with c 

# my_function(1,2,3) # This will print out the numbers (arguments) in the order they are placed inside the ()

# To avoid this you can user "Keyword Arguments" instead:
# Structure:

# def my_function(a,b,c):
    # Do this with a 
    # Do this with b
    # Do this with c 

# my_function(a = 1,b = 2,c = 3) # The order of the arguments does not matter anymore because the numbers are bound to the argument_name

# Function greet_with with keyword arguments:

greet_with(location = "Berlin", name = "Joel") # Positional argument -> looks at the position and assign them to the parameters in the function in order