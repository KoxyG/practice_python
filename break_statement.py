#break statement transfers control to the statement right after the loop
x = "Hey there. How are you"
for i in x:
    if i == ".":
        break
    print(i, end="")

