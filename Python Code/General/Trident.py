"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To iteratively draw a trident in python
"""

tineHeight = int(input("Enter the height of the tine: "))
tineSpace = int(input("Enter the space between the tines: "))
handleHeight = int(input("Enter the height of the handle: "))

space = " "
symbol = "*"

for i in range (1, tineHeight + 1):
  first_part = (symbol + (space*tineSpace) + symbol + (space*tineSpace) + symbol)
  print(first_part)

firstlen = len(first_part)

line = symbol*firstlen

print(line)

for b in range (1, handleHeight + 1):
  print(space*(tineSpace + 1) + symbol + space*(tineSpace + 1))