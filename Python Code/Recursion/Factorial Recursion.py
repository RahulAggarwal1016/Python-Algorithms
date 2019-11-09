"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Factorial Calculator
"""

def fac(num):
    if num == 1:
        return 1
    else:
        return num*fac(num - 1)

print(fac(5))