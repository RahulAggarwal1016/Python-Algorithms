"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To continously calculate the average weight of a set of items until "-1"
is inputted by the user
"""

loopRunner = True
totalSum = 0
numbers = 0

while loopRunner:
  user_input = float(input("Enter a weight: "))
  totalSum += user_input
  numbers += 1
  if user_input == -1:
    totalSum += 1
    loopRunner = False
    numbers -= 1

print("The average weight is: ", totalSum/numbers)