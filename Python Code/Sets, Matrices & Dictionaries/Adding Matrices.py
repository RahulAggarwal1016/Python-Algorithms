"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To add two matrices
"""

def matrix(a):
    for i in a:
        print(i)

def sameMatrix(a,b):
    if len(a[0]) == len(b[0]) and len(a) == len(b):
        return True
    else:
        return False        

a1 = [[1,3,1],[1,0,0]]

b1 = [[0,0,5],[7,5,0]]

print(" ")
matrix(a1)
print(" ")
matrix(b1)
print(" ")

def add(a,b):
    if sameMatrix(a,b):
        width = len(a[0])
        height = len(a)

        master_list = []

        for i in range(0,height):
            temp_list = []
            for j in range(0,width):
                thing = a[i][j] + b[i][j]
                temp_list.append(thing)
            master_list.append(temp_list)
        return master_list
    else:
        print("Cannot be added since they have different measurements")

matrix(add(a1,b1))