# Generate a range that the numbers or etc. loops through
# Structure:
# for number in range(a,b):
    # Do something cool

for number in range(1,10): # Does not include 10
    print(number)

# By default the loop increases it's current step by one. To increase it more than one you can add another number separated by a comma after the range:

for number in range(1,10, 2):
    print(f"Your number is:{number}")

total = 0

for number in range (1,101):
    total += number

print(total)