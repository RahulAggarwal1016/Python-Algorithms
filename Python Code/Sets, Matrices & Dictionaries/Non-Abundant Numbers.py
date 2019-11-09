"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Find all abundant numbers from 14 to 28124:
https://www.tutorialspoint.com/abundant-number-in-c
"""

https://www.tutorialspoint.com/abundant-number-in-c

def isAbun(n):
    factor_list = []
    for i in range(1,n):
        if n % i == 0:
            factor_list.append(i)
    if sum(factor_list) > n:
        return True
    else:
        return False

master_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]

abuns_under = {}

abuns_under[13] = [12]

for i in range(14, 28123 + 1):

    if isAbun(i-1):
        abuns_under[i] = abuns_under[i-1] + [i-1]
    else:
        abuns_under[i] = abuns_under[i-1]
    
    j = 0
    k = len(abuns_under[i]) - 1

    loop = True

    while j != k:
        total = abuns_under[i][j] + abuns_under[i][k]
        if total == i:
            loop = False
            break
        elif total < i:
            j += 1
        elif total > i:
            k -= 1
    if loop:
        master_list.append(i)

print(master_list)
print(sum(master_list))