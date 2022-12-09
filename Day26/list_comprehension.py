# unique to python 
# creating a list from another list
# so far we have been using for loops for that

# Basic syntax:

# new_list = [new_item for item in list]

# Example:

numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

name = "Angela"

new_list = [letter for letter in name]
print(new_list)

new_list = [r*2 for r in range(1,5)]
print(new_list)

# Conditional list comprehension:

# Basic syntax:

# new_list = [new_item for item in list if test]
# only add the item to the new_lis if the test passes, so if it is True

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# Only contain names that are shorter than 5 characters
short_names = [name for name in names if len(name) < 5]
print(short_names)

names_in_upper_case = [name.upper() for name in names if len(name) > 5]
print(names_in_upper_case)