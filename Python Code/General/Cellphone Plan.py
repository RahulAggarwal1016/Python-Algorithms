"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To determine the optimal phone plan given the number of daytime, 
evening and weekend hours in which the phone is used
"""

daytime = int(input())
evening = int(input())
weekend = int(input())

if daytime <= 100:
  daytime_A = 0
else:
  daytime_A = (daytime - 100)*25

evening_A = 15*evening
weekend_A = 20*weekend

total_A = daytime_A + evening_A + weekend_A

print("Plan A costs", (total_A/100), "dollars")

if daytime <= 250:
  daytime_B = 0
else:
  daytimeB = (daytime - 100)*45

evening_B = 35*evening
weekend_B = weekend*25

total_B = daytime_B + evening_B + weekend_B

print("Plan B costs", (total_B/100), "dollars")

if total_A > total_B:
  print("Plan B is cheaper")
elif total_B > total_A:
  print("Plan A is cheaper")
else:
  print("Plan A and Plan B are the same price")