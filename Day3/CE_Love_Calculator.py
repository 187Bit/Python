# Lower() funtion: sets every upper case in a string to a lower case
# Count() function: counts all of same letters (upper and lower case are separated)

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


combined_string = name1.lower() + name2.lower()

count_first = combined_string.count("t")

count_first = count_first + combined_string.count("r")

count_first = count_first + combined_string.count("u")

count_first = count_first + combined_string.count("e")


count_second = combined_string.count("l")

count_second = count_second + combined_string.count("o")

count_second = count_second + combined_string.count("v")

count_second = count_second + combined_string.count("e")


total_count = str(count_first) + str(count_second) # You have to use the string typecast on both variables individually



if int(total_count) < 10 or int(total_count) > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif int(total_count) > 40 and int(total_count) < 50:
    print(f"Your score is {total_count}, you are alright together.")
else:
    print(f"Your score is {total_count}")