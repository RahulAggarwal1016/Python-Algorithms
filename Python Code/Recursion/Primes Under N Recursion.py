"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find all the prime numbers under N
"""

def isPrime(num):
    a_list = [i for i in range(1, num+1) if num % i == 0]
    if len(a_list) == 2:
        return True
    else:
        return False

def primesUnder(num, i = 1, result = []):
    if i > num:
        return result
    else:
        if isPrime(i):
            result.append(i)
        return primesUnder(num, i + 1)

print(primesUnder(50))