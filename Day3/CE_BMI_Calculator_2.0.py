# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: ")) # Gets the users height input as a float and stores in in the variable height
weight = float(input("enter your weight in kg: ")) # Gets the useer weight input as a float and stores it in the variable weight
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI_result = round(weight / height ** 2) # Calculates the BMI and stores it in the variable BMI_result

if BMI_result < 18.5: # Checks if the value in BMI_result is smaller or equal to 18.5
    print(f"Your BMI is {BMI_result}, you are underweight.")
elif BMI_result < 25: # Checks if the value in BMI_result is smaller or equal to 25
    print(f"Your BMI is {BMI_result}, you have a normal weight.")
elif BMI_result < 30: # Checks if the value in BMI_result is smaller or equal to 30
    print(f"Your BMI is {BMI_result}, you are slightly overweight.")
elif BMI_result < 35: # Checks if the value in BMI_result is smaller or equal to 35
    print(f"Your BMI is {BMI_result}, you are obese.")
else: # condition if value in BMI_result is greater tha 35
    print(f"Your BMI is {BMI_result}, you are clinically obese.")