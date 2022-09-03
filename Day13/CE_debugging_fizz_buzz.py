for number in range(1, 101):
  if number % 3 == 0 or number % 5 == 0: # Or is wrong, because it should only be executed if the number is divisible by both 3 and 5
    print("FizzBuzz")
  if number % 3 == 0: # If needs to be an elif, because it should only print out one statement
    print("Fizz")
  if number % 5 == 0:
    print("Buzz")
  else:
    print([number])

# Solution:
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0: # Replace or with and, because this statement only should be true if the number is divisible by both 3 and 5
    print("FizzBuzz")
  elif number % 3 == 0: # Replaced if with elif
    print("Fizz")
  elif number % 5 == 0: # Replaced if with elif
    print("Buzz")
  else:
    print([number])