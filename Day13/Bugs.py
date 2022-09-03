
############DEBUGGING#####################
# To solve bugs you can:

# # Describe Problem
# def my_function():
#   for i in range(1, 20): # i will be a number from 1 to 19
#     if i == 20: # Since i will never be 20 this if-statement will not be triggered
#       print("You got it")
# my_function()
# # Solution:
# def my_function():
#   for i in range(1, 21): # Increased the range by 1; 20 -> 21
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1,6) # The list dice_imgs has 6 position but since the list starts to count from 0 you only have 5 positions. The randint function generates number from 1 to 6. If a 6 gets generated it will produce a index out of range error
# print(dice_imgs[dice_num])
# # Solution:
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 5) # Decrease the range to 5
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994: # If you enter 1994 nothing will happen, because 1994 is greater than 1980 but it is not greater than 1994. So none of the if-statements will be triggered
#   print("You are a Gen Z.")
# Solution:
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?") # age is a string and not an int
# if age > 18: # cannont compare int and string
# print("You can drive at age {age}.") # No indentation and no f-string string
# # Solution:
# age = int(input("How old are you?")) # typecast the value in the variable age into an int
# if age > 18:
#     print(f"You can drive at age {age}.") # Add the f string

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # Double equal sign which means that the value stored in word_per_page is 0
# print(word_per_page) # prints out 0
# total_words = pages * word_per_page # since word_per_page is 0 the whole multiplication is zero because something * 0 is equal to zero
# print(total_words)
# # Solution:
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: ")) # removed one equal sign
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) # Only one items gets appended because it is at the end of the for loop
#   print(b_list)
## Solution:
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item) # indented 
#   print(b_list)

# mutate([1,2,3,5,8,13])