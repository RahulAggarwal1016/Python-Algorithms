"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the greatest palindrome product
"""

palinList = []

for j in range(100,999 + 1):
    for i in range(100,999 + 1):
        total = j*i
        if str(total) == str(total)[::-1]:
            palinList.append(total)

print(max(palinList))