#Gets the input of the user and combines it into a band name

#1. Create a greeting for your program.
print("Welcome to the Band Name Generator") #Prints out a welcome statement
#2. Ask the user for the city that they grew up in.
city_name = input("What is the name of the city you grew up in?\n") #to start a new line place \n inside the input() function; asks the user for the city he/she/it was born
#3. Ask the user for the name of a pet.
pet_name = input("What is the name of your pet?\n") #Asks the user for the name of his/her/its pet
#4. Combine the name of their city and pet and show them their band name.
print("The name of your band would be: " + city_name + "'s" + " " + pet_name) #prints out the combined statement of the variables city_name and the pet_name
#5. Make sure the input cursor shows on a new line by adding \n into the input("something\n")
