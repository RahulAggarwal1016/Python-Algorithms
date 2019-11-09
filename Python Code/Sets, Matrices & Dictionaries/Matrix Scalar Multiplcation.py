"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To perform scalar multiplcation on a given matrix
"""

def matrix(a):
    for i in a:
        print(i)

a_list = [[1,8,3],[4,2,-5]]

matrix(a_list)

print(" ")

def scalar_multiply(a,num):

    master_list = []
    for i in a:
        temp_list = []
        for j in i:
            temp_list.append(j*num)
        master_list.append(temp_list)
    return master_list

matrix(scalar_multiply(a_list, 2))