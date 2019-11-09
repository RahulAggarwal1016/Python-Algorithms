"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To compare two sets
"""

def list_compare(a_list,b_list):
    if len(a_list) != len(b_list):
        return False
    else:
        for i in a_list:
            if i in b_list:
                return False
        return True

a_list = [1,2,3]
b_list = [4,2,1]

print(list_compare(a_list,b_list))
    
a_set = {1,2,3,4}
b_set = {3,2,15,5}

def set_compare(a_set, b_set):
    length = len(a_set)
    a_set &= b_set
    if len(a_set) != length:
        return False
    else:
        return True

print(set_compare(a_set,b_set))