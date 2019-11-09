"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To determine if a string is a palindrome
"""

def ispalin(word):
    if not word:
        return True
    elif len(word) == 1:
        return True
    else:
        return word[0] == word[-1] and ispalin(word[1:-1])

print(ispalin("tacocat"))