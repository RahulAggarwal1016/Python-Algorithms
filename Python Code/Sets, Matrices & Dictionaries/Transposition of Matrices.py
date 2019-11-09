"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To transpose a matrix
"""

def matrix(a):
    for i in a:
        print(i)

list5 = [[1,2,3],[0,6,7]]
matrix(list5)
print(" ")

def transpos(a):
    master_list = []
    width = len(a[0])
    counter = 0
    while counter < width:
        temp_list = []
        for i in a:
            temp_list.append(i[counter])
        counter += 1
        master_list.append(temp_list)
    return master_list

matrix(transpos(list5))