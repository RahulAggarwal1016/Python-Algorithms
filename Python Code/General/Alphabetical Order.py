"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To sort a word in alphabetical order
"""

def new(word):
    new_word = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i in word:
            new_word += word.count(i)*i
    return new_word

print(new("hello"))