"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To build a minimum value function in python
"""
def smallest(num):
    lowest_number = max(num)
    for i in num:
        if i <= lowest_number:
            lowest_number = i
    
    return lowest_number

print(smallest([6,53,4,5,6]))