"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To create a null (n by m) matrix
"""

width = int(input("Enter a width: "))
height = int(input("Enter a length: "))

temp_matrix = [[0 for x in range(width)] for j in range(height)]

def matrix(a):
    for i in a:
        print(i)

matrix(temp_matrix)