"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To Create a Deck of Cards
"""

value_list = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
symbol_list = ["spades", "diamonds", 'hearts', "clovers"]

deck = [(i,j) for i in value_list for j in symbol_list]

import random

random.shuffle(deck)

for i in deck:
    print(i)