"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the factors of a number recursively
"""

def factors(num, i = 1, result = []):
    if i > num:
        return result
    else:
        if num % i == 0:
            result.append(i)
        return factors(num, i + 1)

print(factors(34))