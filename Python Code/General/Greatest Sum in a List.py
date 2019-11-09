"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the largest sum of an adjacent sequence in an unsorted array
"""

def greatestSubList(user_input):
    if len(user_input) <= 1:
        return user_input

    largestSum = user_input[0]
    total = 0
    randomList = []

    i = 0
    
    while i <= len(user_input)-1:
        j = i + 1
        while j <= len(user_input)-1:
            total = sum(user_input[i:j+1:1])
            if total >= largestSum:
                largestSum = total
                randomList = user_input[i:j+1:1]
            j += 1

        if j > len(user_input)-1:
            total = user_input[i]
            if total >= largestSum:
                return [total]

        i += 1

    return randomList

print(greatestSubList([1,2,3,80,150,4]))