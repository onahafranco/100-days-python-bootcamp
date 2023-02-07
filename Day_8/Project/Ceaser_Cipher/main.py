from art import logo
def ceaser(message, action, shift_length):
    cipher = ""
    for char in message:
        if char in alphabet: 
            position = alphabet.index(char)
            if action == "encode":
                new_position = position + shift_length
            elif  action == "decode":
                new_position = position - shift_length
            new_letter = alphabet[new_position]
            cipher = cipher + new_letter

        else:
            cipher = cipher + char #this line of code appends charcters that are not alphabets to cipher"" without altering the orignal text
    
    print(f"the {action}d word is {cipher}")


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
#note that items in list alphabet were duplicated, this is to contain inputs(alphabets) that appears towards the end of the list.
looper = True
while looper:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26 #this is to be able to contain large shift value that are above the range of letters in the list alphabet
    ceaser(message = text, action = direction, shift_length = shift) 

    repeat = input("type 'yes' if you want to go again, else type 'no'\n").lower()
    if repeat == "no":
        looper = False
        print("thank you for using Brendan's ceaser ciper, goodbye...")
