"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
Finding fibbonanci position using dictionaries
"""

def fibnum(position):
    total1 = 0
    total2 = 1
    totaln = 0

    if position == 1:
        return total1
    if position == 2:
        return total2 
    else:
        for i in range(1, position-1):
            totaln = total1 + total2
            total1 = total2
            total2 = totaln
            
        return total2

user_input = int(input("Greatest Fib Position: "))

fib_dict = {}

for i in range(1, user_input + 1):
    fib_dict[i] = fibnum(i)

print(fib_dict)