"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To move the second half of a string to the front of itself
"""

user_input = input("Enter a word: ")
length_of_word = len(user_input)
half_word = ""

for number in range (1, (length_of_word//2) + 1):
  half_word += user_input[number-1]

other_half = user_input.replace(half_word,"")

print(user_input.replace(user_input[0:(length_of_word//2):],"") + user_input[0:(length_of_word//2):])