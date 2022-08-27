# Group things together and tag related pieces of information
# Left side: Key 
# Right side: Value

# Structure:
# {Key: Value} -> content of dictionary

# Example:
#{"Bug": "An error in a program that prevents the program from running as expected."}
# To add multiple words to one dictionary you can separate them by a comma:
programming_dictionary = {  
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}
# Convention on formatting dictionaries:
# Example:
# name = {
#   "Key_1": "Value_1",
#   "Key2": "Value_2",
#   "Key_3": "Value_3",
# }

# To retrieve an item from a list you use:
# name_of_dictionary["Key"]

print(programming_dictionary["Bug"])

# To add new items to the dictionary you use:
# Structure:
# dictionary_name["new_key_name"] = "Value"

programming_dictionary["Variable"] = "Variable is an abstract storage location paired with an associated symbolic name which contains some known or unknown quantity of information referred to as a value"

print(programming_dictionary)

# To create an empty dictionary you use:
empty_dictionary = {}

# Wipe an entire dictionary:
# programming_dictionary = {} # Wipes the dictionary

print(programming_dictionary) # Prints out an empty dictionary

# Edit an item in a dictionary
programming_dictionary["Bug"] = "Error"
print(programming_dictionary["Bug"])

# Loop trough a dictionary:

for key in programming_dictionary:
    print(key) # Prints the key
    print(programming_dictionary[key]) # Prints the value of the key inside the []