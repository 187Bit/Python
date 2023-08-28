student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇

for name in student_scores: # Loops through the dictionary student_scores and assign the value to name

    score = student_scores[name] # stores the score of the student name in the variable score
    
    if score >= 91: # Checks if the score is above or equal to 91
      student_grades[name] = "Outstanding" # Assign the string "Outstanding" to the dictionary student_grades for the corresponding name
    elif score >= 81: # Checks if the score is above or equal to 81
      student_grades[name] = "Exceeds Expectations" # Assign the string "Exceeds Expectations" to the dictionary student_grades for the corresponding name
    elif score >= 71: # Checks if the score is above or equal to 71
      student_grades[name] = "Acceptable" # Assign the string "Acceptable" to the dictionary student_grades for the corresponding name
    elif score <= 70: # Checks if the score is above or equal to 70
      student_grades[name] = "Fail" # Assign the string "Fail" to the dictionary student_grades for the corresponding name

# 🚨 Don't change the code below 👇
print(student_grades)