#recieve message to encrypt and the number of character to shift

message = input("Enter your message : ")
key = int(input("How many characters to shift(1 - 26): "))

#prepare secret message
secret_message = " "
#cycle through each character in the message
for char in message:
    #if it isn't a letter then keep it as it is
    if char.isalpha():
        #get charcter code and add the shift amount
        char_code = ord(char)
        char_code += key

        #if uppercase then compare to uppercase unicode
        if char.isupper():
            #if bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
            #if smaller than A add 26
            if char_code < ord('A'):
                char_code += 26
        #Do thesame for lowercase character
        else:
            #if bigger than z subtract 26
            if char_code > ord('z'):
                char_code -= 26
            #if smaller than a add 26
            if char_code < ord('a'):
                char_code += 26

        #convert from code to letter and add secret message
        secret_message += chr(char_code)

    else:
        secret_message += char
print("Encrypted : ", secret_message)

#To decrypt the only thing changes is the sign of the key
key == -key

orig_message = ""
for char in secret_message:
    #if it isn't a letter then keep it as it is
    if char.isalpha():
        #get charcter code and add the shift amount
        char_code = ord(char)
        char_code += key

        #if uppercase then compare to uppercase unicode
        if char.isupper():
            #if bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
            #if smaller than A add 26
            if char_code < ord('A'):
                char_code += 26
        #Do thesame for lowercase character
        else:
            #if bigger than z subtract 26
            if char_code > ord('z'):
                char_code -= 26
            #if smaller than a add 26
            if char_code < ord('a'):
                char_code += 26

        #convert from code to letter and add secret message
        orig_message += chr(char_code)

    else:
        orig_message += char
print("Decrypted : ", orig_message)