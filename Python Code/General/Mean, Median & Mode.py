"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the mode, median and mean of an array of 5 numbers
"""

inputs = []

for i in range(1,6):
  user_input = int(input())
  inputs.append(user_input)

total = 0
mode = 0
common_number = 0 

for number in inputs:
  total += number
  if inputs.count(number) >= common_number:
    common_number = inputs.count(number)
    mode = number
  
print("Mode:", mode)
print("Median", inputs[len(inputs)//2])
print("Mean", total/11)