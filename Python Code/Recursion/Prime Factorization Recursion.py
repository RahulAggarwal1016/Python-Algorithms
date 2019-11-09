"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To prime factorize a number recursively
"""

def isPrime(num):
    a_list = [i for i in range(1, num+1) if num % i == 0]
    if len(a_list) == 2:
        return True
    else:
        return False

def prime_fac(num, i = 2, result = []):
    if not result and num == 1:
        return [1]
    elif num == 1:
        return result
    else:
        while num % i == 0:
            if isPrime(i):
                result.append(i)
                num //= i
                
        return prime_fac(num, i + 1, result)

print(prime_fac(12))