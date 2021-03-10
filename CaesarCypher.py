user_continue = True  # asks user if they would like to continue running the program

alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]  # double alphabet to cover shifts that go past 26 index positions

def caesar(word, shift, direction):  # define cypher function
    output = ""  # initialize output string
    word = word.lower()  # normalize input to lowercase characters

    if direction == "encode":
        for char in word:
            char_position = alphabet.index(char)
            new_position = char_position + int(shift)
            output += alphabet[new_position]
        return "\nYour encode mesage is: \n" + output + "\n"
    
    elif direction == "decode":
        for char in word:
            char_position = alphabet.index(char)
            new_position = char_position - int(shift)
            output += alphabet[new_position]
        return "\nYour decode mesage is: \n" + output + "\n"

    else:
        return "Please enter either 'encode' or 'decode'."
    
while user_continue is True:  # run program until user decides to exit

    print(caesar(input("\nType your message: \n"), input("Enter your shift number: \n"),
                 input("'encode' or 'decode': \n")))
    
    yes_or_no = input("Type 'yes' to go again, or 'no' to end the program: ")
    if yes_or_no == "no":
        user_continue = False

  #NEXT VERSION CAN BE MADE EVEN MORE SUCCINCT
