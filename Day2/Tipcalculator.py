#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.") 
bill = float(input("What was the total bill?\n")) #Gets the user's total bill as datatype float and stores it in the variable bill
tip_percentage = int(input("What percentage tip would you like to give?\n")) #Gets the users tip as a datatype integer and stores it in the variable tip_percentage
amount_of_people = int(input("How many people to split the bill?\n")) #Gets the amount of people the bill should be spilt between as a datatype integer and stores it in the variable amount_of_people

result = round((bill * (tip_percentage/100 + 1)) / amount_of_people, 2) #rounds the result into two decimal points, divides the tip percentage by 100 and adds 1, multiplies the tip-value with the bill and divides it by the amount of people and stores it in th variable resutl
#result = "{:.2f}".format(result) #If the result only has one decimal point and you want to add a zero to the value e.g 33.6 -> 33.60
print(f"Each person has to pay: {result} €") #prints out the result by using an F-String 