#while loop is used to repeat a section of code in an unknown number of times until a specific condition is met

#syntax:        while EXPRESSION:
#                           statement(s)

#asking the user to enter a number to check if a multiple of seven is entered correctely

val = int(input("enter a multiple of seven"))  #converting a string to an int since every input entered is authomatically a string
while val % 7 != 0:
    val = int(input("enter a multiple of seven"))
else: #else can  be used in python only
    print("%d is a multiple of 7" %val) #always put the modulus sign % is used in python instead of &