#Write your code below this row 👇


for number in range(1,101): # Loops between 1 and 100
    
    if number % 3 == 0 and number % 5 == 0: # Checks if the number is divisible by 3 and 5 (Modulu = 0)
        print("FizzBuzz")
    elif number % 3 == 0: # Checks if the number is divisible by 3
        print("Fizz")
    elif number % 5 == 0: # Checks if the number is divisible by 5
        print("Buzz")
    else:
        print(number)