"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find all of the twin prime pairs under N
"""

def isPrime(num):
    if num <= 1:
        return False
    else:
        factorCounter = 0
        for i in range(1, num + 1):
            if num % i == 0:
                factorCounter += 1

        if factorCounter == 2:
            return True
        else:
            return False

def primeList(num2):
    temp_list = []
    for i in range (1,num2+ 1):
        if isPrime(i):
            temp_list.append(i)
    return temp_list

user_input = int(input("Enter a number to check: "))
a_list = primeList(user_input)

twinPrimeCounter = 0

for i in a_list:
    if (i + 2) in a_list:
        print ([i,i+2])
        twinPrimeCounter += 1

print("There are", twinPrimeCounter, "twin primes")