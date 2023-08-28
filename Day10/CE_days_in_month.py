#Write your code below this line 👇
def leap_year(year):

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
        return True
    else: # Condition if the variable is_leapyear is not True
        return False

def days_in_month(year, month): # Defines a function called days_in_month with the parameters "year" and "month"

    if month > 12 or month < 1:
        return "Invalid input."
    
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # List called "month_days" 
    
    is_leap_year = leap_year(year) # Calls the function leap_year() with the argument year and stores the return value in is_leap_year

    if is_leap_year and month == 2: # Checks if the variable is_leap_year is True and month is equal to 2
        return 29
    else:
        number_of_days = month_days[month-1] # Stores the value in the list month_days at the position month - 1
        return number_of_days # returns the value of the variable number_of_days

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)