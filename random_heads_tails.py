#A program that creates random heads and tails
import random

#count the list
fliplist = []

#populate the list with 100 Hs and Ts
for i in range(1, 101):
    fliplist += random.choice(['H', 'T'])
    
#output results
print("Heads : ", fliplist.count('H'))
print("Tails :", fliplist.count('T'))