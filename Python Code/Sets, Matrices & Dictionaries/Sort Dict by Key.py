"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To sort a dictionary by it's key
"""

random_list = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

new_list = []

while random_list:
    first = min(random_list)
    new_list.append((first,random_list[first]))
    del random_list[first]

print(dict(new_list))