"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find all the perfect numbers from 2 to 1000 inclusively
"""

perfect = []

for i in range(2,1001):
    factorSum = 0
    for factors in range(1,i):
        if i % factors == 0:
            factorSum += factors
    if factorSum == i:
        perfect.append(i)

print(perfect)