"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To iteratively draw a bowtie in python
"""

height = int(input("Enter the height of bowtie (should be an odd number): "))
symbol = "*"
space = " "

bowlength = height*2

if height %2 != 0 and height > 0:
  for number in range (1,height+1,2):
    temp = symbol*number
    tempLen = len(temp)
    last_line = (temp + space*(bowlength - 2*tempLen) + temp)
    print(last_line)

  for number in range (height-2,0,-2):
    temp = symbol*number
    tempLen = len(temp)
    print(temp + space*(bowlength - 2*tempLen) + temp)
else:
  print("Height must be an odd number and/or greater than 0!")