"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To sort a list in ascending order
"""

newList = []
variable = [1,3,6,2,3,6,23,4,67,2,6,3,7,21]

while variable:
  small = min(variable)
  newList.append(small)
  variable.remove(small)

print(newList)