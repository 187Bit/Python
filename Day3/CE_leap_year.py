# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? ")) # Asks the user for a year and stores it in the variable year as an integer
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

is_leapyear = False # sets leap year to false

if year % 4 == 0: # Checks if the year is evenly divisible by 4 
    is_leapyear = True
    # print(f"Divisible by 4: {is_leapyear}")

    if year % 100 == 0: # Checks if the year is evenly divisible by 100 
        is_leapyear = False
        # print(f"Divisible by 100: {is_leapyear}")

        if year % 400 == 0: # Checks if the year is evenly divisible by 400 
            is_leapyear = True
            # print(f"Divisible by 400: {is_leapyear}")
        else: # Condition if year is not evenly divisible by 400
            is_leapyear = False
    else: # Condition if year is not evenly divisible by 100
        is_leapyear = True

else: # Condition if year is not evenly divisible by 4
    is_leapyear = False

# Interpreter for the true/false value

if is_leapyear == True: # Checks if the variable is_leapyear is True
    print("Leap year.")
else: # Condition if the variable is_leapyear is not True
    print("Not leap year.")