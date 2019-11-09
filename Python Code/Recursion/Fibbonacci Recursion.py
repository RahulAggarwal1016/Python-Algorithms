"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the Nth fibbonacci number recursively
"""

def fib(num):
    if num <= 1:
        return num
    else:
        return fib(num - 1)  + fib(num - 2)

print(fib(6))