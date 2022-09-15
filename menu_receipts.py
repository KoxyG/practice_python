#writing a program that prints prints a waiter's receipt that prints the extra charges

total = 19 + 9.99 + 13.97 + 20 + 15.97 + 9.97 + 10 * 2
party = 8
print("Receipt for your meal")

if party >= 8:
    total = total + total *.2
    print("We've added the tip automatically, since your party was eight or larger.")
    print("Total:", total)
    print("Thank you for dinning with us today!\n\n")

#another receipt program

total = 13 + 14.02 + 22.35
party = 3
print("Receipt for your meal...")

if total >= 8:
    total = total + total *.2
    print("We've added the tip automatically, since your party was eight or larger")
    print("Total:", total)
    print("Thank you for dinning with us today!")
