"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the sum of all non-prime factorials from 1 to 50001
"""

def factorial(num):
    """
    Purpose:
    This function finds the factorial of a number

    Parameter:
    Singlular integer input (num)

    Return:
    Singular integer output which is the resulting factorial
    """
    
    total = 1

    for i in range(1, num+1):
        total *= i

    return total

def isPrime(num):
    """
    Purpose:
    Determines if a number is prime

    Parameter:
    Singular integer input

    Return:
    Boolen value 
    """
    factorCounter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factorCounter += 1

    if factorCounter == 2:
        return True
    else:
        return False

#Finds prime factors between 1 and 50001

prime_numbers = []

for i in range(1,50001):
    if isPrime(i):
        prime_numbers.append(i)

#Finds prime factorial numbers

primeFactorials = []
number_starter = 1
answer = 0

while answer <= 50001:
    answer = factorial(number_starter) - 1
    if answer <= 50001 and isPrime(answer) and answer not in primeFactorials:
        primeFactorials.append(answer)

    answer = factorial(number_starter) + 1
    if answer <= 50001 and isPrime(answer) and answer not in primeFactorials:
        primeFactorials.append(answer)
    
    number_starter += 1

#Outputs the sum of numbers that are prime and not factorial primes

master_list = []

for number in prime_numbers:
    if number not in primeFactorials:
        master_list.append(number)

print(sum(master_list))
