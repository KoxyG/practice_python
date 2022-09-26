#creating a list of even numbers

#converting a string into a list
rand_string = "this is just a word"
a_list = ["Bunch", "of", "random", "words"]
print(" ".join(a_list))

a_list2 = rand_string.split()
for i in a_list2:
    print(i)

evenlist = [i * 2 for i in range(10)]
for k in evenlist:
    print(k, end=", ")
print()

#list containing values to the power of 2, 3, 4
numlist = [1, 2, 3, 4, 5]

listofvalues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numlist]
for j in listofvalues:
    print(j)

#creating a 10*10 list
multiDlist = [[0] * 10 for i in range(10)]
multiDlist[0][1] = 10 #change a value in the multidimensional list

print(multiDlist[0][1])
print(multiDlist[1][1]) #second item in a list


#showing how index works in multidimentional list
listTable = [[0] * 10 for i in range(10)]

for i in range(10):
    for j in range(10):
        listTable[i][j] = "{} : {}".format(i, j)

for i in range(10):
    for j in range(10):
        print(listTable[i][j], end=" || ")
    print()

#-----------Problem: CREATE A MULTIPLICATION TABLE
#with two loops fill the cells in a multidimentional list
#list with a multiplication table using 1-9

mullist = [[0] * 10 for i in range(10)]
for i in range(1, 10):
    for j in range(1, 10):
        mullist[i][j] = i * j

for i in range(1, 10):
    for j in range(1, 10):
        print(mullist[i][j], end=", ")
    print()