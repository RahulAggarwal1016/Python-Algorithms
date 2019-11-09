"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To determine recurrsively if a number is prime
"""

def isPrime(num, i = 2):
    if num <=1:
        return False
    elif num in [2,3]:
        return True
    else:
        if num == i:
            return True
        if num % i == 0:
            return False
        return isPrime(num, i + 1)

print(isPrime(13))