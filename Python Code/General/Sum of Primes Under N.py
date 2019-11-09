"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the sum of all prime numbers under N
"""

def primeSum(number):

    primeNumbers = []

    for i in range(1, number):

        factorCounter = 0

        for j in range(1, i+1):
            if i % j == 0:
                factorCounter += 1

        if factorCounter == 2:
            primeNumbers.append(i)

    return sum(primeNumbers)

print(primeSum(10))