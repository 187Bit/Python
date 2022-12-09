# Comprehension also works for dictionaries
# basic syntax: 
# new_dict = {new_key: new_value for item in list()}
# or
# new_dict = {new_key: new_value for (key,value) in dict.items()}
# you can also add a test:
# # new_dict = {new_key: new_value for (key,value) in dict.items() if test}

import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {students: random.randint(1,100) for students in names}

print(students_scores)

passed_students = {students:students_scores[students] for students in students_scores if students_scores[students] >= 60}
# or
passed_students = {students:score for (students,score) in students_scores.items() if score >= 60}
print(passed_students)