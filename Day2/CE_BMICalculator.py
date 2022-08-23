# 🚨 Don't change the code below 👇
height = input("enter your height in m: ") #gets the user's height input (type: string)
weight = input("enter your weight in kg: ") #gets the user's weight input (type: string)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi_result = int(weight) / float(height) ** 2 #converts the weight into an integer and the height into a float, makes the height to the power of two and adds the two values
print(int(bmi_result)) #print the bmi_result as a whole number (int)