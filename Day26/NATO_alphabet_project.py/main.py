student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("Day26/NATO_alphabet_project.py/nato_phonetic_alphabet.csv")
nato_phonetic_alphabet_dictionary = {row.letter:row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
# print(type(nato_phonetic_alphabet_dictionary["A"]))
user_input = input("Enter a word:\n").upper()
# string_to_list = [letter for letter in user_input]
# output = []

# for letter in string_to_list:

#     output.append(nato_phonetic_alphabet_dictionary[letter])

# or

output = [nato_phonetic_alphabet_dictionary[letter] for letter in user_input]

print(output)
