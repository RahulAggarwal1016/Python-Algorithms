"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find how many times each letter in a string occurs
"""

def occur(word):
    a_set = set()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in word:
        if i in alphabet:
            a_set.add(i)
    final = [(i, word.count(i)) for i in a_set]
    return final
    
print(occur("hello"))