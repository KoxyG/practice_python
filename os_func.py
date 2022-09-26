import os

with open("mydata.txt", mode="w", encoding="utf-8") as myfile:
    myfile.write("some random text\nMore randomtext\nAnd some more")

with open("mydata.txt", encoding="utf-8") as myfile:
    print(myfile.read())

#os commands
os.rename("mydata.txt", "mydata2.txt")
os.remove("mydata2.txt")
os.mkdir("del")
os.chdir("del")

print("current directory : ", os.getcwd())