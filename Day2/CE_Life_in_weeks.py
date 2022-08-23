# 🚨 Don't change the code below 👇
age = int(input("What is your current age?"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Time age years old

days = age * 365
weeks = age * 52
months = age * 12

#Time 90 years old

days_90 = 90 * 365
weeks_90 = 90 * 52
months_90 = 90 * 12

#Calculations

days = days_90 - days
weeks = weeks_90 - weeks
months = months_90 - months

print(f"You have {days} days, {weeks} weeks, and {months} months left.")