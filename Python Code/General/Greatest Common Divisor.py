"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the greatest common divisor of a list of number
"""

import random

a = int(input())
b = int(input())

numbers = int(input())
ourValues = [random.randint(a,b) for x in range(numbers)]

print(ourValues)

GCD = 0
smallestNumber = min(ourValues)

for divisor in range(1, smallestNumber +1):
    counter = 0
    for i in ourValues: 
        if i % divisor == 0:
            counter += 1
    if counter == len(ourValues):
        GCD = divisor

print("GCD is:", GCD)