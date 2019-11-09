"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To perform the "search function" algorithm recursively
"""

def search(array, location, counter = 0):
    if location > len(array) - 1:
        return -1
    else:
        if counter == location:
            return array[location]
        else:
            return search(array, location, counter + 1)

print(search("hello", 1))