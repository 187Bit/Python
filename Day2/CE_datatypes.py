# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

a = two_digit_number[0] #stores the first character of the variable "two_digit_number" in a
b = two_digit_number[1] #stores the second character of the variable "two_digit_number" in b
a_new = int(a) #converts the string that is stored in a into and integer and stores it in a new variable
b_new = int(b) #converts the string that is stored in b into and integer and stores it in a new variable
c = a_new + b_new #adds the two integer type values together and stores it in a new variable c
c_new = str(c) #converts the integer data type c into a string and stores it in a new variable

print(a + " + " + b + " = " + c_new) #prints out the whole calculation
print(c) #only prints out the result of the calculation


#Shorter version
a = two_digit_number[0] #stores the first character of the variable "two_digit_number" in a
b = two_digit_number[1] #stores the second character of the variable "two_digit_number" in b

result = int(a) + int(b)
print(result)