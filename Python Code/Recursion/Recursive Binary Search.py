"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To perform the "binary search algorithm" recursively
"""

def binary_search(target, array, track = 0):
    left = 0
    right = len(array) - 1
    
    if not array:
        return track
    elif len(array) == 1 and array[0] != target:
        return -1
    else:
        middle = (left+right)//2
        if array[middle] == target:
            return track + middle
        elif array[middle] < target:
            return binary_search(target, array[middle + 1:], track + middle + 1)
        else:
            return binary_search(target, array[:middle], track)

print(binary_search(7,[1,2,3,4,5,6,7,8]))