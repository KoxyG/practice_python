#break statement transfers control to the statement right after the loop
x = "Hey there. How are you"
for i in x:
    if i == ".":
        break
    print(i, end="")

for n in range(2, 10):
    for x in range(2, n):
         if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
         # loop fell through without finding a factor
        print(n, 'is a prime number')