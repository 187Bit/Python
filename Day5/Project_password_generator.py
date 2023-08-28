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


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# letters = 1
# numbers = 2
# symbols = 3

# Generate a random sequence with the numbers from 1 to 3 that is the structure of the random order:

length_password = nr_letters + nr_symbols + nr_numbers

random_number_list = []

#! The random_numbers that are generated in the loop to not match up with the numbers that the user enters, which means that the password may have a different amount of letters, numbers or symbols in it.
# Solution: Match up the amount given by the user with the amount that will be generated

#for length in range(1,length_password + 1):
    
  #  random_number = random.randint(1,3)
   # random_number_list.append(random_number)

for letter_counter in range(1, nr_letters + 1):

    random_number_list.append(1)
       
    
for number_counter in range(1, nr_numbers + 1):

    random_number_list.append(2)
        

for symbol_counter in range(1, nr_symbols + 1):

    random_number_list.append(3)

random.shuffle(random_number_list)
     

print(random_number_list)

# print(random_number_list)

random_letters_sequence = []

for loop_length in range(1, nr_letters + 1):

    random_letter_number = random.randint(0,51)
    random_letters_sequence.append(random_letter_number)

random_numbers_sequence = []


for loop_length in range(1, nr_numbers + 1):

    random_numbers_number = random.randint(0, 9)
    random_numbers_sequence.append(random_numbers_number)

random_symbol_sequence = []

for loop_length in range(1, nr_symbols + 1):

    random_symbol_number = random.randint(0, 7)
    random_symbol_sequence.append(random_symbol_number)


length_random_number_sequence = len(random_number_list)
length_letter_list = len(random_letters_sequence)
length_number_list = len(random_numbers_sequence)
length_symbol_list = len(random_symbol_sequence)
counter_random_number_list = 0

# string_random_number_list = ''.join(random_numbers_sequence)
# print(string_random_number_list)


password = []

#print(random_letters_sequence)
#print(f"Random sequence is: {random_numbers_sequence}")

counter_random_number_list = 0
counter_random_letter_list = 0
counter_random_symbol_list = 0
counter_random_number_list = int(counter_random_number_list)

for password_position in range (0, length_password):

    # print(f"Position: {password_position}")

    if random_number_list[password_position] == 1:

        password.append(letters[random_letters_sequence[counter_random_letter_list]])
        counter_random_letter_list += 1
        if counter_random_letter_list == length_letter_list:
            counter_random_letter_list = 0
    if random_number_list[password_position] == 2:

        password.append(numbers[random_numbers_sequence[counter_random_number_list]])
        counter_random_number_list += 1
        if counter_random_number_list == length_number_list:
            counter_random_number_list = 0
    if random_number_list[password_position] == 3:

        password.append(symbols[random_symbol_sequence[counter_random_symbol_list]])
        counter_random_symbol_list += 1
        if counter_random_symbol_list == length_symbol_list:
            counter_random_symbol_list = 0

password_string = ''.join(password)
print(password_string)