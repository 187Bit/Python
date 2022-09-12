# A package is a whole bunch of code that someone has written to achieve some goal or purpose
# A module is a file

# On Pypi you can install packages

# import prettytable
from prettytable import PrettyTable

my_table = PrettyTable()
# Method:

my_table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"]) # Field name: Pokemon, Data: "Pikachu" etc.
my_table.add_column("Type", ["Electric", "Water", "Fire"])
my_table.align = "l" # Because it is a variable you have to use an equal sign
print(my_table)

# Difference between attribute and method:
# An attribute is basically a variable that you can modify. To modify it you need to use an equal sign. If you want to change the allignment of the table you have to specify it with my_table.align
# The .align tells the computer to change the allignment of the table
# Finally you have to modify the value by typing my_table.align = "value"

# A method has () after the methodname
# my_table.add_colum(argument_1, argument_2)