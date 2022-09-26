# To open files you can use the open function:

file = open("/Users/PVTJL/Desktop") # you have to use an absolute or relative path 

# The relative path is the path relative to the folder you are workin in. Example: You are currently working in the directory: C:\Users\PVTJL\OneDrive\Work-Education\Coding\Development\Languages\Python
# This means that a relative file path would be something like: Dayx/file_name.extension

# An absolute file path is the path that originates in the root directory (relative to the root directory): 
# Example: /Users/PVTJL/OneDrive/Work-Education/Coding/Development/Languages/Python/Day24/file.extension # it is important that you use a forward slash!
# To got back in your folder hierachy you can use: ../

# To read a file you use the .read function. This returns the contents of the file as a string:

contents = file.read()

print(contents)

file.close() # after being done with working on the file you have to close it again

# There is also another way of opening files without having to open them again: 

with open("Day24/my_files.txt") as file:
    contents = file.read()
    print(contents)


# Writing to a file:

with open("Day24/my_files.txt", mode = "w") as file: # In order to write to a file you have to change the mode for the open function to write -> "w"
    file.write("New Text.\n") # Replaces the old text with the string inside the .write() function

# To just add to the file

with open("Day24/my_files.txt", mode = "a") as file: # In order to add to a file you have to change the mode for the open function to append -> "a"
    file.write("New Text.") # Replaces the old text with the string inside the .write() function


# If open a file in write mode that does not exist, it will automatically create a new file for you:

with open("Day24/new_file.txt", mode = "w") as file: # In order to write to a file you have to change the mode for the open function to write -> "w"
    file.write("New Text.\n") # Replaces the old text with the string inside the .write() function