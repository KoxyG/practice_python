#a program that splits an option equaally

numbers = input("Please enter two values seperated by a space: ".split()).split(" ") #split function converts string to a list

if int(numbers[1]) % int(numbers[0]) == 0: #changing the type to int, or typcasting
    print("Give away")
else:
    print("Eat them yourself")