#If you convert a float into an integer it will cut off the numbers after the decimal point
#To round a float, use the round() funtion

print(round(8/3))
#To round the number to decimal places (Nachkommastellen), you can place a comma after the calculation following by the number of places you want
print(round(8/3, 2))

#Flaw_division: cuts of the number after the decimal point, like the type cast from float to integer
#The // symbolises a flaw division
print(8 // 3)

#You can also use variables to continue your calculation

result = 4 / 2
result /= 2
print(result)

#F Strings: Add an f in front of your string and in front of the "
#To add other data types to the string, place {} into the string and inside these you can place your variable

score = 0
height = 1.8
isWinning = True

print(f"Your score is {score} and your height is {height}. You are winning is {isWinning}")