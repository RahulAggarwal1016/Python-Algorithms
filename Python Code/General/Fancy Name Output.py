"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To output a name in N number of rows
"""

user_input = input("Enter a word: ")

wordLen = len(user_input)

for letter in range(1, wordLen + 1):
  print(user_input[0:wordLen])
  wordLen -= 1