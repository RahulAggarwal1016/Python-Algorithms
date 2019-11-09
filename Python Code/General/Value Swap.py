"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To swap two values in a list
"""

a_list = [1,2,3,4,5,5,6,7,8,9,10]

location1 = int(input("What location do u want to switch: "))
location2 = int(input("What location do u want to switch with: "))

value2 = a_list.pop(location2)
value1 = a_list.pop(location1)

a_list.insert(location1, value2)
a_list.insert(location2, value1)

print(a_list)