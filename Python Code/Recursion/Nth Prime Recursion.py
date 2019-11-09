"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the Nth Prime Number
"""

def isPrime(num):
    factors = [i for i in range(1,num+1) if num % i == 0]
    if len(factors) == 2:
        return True
    else:
        return False

def NthPrime(target, num = 0, primes = 0):
    if primes == target:
        return num - 1
    else:
        if isPrime(num):
            primes += 1
        return NthPrime(target, num + 1, primes)

print(NthPrime(1))