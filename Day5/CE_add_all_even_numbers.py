#Write your code below this row 👇

total = 0

for number in range(2,101,2): # Loops in between 2 and 100 and uses a step size of 2
    total += number # Add number to the total value
    # print(f"Current number is {number}")

print(total)

# Alternative

total2 = 0

for number in range (1, 101):
    if number % 2 == 0:
        total2 += number

print(total2)