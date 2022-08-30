# Function with outputs return a value 
# Structure:
# def my_function():
    # result = 3 * 2
    # return result # returns the variable result 
# To "capture" the output you have to save it to a variable
# function_output = my_function()


def format_name(first_name, last_name):
    formatted_name = first_name.title() + " " + last_name.title() # Concatenates the two variables and stores it in the variable formatted_name, also make it title case

    return formatted_name # returns the variable formatted_name

print(format_name("joel", "bauer"))