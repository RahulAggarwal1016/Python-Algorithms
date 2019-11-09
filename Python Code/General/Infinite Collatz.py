"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To analyze infinite collatz sequences
"""

def conjat(num):
    """
    Purpose: 
    Performs the famous conjecture sequence using the new ruleset
    
    Parameter:
    A single integer input
    
    Return:
    A single list output
    """

    a_list = []
    a_list.append(num)
    loop = True

    while loop:

        if a_list[-1] % 2 == 0:
            a_list.append(a_list[-1]//2)
        else:
            a_list.append(a_list[-1]*3 - 1)
        
        if a_list.count(a_list[-1]) == 2:
            temp = a_list.pop()
            loop = False

        if a_list[-1] == 1:
            loop = False  

    return a_list

# Finds the number of infite sequences

numInfinite = 0
infinite_nums = []

for i in range(2, 1000 + 1):
    sequence = conjat(i)
    if sequence[-1] != 1:

        numInfinite +=1
        infinite_nums.append(i)

print("There are", numInfinite, "infinite sequences.")
print(" ")

# Finds what number creates the largest infite sequence
# The length of that longest sequence
# What the longest infinite sequence is 

biggest_infinite = 0
length = 0
longest_sequence = []

for i in infinite_nums:
    if len(conjat(i)) >= length:
        biggest_infinite = i
        length = len(conjat(i))
        longest_sequence = conjat(i)

print("The number that creates the largest infinite sequence: ", biggest_infinite)
print(" AH! ")
print("The length of the longest infinite sequence: ", length)
print(" ")
print("This is the longest infinite sequence: ", longest_sequence)