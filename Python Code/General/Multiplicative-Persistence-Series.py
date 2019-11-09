"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the multiplicative persistence sequence of a number
https://codegolf.stackexchange.com/questions/181958/multiplicative-persistence
"""

def series(num):
    tempList = []
    if len(str(num)) == 1:
        return [num]
    else:
        tempList.append(num)
        while len(str(tempList[-1])) != 1:
            num = str(num)
            product = 1
            for i in num:
                product *= int(i)
            num = product
            tempList.append(num)
        
        return tempList