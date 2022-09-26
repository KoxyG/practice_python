#a program that converts words to acronym
#Ask for a string
orig_string = input("convert to acronym: ")

#convert the string into uppercase
orig_string = orig_string.upper()
print(orig_string)

#convert the string into a list
list_of_words = orig_string.split()
print(list_of_words)

#cycle through the list
for word in list_of_words:
    #Get the first letter of the word and eliminate the newline
    print(word[0], end="")
#add a newline
print()
