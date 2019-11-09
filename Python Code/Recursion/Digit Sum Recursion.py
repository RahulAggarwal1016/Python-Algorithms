"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To calculate the sum of a number's digits
"""

def digitSum(num, total = 0):
    num = str(num)
    total += int(num[0])
    
    if len(num) == 1:
        return total
    else:
        return digitSum(num[1:], total)

print(digitSum(143))