"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To perform the "linear search" algorithm recursively
"""

def linear(array,targ,track=0):

    look = array[track]

    if look != targ:
        return linear(array,targ,track + 1)
    else:
        return track

print(linear([1,2,3,4], 3))