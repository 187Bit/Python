# Nested if statements structure:
# If condition:
    # if another condition:
        # do this
    # else:
        # do this
# else:
    # do this

# Rollercoaster example v2


print("Welcome to the rollercoaster!") #print a welcome message
height = int(input("What is your height in cm?\n")) #Asks the user for the height and saves it in the variable height as a datatype int
age = int(input("What is your age?\n")) #Asks the user for the height and saves it in the variable height as a datatype int

# Nested if statement

# if height >= 120: # Checks if the height is greater or equal to 120
#     if age <= 18: # Checks if the age is lesser or equal to 18
#         print("Please buy the 7€ ticket.")
#     else: # Else condition if age is greater than 18
#         print("Please buy the 15€ ticket.")
# else: # Else condition if height is lesser than 120
#     print("You are not allowed to ride the rollercoaster.")

# elif statments

# Structure: 
# if condition1:
#     do A
# elif condition2: 
#     do B
# else:
#     do C

if height >= 120: # Checks if the height is greater or equal to 120
    if age < 12: # Checks if the age is lesser than 12
        print("Please buy the 5€ ticket.") 
    elif age <= 18: # Condition else if: checks if age is lesser or equal to 18 (but over 12)
        print("Please buy the 7€ ticket.")
    else: # Else conditon if age is greater than 18
        print("Please buy the 15€ ticket.")
else: # Else condition of height is lesser than 120
    print("You are not allowed to ride the rollercoaster.")