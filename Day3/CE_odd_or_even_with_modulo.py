# The modulo gives you the remainder of a division
# It uses the % symbol
# Example: 6 % 2 -> 0 (no remainder)
# 6 % 4 -> 1 (remainder)

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? ")) #Asks the user for a number and stores it in the variable number as an integer
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

is_even = number % 2 # Calculates the modulo of the number divided by 2 and stores it in the variable is_even

if is_even == 0: # Checks if the value stored in is_even is equal to 0
    print("This is an even number.") # Prints out a message if the value is equal to 0
else: # If the value is not 0
    print("This is an odd number.") # Prints out a message if the value is equal to 1 