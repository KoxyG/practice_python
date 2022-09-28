#find the multiple of 9 from a random 100 value list with47

#values between 1 and 1000
#filter selects items from a list based on a function

import random

#print out even number from a list
randlist = list(random.randint(1,1001) for i in range (100))

print(list(filter((lambda x: x % 9 == 0), randlist)))

                             #MAP
#Map allows us to execute a function and the list to generate a new list

#generates a list from 1 to 10
OneToTen = range(1, 11)

#The function to pass into map
def db_num(num):
    return num * 2
print(list(map(db_num, OneToTen)))
print(list(map((lambda x: x * 3), OneToTen)))

                #REDUCE
#Reduce receives a list and returns a single result

#you must import reduce
from functools import reduce

#Add up the values in a list
print(reduce((lambda x, y: x + y), range(1, 6)))