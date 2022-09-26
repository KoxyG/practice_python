#A recursive function is a function that calls itself inside itself
#factorial of 3! is 3! = 3 * 2 * 1

def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num - 1)
        return result
print("4! = ", factorial(4))
