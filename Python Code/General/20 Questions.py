"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To guess the user's number in under 20 questions
"""

import random

target = int(input("Pick a number from 1 to 100: "))
a_list = [i for i in range(1,100+1)]
counter = 1
guessed = False

user_input = input("Is your number even or odd (E/O): ")
if user_input == "E":
    a_list = [i for i in a_list if i % 2 == 0]
else:
    a_list = [i for i in a_list if i % 2 != 0]

while len(a_list) != 1:
    counter += 1
    print("Is your number higher, lower or equal than", a_list[len(a_list)//2], "(H/E/L): ")
    user_input = input("")
    if user_input == "H":
        a_list = a_list[len(a_list)//2 + 1:]
    elif user_input == "L":
        a_list = a_list[:len(a_list)//2]
    else:
        print("Your number is", a_list[len(a_list)//2])
        print("It took", counter, "questions")
        guessed = True
        break

if not guessed:
    print("Your number is", a_list[0])
    print("It took", counter, "questions")