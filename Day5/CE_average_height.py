# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

last_height = 0
number_of_heights = 0

for height in student_heights:
    sum = last_height + height
    last_height = sum
    # print(f"The sum is {sum}")
    number_of_heights += 1

average_height = sum / number_of_heights

print(round(average_height))

# You are not allowed to use the len() and sum() funtions