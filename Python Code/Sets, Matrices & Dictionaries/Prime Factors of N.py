"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Find the prime factors of N
"""

def isPrime(num):
    if num <= 1:
        return False
    else:
        factors = {i for i in range(1, num+1) if num % i == 0}
        if len(factors) == 2:
            return True
        else:
            return False


num = int(input("Enter a number: "))

factor_set = {i for i in range(1,num+1) if num % i == 0}

prime_factors = list(filter(isPrime, factor_set))

print(prime_factors)