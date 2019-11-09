"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To transform a multi digit number into a singular digit
"""

def one(num, steps = 0):
    if len(str(num)) == 1:
        return steps
    else:
        total = 0
        for i in str(num):
            total += int(i)
        num = total
        return one(num, steps + 1)

print(one(14))