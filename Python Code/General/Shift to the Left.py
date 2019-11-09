"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To shift an array one index to the left
"""

empty = []

for i in range(1,7):
  word = int(input("Enter a number: "))
  empty.append(word)

temp = empty.pop(0)
empty += [temp]

print(empty)