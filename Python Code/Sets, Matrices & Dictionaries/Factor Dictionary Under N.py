"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the factors of every number under and including N
"""

user_input = int(input())
a_list = [i for i in range(2, user_input + 1)]

factor_dic = {}

for i in a_list:
    factor_list = []
    for j in range(1,i + 1):
        if i % j == 0:
            factor_list.append(j)
    factor_dic[i] = factor_list

print(factor_dic)