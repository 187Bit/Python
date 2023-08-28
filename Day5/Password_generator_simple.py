#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised: 
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# for char in range (1, nr_letters + 1): # For loop in range between 1 and the number of letters the user entered and stored in variable nr_letters + 1
#     password_list += random.choice(letters) # Assign the list password_list a random character from the list letters by using the random.choice funtion
# for char in range (1, nr_numbers + 1): # For loop in range between 1 and the number of letters the user entered and stored in variable nr_numbers + 1
#     password_list += random.choice(numbers) # Assign the list password_list a random character from the list numbers by using the random.choice funtion
# for char in range (1, nr_symbols + 1): # For loop in range between 1 and the number of letters the user entered and stored in variable nr_symbols + 1
#     password_list += random.choice(symbols) # Assign the list password_list a random character from the list symbols by using the random.choice funtion

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = [] # Empty list named password_list

for char in range (1, nr_letters + 1): # For loop in range between 1 and the number of letters the user entered and stored in variable nr_letters + 1
    password_list += random.choice(letters) # Assign the list password_list a random character from the list letters by using the random.choice funtion
for char in range (1, nr_numbers + 1): # For loop in range between 1 and the number of letters the user entered and stored in variable nr_numbers + 1
    password_list += random.choice(numbers) # Assign the list password_list a random character from the list numbers by using the random.choice funtion
for char in range (1, nr_symbols + 1): # For loop in range between 1 and the number of letters the user entered and stored in variable nr_symbols + 1
    password_list += random.choice(symbols) # Assign the list password_list a random character from the list symbols by using the random.choice funtion

# print(password_list)

random.shuffle(password_list)

#password = ''.join(password_list) # Converts the password list into a string

password = "" # Empty string named password

for char in password_list: # For loop 
    password += char #Assign the variable password (string) the value that is stored in char

print(password)