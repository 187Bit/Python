# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Hello")
#     print("Good day!")
#     print("Bye")


# greet()

# Functions with inputs have something inside the (): # The passed input can be used inside the function
# Structure:
# def my_function(something):
    # Do something with something

# my_function(123) # When calling the function you need to add the input into the ()

def greet_with_name(name): # Defines a function with an parameter(input/variable) called name
    print(f"Hello {name}")
    print(f"How are you today {name}?")
    print(f"Bye, {name}")

greet_with_name("Joel") # Calling the function while using an argument -> data in the ()