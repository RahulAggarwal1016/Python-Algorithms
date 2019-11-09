"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Based upon the RSA number question:
https://www.geeksforgeeks.org/rsa-algorithm-cryptography/
"""

starting_number = int(input("Enter a starting number: "))
ending_point = int(input("Enter an ending number: "))
divisor = 1
number_of_factors = 0
rsa_numbers = 0

while starting_number <= ending_point:
  while divisor <= starting_number:
      
    if starting_number % divisor == 0:
      number_of_factors += 1  
    divisor += 1
    
  if number_of_factors == 4:
    rsa_numbers += 1
    print(starting_number)

  number_of_factors = 0
  divisor = 1  
  starting_number += 1

print("There are", rsa_numbers, "rsa numbers!")