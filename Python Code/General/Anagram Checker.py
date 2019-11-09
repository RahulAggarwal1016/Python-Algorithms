"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To check if two phrases are anagrams of each other 
"""

def isAnagram(word1,word2):
    word1 = word1.replace(" ", "")
    word2= word2.replace(" ", "")

    loop = True

    for i in word1:
        if word1.count(i) != word2.count(i):
            loop = False
    
    return loop           

print(isAnagram("coolo as wet art", "cs at waterlooo"))