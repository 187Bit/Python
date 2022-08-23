#Check for multiple conditions at once in one if statement

# Logical operators

# And: Both have to be true
# Or: One has to be true
# Not: None have to be true

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
    elif age >= 45 and age <= 55:
        print("Your ticket price is free.") # Midlife crisis ticket
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