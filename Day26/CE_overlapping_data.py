with open("Day26/file_1.txt") as file_1:
    data_file_1 = file_1.readlines() # opens the file data_file_1 as saves it to data_file_1 as a list
with open("Day26/file_2.txt") as file_2:
    data_file_2 = file_2.readlines() # opens the file data_file_2 as saves it to data_file_1 as a list

# full_list = data_file_1 + data_file_2
# full_list = [string.strip() for string in full_list]

data_file_1 = [int(num.strip()) for num in data_file_1] # removes the \n from the data_file_1 list and converts it into an int
data_file_2 = [int(num.strip()) for num in data_file_2] # removes the \n from the data_file_2 list and converts it into an int

result = [num for num in data_file_1 if num in data_file_2] # loops through the data_file_1 list and checks if num is in the list of data_file_2
print(result)