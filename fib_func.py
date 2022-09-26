#fibonacci that uses a recursive function
#formular for fib. fib = fib(n-1) + fib(n-2)
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num-1) + fib(num - 2)
        return result
#asking for fibonacci values and printing them to the stdout after calling the fibonacci function
enter_command = int(input("How many fibonacci values should be found: "))
i = 1
while i < enter_command:
    fibvalue = fib(i) #calling the fib defined function
    i += 1
    print(fibvalue)
    print("All done")
#print("Fibonacci should be greater than 1")