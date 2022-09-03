# number = int(input("Which number do you want to check?"))

# if number % 2 = 0: # Another equal sign is missing
#   print("This is an even number.")
# else:
#   print("This is an odd number.")

## Solution:
number = int(input("Which number do you want to check?"))

if number % 2 == 0: # Added an equal sign because it is an if statements (comparison)
  print("This is an even number.")
else:
  print("This is an odd number.")