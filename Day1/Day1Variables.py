#Variables are used to store information (variables always start with a small letter)
#Do not call variables as funtions

name = input("What is your name? ")
#to print() out the variable use print(variable name)
print(name)

#to change variables names you can do:

new_name = name
print(new_name)

#simplify the length funtion of the string

name = input("What is your name? ") #the input of the user is stored in the variable "name"
length = len(name) #the length of the user input is stored in length
print("The length of your name is: ") #prints out "The length of your name is: "
print(length) #prints out the value that is stored in the variable length