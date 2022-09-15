#using try or except to will hide  errors and keep programs running
#with a try/except block, the block of code under the try statement will execute until an error is encountered.
#if thay happens then and only will the block of code under the except statement execute
#trying 5/0
try:
    5/0
except:
    print("Please don't do that")

#don't want anything in my except block
try:
    5/0
except:
    pass

#trying 5/1
try:
   a = 5/1
   print("Good to go")
except:
    print(" please dont try that")

#trying a + 1
a = 5
try:
    a = a + 1
    a = a / 0
except:
    print("Please don't do that..")
    print(a)