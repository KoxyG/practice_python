import os

try:
    myFile = open("mydata2.txt", encoding="utf-8") :

except fileNotFoundError as ex:
    print("That file was not found")

    #printing content
else:
    print("file :", myFile.read())
    myFile.close()
finally:
    print("finished working with file")