import Caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(Caesar_art.logo)
direction = input("Type 'encrypt' to encrypt, type 'decrypt' to decrypt:\n").lower()


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):
    

    new_text = []

    for letter in text: # or for i in range (0, len(text))

        position_in_alphabet = 0
        
        position_in_alphabet = alphabet.index(letter) # -> other option for getting the index of an item in a list

        # for l in range(0, len(alphabet)):

        #     if letter == alphabet[l]: # Checks if the letter from the variable text at the index i (from the for loop) equals the letter in the list alphabet at the position l
        #         position_in_alphabet = l

        shift_value = position_in_alphabet + shift

        if shift_value >= len(alphabet): # Checks if the value stored in shift_value is bigger or equal to the length of the alphabet (without this the shift_value could be longer than the length of the alphabet which would cause a index out of range error)
           shift_value -= len(alphabet) # subtracts the value of the length of the alphabet from the shift_value

        new_text.append(alphabet[shift_value]) # Appends the shifted letter in the alphabet to the variable new_text

    # print(new_text) 
    new_text_string = ''.join(new_text).upper() # Converts the list into a string and makes it upper case
    print(new_text_string)

def decrypt(text, shift):

    
    
    new_text = []

    for letter in text: # or for i in range (0, len(text))

        position_in_alphabet = 0
        
        position_in_alphabet = alphabet.index(letter) # -> other option for getting the index of an item in a list

        # for l in range(0, len(alphabet)):

        #     if letter == alphabet[l]: # Checks if the letter from the variable text at the index i (from the for loop) equals the letter in the list alphabet at the position l
        #         position_in_alphabet = l

        shift_value = position_in_alphabet - shift

        if shift_value >= len(alphabet): # Checks if the value stored in shift_value is bigger or equal to the length of the alphabet (without this the shift_value could be longer than the length of the alphabet which would cause a index out of range error)
           shift_value -= len(alphabet) # subtracts the value of the length of the alphabet from the shift_value

        new_text.append(alphabet[shift_value]) # Appends the shifted letter in the alphabet to the variable new_text

    # print(new_text) 
    new_text_string = ''.join(new_text).upper() # Converts the list into a string and makes it upper case
    print(new_text_string)

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
#TODO-4: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function
#based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encrypt":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
elif direction == "decrypt":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(text, shift)
else:
    print("Wrong input")