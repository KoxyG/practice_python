#Note: A prime number is a number that can only be divided by 1 and itself
#A function that checks for the lists of primes in a number
#gets the number, stores it in a list and prints out all the prime numbers in that number

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
        return True

#A function that gets the prime numbers and put it inside a list

def get_primes(max_number):
    list_of_primes = []
    for num1 in range(2, max_number):
        if is_prime(num1):
            list_of_primes.append(num1)
    return list_of_primes
max_num_check = int(input("Search for prime: "))

list_of_primes = get_primes(max_num_check)

for prime in list_of_primes:
    print(prime)
