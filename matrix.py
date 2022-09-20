#we are having two list
#i is the first list, and j is used to interates over every element in the first list
x = [[1, 2, 3], ["a", "b", "c"]]
for i in x:
    for j in i:
       # print(j) #prints with a new line
        print(j, end="") #removes the new line which is authomatically put by the print function
