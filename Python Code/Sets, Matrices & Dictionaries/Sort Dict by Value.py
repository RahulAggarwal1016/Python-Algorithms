"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To sort a dictionary by its value
"""

random_dict = {"Two": 2, "One": 1, "Three": 3, "Five": 5, "Four": 4}

sorted_values = []
values_list = list(random_dict.values())

while values_list:
    sorted_values.append(min(values_list))
    values_list.remove(min(values_list))

master_list = []

while sorted_values:
    for i in random_dict:
        if random_dict[i] == sorted_values[0]:
            master_list.append((i,random_dict[i]))
    sorted_values.remove(sorted_values[0])

print(dict(master_list))