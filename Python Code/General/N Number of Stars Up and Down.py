"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To iteratively draw an ascending and descending star pattern in python
"""

user_input = int(input("Enter a number: "))

symbol = "*"

for number in range(1, user_input + 1):
  print(symbol)
  symbol = symbol + "*"

start = -3
for number in range (1, user_input):
  print(symbol[start::-1])
  start -=1