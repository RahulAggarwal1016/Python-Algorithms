"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To solve the famous Joseph Circle Permutation Problem
https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/
"""

def one_round(people_list):

    for i in people_list:
        location = people_list.index(i)
        beside_location = location + 1
        if people_list[location] != 0:
            if beside_location >= len(people_list):
                people_list[0] = 0
            else:
                people_list[beside_location] = 0
        
    zeros = people_list.count(0)

    for j in range(1,zeros+1):
        people_list.remove(0)
    
    return (people_list)

def winner(num_of_people):

    a_list =list(range(1,num_of_people+1))

    while len(a_list) != 1:
        one_round(a_list)

    return a_list[0]

print(winner(9))