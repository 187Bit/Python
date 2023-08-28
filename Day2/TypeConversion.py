#Type funtion: returns the datatype of the entered variable
#print(type(variable))

#Typecasting: Converts a datatype to another one

# new_variable = str(variable) -> converts the variable inside the () into a string and stores it in the new_variable

name_length = len(input("What is your name?\n"))

converted = str(name_length)

print("Your name has " + converted + " characters.")
#Without the typecast the print() would give you a type error, because the name_length is a integer and the rest in the print() are strings

#Other typecasts:
#integer: int
#float: float
