# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n]) # converts the student scores strings into ints
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

highest_score = 0

for score in student_scores: # iterrates through the list of student_scores

    if score > highest_score: # checks if the current score is greater than the highest_score
        highest_score = score # replaces the highests score with the new score
    # print(f"Currently the highest score is: {highest_score}.")

print(f"The highest score in the class is: {highest_score}")