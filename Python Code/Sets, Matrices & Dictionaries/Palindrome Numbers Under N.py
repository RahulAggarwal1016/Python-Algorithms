"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find all the palindrome numbers under N
"""

def isPalin(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

user_input = int(input())

a_list = [i for i in range(1,user_input+1)]
palin_list = list(filter(isPalin, a_list))
print(palin_list)