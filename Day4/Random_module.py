# Computers are deterministic and predictable
# Pseudorandom number generators are responsible for random actions in computers
# Pyhton uses the "Mersenne Twister"-generator

import random # imports the random module in the file
# import my_module # imports the module "my_module"

# modules: if you write long code it is better to split them up into separate modules (every module is responsible for a different functionality in your code)
# You can think about it like a car-factory: a car is build by multiple people, not one person alone, the car parts are "modules" in that sense 

random_number_int = random.randint(1,10) # calls the random module and uses the randint-function (random integer) to create a random number between the range(a,b) and stores it in the variable random_number_int
print(random_number_int)

# the main.py file is the file that gets executed when you run your code
# you can import new python files (modules) into your main code 

# print(my_module.pi) # prints out the information that is stored in the module "my_module.py"

# create random floating point number:

random_number_float = random.random() # generates a random floating point number in the range between 0 and 1 (excluding 0 and 1) and stores it in the variable random_float number
print(random_number_float)

print(random_number_float * 5) # generates a random floating point number in the range of 0 and 5

# To create a number between other ranges: Multiply the result of the random.random() funtion or use the random.uniform(a,b) function

random_number_float = random.uniform(0,5) # generates a random floating point number in the range of 0 and 5
print(random_number_float)