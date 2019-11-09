"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To raise an integer to the power of N recursively
"""

def power(num,exponent):
    if exponent == 0:
        return 1
    else:
        return num * power(num, exponent - 1)

print(power(2,4))