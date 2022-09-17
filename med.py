email = input("what is wrong\n")
reply1= email.find('emergency')
reply2= email.find('joke')

if email != reply1:
    print("Do you want to make this email urgent")
elif email == reply2:
    print("Do you want to set this email as non-urgent")
else:
    ...