"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To prime factorize each number from 1 to 1000 and 
find the sum of their respective values
"""

def isPrime(num):
    factorCounter = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factorCounter += 1

    if factorCounter == 2:
        return True
    else:
        return False

def primeFactors(num):
    primeFactors_list = []

    for i in range(1,num + 1):
        if num % i == 0 and isPrime(i):
            primeFactors_list.append(i)
    
    return primeFactors_list

for i in range(2,1001):
    number = i
    prime_factor_list = primeFactors(i)
    master_list = []

    while number != 1:
        for divisible in prime_factor_list:
            if number % divisible == 0:
                master_list.append(divisible)
                number = number/divisible
        
    print("The number is:", i)
    master_list.sort()
    print(master_list)
    print(sum(master_list))