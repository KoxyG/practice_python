import os

try:
    myFile = open("mydata2.txt", encoding="utf-8")

#as helps access data and metthod in the exception class
except FileNotFoundError as ex:
    print("That file was not found")

    print(ex.args)

    #printing content
else:
    print("file :", myFile.read())
    myFile.close()
finally:
    print("finished working with file")