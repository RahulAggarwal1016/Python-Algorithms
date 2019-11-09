"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Lychel Number Implementation
https://www.geeksforgeeks.org/lychrel-number-implementation/
"""

def palin(num):
    "Determines if a number is a palindrome"
    return str(num) == str(num)[::-1]

sequence_lengths = []
number_list = []
answer_list = []

#Question Number 1

for i in range(1, 195):
    length = 0
    number_list.append(i)
    while not(palin(i)):
        i = i + int(str(i)[::-1])
        length += 1
    answer_list.append(i)
    sequence_lengths.append(length)

location = sequence_lengths.index(max(sequence_lengths))

print(number_list)
print(" ")
print(sequence_lengths)
print(" ")
print(answer_list)
print(" ")

print(number_list[location])

#Question 2

print(sequence_lengths[location])

#Question 3

print(max(answer_list))

#Question 4

counter = 0

for i in sequence_lengths:
    if i >= 2:
        counter += 1

print(counter)