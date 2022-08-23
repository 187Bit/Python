# To create one lists that still has a separation for two lists you can use nested lists:

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches"]
vegetables = ["Tomatoes", "Potatoes", "Spinach"]

combined_list = [fruits, vegetables] # "inserts" the two lists into the "combined list"

print(combined_list)

print(combined_list[1][1]) # the number in the first [] selects the list and the second number in the [] selects the offset in the chosen list
