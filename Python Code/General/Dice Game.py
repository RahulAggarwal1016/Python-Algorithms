"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To determine how many ways there are to add up to 10 with N and M sided dices
"""

dice_1 = int(input("Enter the number of sides on the first dice: "))
dice_2 = int(input("Enter the number of sides on the second dice: "))
target = 10

sum_counter = 0 #This tracks how many times we add up to 10
dice_1_values = 1

while dice_1_values <= dice_1:
  dice_2_values = 1

  while dice_2_values <= dice_2:
    if dice_1_values + dice_2_values == target:
      sum_Counter += 1
      
      print(dice_1_values, "+", dice_2_values, "= 10")
      
      dice_2_values += 1
  dice_1_values += 1

print("There are", sum_counter, "many ways to add up to 10")