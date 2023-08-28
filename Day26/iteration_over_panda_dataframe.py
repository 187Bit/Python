import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98],
}

# Looping through dictionaries:

# for (key,value) in student_dict.items():
#     print(key)
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)

# # Loop through the Data Frame:

# for (key,value) in student_data_frame.items():
#     print(key)
#     print(value)

# # Not useful:

# Rather use the in-built function from pandas: Loop through rows of a data frame

for (index, row) in student_data_frame.iterrows():
    print(row) # row is a series so you can tap into it
    print(row.student)
