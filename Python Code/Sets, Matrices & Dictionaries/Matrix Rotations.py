"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To rotate a Matrix left and right
"""

a_matrix = [[9,13,5], [1, 11, 7], [2, 6, 3,]]

for i in a_matrix:
    print(i)

print(" ")

def left(matrix):
    last_location = len(matrix[0]) - 1
    new_list = []

    while last_location >= 0:
        temp = []
        for i in matrix:
            temp.append(i[last_location])
        last_location -= 1
        new_list.append(temp)
    return new_list

for i in left(a_matrix):
    print(i)

print(" ")

def right(matrix):
    
    new_list = []
    number = 0

    while number <= len(matrix[0]) - 1:
        temp = []
        for i in matrix:
            temp.append(i[number])
        number += 1
        new_list.append(temp)
    return new_list

for i in right(a_matrix):
    print(i)