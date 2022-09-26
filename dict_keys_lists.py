#A customers program that asks the user for the custmers names, saves it and print them all out.

#create a list to store the custmers
customers = []

#create a loop
while True:
    #get input and make it work for y or n
    createEntry = input("Enter Customer (Yes/No) : ")
    createEntry = createEntry[0].lower()

    #check to leave loop
    if createEntry == 'n':
        break
    else:
        fName, lName = input("Enter customer name : ").split()
        #add customers data to the list
        customers.append({"fName": fName, "lName": lName})
#print customers data
for cust in customers:
    print(cust["fName"], cust["lName"])
