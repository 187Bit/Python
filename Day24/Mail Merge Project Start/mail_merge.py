#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Day24/Mail Merge Project Start/Input/Names/invited_names.txt") as people: # opens up the file invited_names.txt as people 

    names = people.readlines() # Returns all lines in the file, as a list where each line is an item in the list


for name in names: # loops through every name in the list names
    
    with open("Day24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as start_letter:
        starting_letter = start_letter.read()

    name = name.strip() # Returns a COPY of the string with leading and trailing whitespace removed.

    starting_letter = starting_letter.replace("[name]", f"{name}") # replaces the string "[name]" with the string f"{name}", returns a COPY 

    with open(f"/Users/PVTJL/Downloads/Output/Letter_{name}.txt", "w") as output: # Creates a new file with name stored in name as people
        output.write(starting_letter) # writes the edited starting letter file to output

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp