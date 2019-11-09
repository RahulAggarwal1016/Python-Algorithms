"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To convert a number to it's binary form
"""

def binary(num):

    empty_string = ""
    pattern = "10"
    if num % 2 == 0:
        return pattern*int(num/2)
    else:
        return pattern*int((num-1)/2) + "1"

print(binary(34))