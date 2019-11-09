"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Sum of all amicable numbers from 1 to 10000
https://www.geeksforgeeks.org/pairs-amicable-numbers/
"""

ambicable_numbers = set()

def d(n):
    factor_list = []
    for i in range(1,n):
        if n % i == 0:
            factor_list.append(i)
    return sum(factor_list)

total1 = 0
total2 = 0
for i in range(1,10000):
    total = d(i)
    if d(total) == i and total != i:
        ambicable_numbers.add(i)
        ambicable_numbers.add(total)
    
print(ambicable_numbers)
print(sum(ambicable_numbers))