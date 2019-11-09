"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To count the number of vowels in a string
"""

def vowelCounter(word, vowels = 0):

    if not len(word):
        return vowels
    else:
        if word[0] in "aeiou":
            vowels += 1
        return vowelCounter(word[1:], vowels)

print(vowelCounter("e"))