#a program that searches for the word emergency in each email sent

message = input("please enter a message")

if "emergency" in message:
    print("Do you want to make this email urgent?")
elif "joke" in message:
    print("Do you want to set this email as non-urgent")