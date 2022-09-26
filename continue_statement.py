#skips the statements following it an returns control to the beginning of the loop

for i in [1, 13, 36, 4, 6]:
    if i > 10:
        continue
    else:
        print(i)

#another example

for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    else:
        print("Found an odd number", num)