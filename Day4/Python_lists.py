# A variable can only store one information
# To store multiple data in one "variable" you need lists
# They are like "Arrays"

# Basic structure of lists:

# list_name = [item1, item2, itemn]
# Can have any datatype and datatypes can also be mixed

states_of_usa = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Conneticut", "Massachusetts"]
print(states_of_usa) 

# You can use lists to store many information and also keep order
# The order is determined by the order in the list

# To print out individual information from the list and not the whole list you can use the index [index]

print(states_of_usa[0])

# You can see the index as an offset from the beginning, since 0 is the first item in the list it has 0 offset from the beginning
# You can also use [-index] to start counting from the back of the list, the offset -1 would print the last item in the list

# To change information of an item in the list you can use:
states_of_usa[0] = "Bla, Bla" # If you would print this, you would get "Bla, Bla" instead of "Delaware"

# To add to the list you can use append()

states_of_usa.append("Land_name") # Appends "Land_name" to the already existing list
print(states_of_usa)

# To add more items than one you can use the extend() function

states_of_usa.extend(["Land_name2", "Land_name3"]) # Extends the existing list with another list that is in the ()
print(states_of_usa)

# To create empty lists:
land_list = []