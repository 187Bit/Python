import Caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(Caesar_art.logo)

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().

def caesar(text, shift, direction):
    
    new_text = []

    for char in text: # or for i in range (0, len(text))
        
        if char in alphabet:
            
            position_in_alphabet = alphabet.index(char) # -> other option for getting the index of an item in a list

            # You can also use the modulus instead of the if statement:

            #shift = shift  % 26

            if shift >= len(alphabet): # Checks if the value stored in shift is greater than the length of the alphabet (would cause an index error without it)
                shift -= len(alphabet) # Subtracts the lenth of the alphabet from the value stored in shift

            if direction == "encrypt":
                shift_value = position_in_alphabet + shift # Adds the shift to the position in the alphabet and stores it in the variable shift_value
            elif direction == "decrypt":
                shift_value = position_in_alphabet - shift # Subtracts the shift to the position in the alphabet and stores it in the variable shift_value
            

            if shift_value >= len(alphabet): # Checks if the value stored in shift_value is bigger or equal to the length of the alphabet (without this the shift_value could be longer than the length of the alphabet which would cause a index out of range error)
                shift_value -= len(alphabet) # subtracts the value of the length of the alphabet from the shift_value

            new_text.append(alphabet[shift_value]) # Appends the shifted letter in the alphabet to the variable new_text
        else:
            new_text.append(char) # Appends the value stored in char to the new_text

        # print(new_text) 
    new_text_string = ''.join(new_text).upper() # Converts the list into a string and makes it upper case
    print(new_text_string)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

restart = True

while restart == True:

    direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt:\n").lower()
    if direction != "encrypt" and direction != "decrypt": # Checks if the text in direction is not equal to "encrypt" and "decrypt"
        print("Wrong input")
    else: #If the text in direction is equal to "encrypt" or "decrypt"
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction) # Calls the function caesar() with the arguments
    
    restart_input = input("Do you want to restart the program? Type 'yes' or 'no'").lower()
    if restart_input == "no":
        restart = False


print("Thank you for using the Caesar-Cypher. Good bye!")


