"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find N's collatz sequence recursively
"""

def collatz(num, a_list = []):
    if num == 0:
        return -1
    else:
        a_list.append(num)
        if num == 1:
            return a_list
        else:
            if num % 2 == 0:
                return collatz(num//2)
            else:
                return collatz(num*3 + 1)

print(collatz(6)) 