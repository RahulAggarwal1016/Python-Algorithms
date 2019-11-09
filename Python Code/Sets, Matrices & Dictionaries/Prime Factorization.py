"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Prime Factorization Tool
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

def primeFactors(num):

    factor_set = {i for i in range(1,num+1) if num % i == 0}
    prime_factors = list(filter(isPrime, factor_set))

    return prime_factors

def primeFactorization(num):

    temp = num
    prime_factors = primeFactors(num)

    temp_list = []

    while num != 1:
        for i in prime_factors:
            if num % i == 0:
                temp_list.append(i)
                num //= i
    
    return temp_list

new_dict = {}

for i in range(1, 150):
    new_dict[i] = primeFactorization(i)

print(new_dict)