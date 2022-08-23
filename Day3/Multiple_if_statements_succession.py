# If one condition in a normal if statement is True, it automatically bypasses the other if statements

# in this example only one of those statements will be executed:

# if condiotion1: 
#     do A
# elif condition2:
#     do B
# else conditon3:
#     do C

# in this example all three conditions will be checked:

# if condition1: 
#     do A 
# if condition2: 
#     do B 
# if condition3:

print("Welcome to the rollercoaster!") #print a welcome message
height = int(input("What is your height in cm?\n")) #Asks the user for the height and saves it in the variable height as a datatype int
age = int(input("What is your age?\n")) #Asks the user for the height and saves it in the variable height as a datatype int
bill = 0 

if height >= 120: # Checks if the height is greater or equal to 120

    if age < 12: # Checks if the age is lesser than 12
        print("Child tickets are 5€ per ticket.") 
        bill = 5
    elif age <= 18: # Condition else if: checks if age is lesser or equal to 18 (but over 12)
        print("Youth tickets are 7€ per ticket.")
        bill = 7
    else: # Else conditon if age is greater than 18
        print("Adult tickets are 15€ per ticket.")
        bill = 15

    wants_photo = input("Do you want to have a photo taken for 3€? Y or N.\n")
    if wants_photo == "Y":
        #Add 3€ to the bill
        bill += 3
    print(f"You have to pay {bill} €.")

else: # Else condition of height is lesser than 120
    print("You are not allowed to ride the rollercoaster.")