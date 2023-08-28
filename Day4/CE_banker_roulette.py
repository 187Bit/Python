import random

# 🚨 Don't change the code below 👇
# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)
random.seed()

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ") # Asks the user for names and stores it in the variable names_string
names = names_string.split(", ") # Divides the name into separate strings and create a list with the name "names"
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

number_of_people = len(names) # Gets the lenght of the string "names" and stores it in the variable number_of_people

random_number = random.randint(0,number_of_people - 1) # Generates a random number between 0 and the value stored in the variable "number_of_people" and stores it in the variable random_number

print(f"{names[random_number]} is going to buy the meal today!")

# For a faster solution you could also use the choice() function

person_who_will_pay = random.choice(names)
print(person_who_will_pay)