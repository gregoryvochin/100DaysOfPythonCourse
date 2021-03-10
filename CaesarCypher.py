user_continue = True  # 

alphabet = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]  # double alphabet to cover shifts that go past 26 index positions

reverse_alphabet = []  # initialize reverse alphabet for decoding
for i in reversed(alphabet):  # loop through reversed alphabet list
    reverse_alphabet.append(i)  #  append reversed alphabet list to initialized list

def encode(word, shift):  # define encode function
    output = ""  # initialize output string
    word_list = []  # initialize character list
    
    for char in word:  # loop through inputed word
        word_list.append(char)  # add each character to the word list

    for i in range(0, len(word_list)):  # loop through range the size of the alphabet list
        if word_list[i] in alphabet: #shift each character by the amount the user selected
            x = alphabet.index(word_list[i])
            x += int(shift)
            word_list[i] = alphabet[x]
            output += word_list[i]
    return "\nYour encode mesage is: \n" + output + "\n"
            

def decode(word, shift):
    output = ""
    word_list = []
    for char in word:
        word_list.append(char)

    for i in range(0, len(word_list)):
        if word_list[i] in reverse_alphabet:
            x = reverse_alphabet.index(word_list[i])
            x += int(shift)
            word_list[i] = reverse_alphabet[x]
            output += word_list[i]
    return "\nYour decoded message is: \n" + output + "\n"

while user_continue is True:  # run program until user decides to exit
    user_mode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")  # select encode or decode

    if user_mode == "encode":
        print(encode(input("\nType your message: \n"), input("Enter your shift number: \n")))

    else:
        print(decode(input("\nType your message: \n"), input("Enter your shift number: \n")))

    yes_or_no = input("Type 'yes' to go again, or 'no' to end the program: ")
    if yes_or_no == "no":
        user_continue = False

  # NEXT VERSION SHOULD CONSOLIDATE THE ENCODE AND DECODE FUNCTIONS INTO ONE
        
