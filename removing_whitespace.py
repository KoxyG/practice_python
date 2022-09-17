#removing whitespace with strip() function call
first_name = "Progress "
middle_name = "Ochuko"

print(first_name.strip () + " " + middle_name) #using .strip() strips out all the whitespace/extra space at the beginning and end
                                              #of a string.

if first_name != "Progress":
    print("Who are you imposter?!!!!!")
else:
    print("Hi Progress!")

#using strip('*') function to remove wrong input in a string
wrong_input = "***It's Koxy the owner, let me in now!!****"
print(wrong_input.strip('*'))

#striping just the beginning or ending of a string using rstrip() (means rightstrip) or lstrip() (means leftstrip)
wrong_input = "***It's Koxy the owner, let me in now!!****"
print(wrong_input.strip('*'))
