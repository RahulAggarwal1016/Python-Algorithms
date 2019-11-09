"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To determine when all candidates in CS city will change positions
"""

current_year = int(input("Enter the current year: "))
future_year = int(input("Enter the future year: "))
difference = future_year - current_year
temp = 1
RealYear = 0

while temp <= difference:
  if temp % 2 == 0 and temp % 3 == 0 and temp % 4 == 0 and temp % 5 == 0:
    print("All positions change on: ",current_year + temp)
    RealYear += 1
  temp += 1

if RealYear == 0:
  print("There is no year where all positions change.")