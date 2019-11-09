"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To find the greatest common divisor of two numbers
"""

#Method 1
def gcd(a,b):
    if a % b == 0:
       return b
    else:
        return gcd(b, a % b)
        
print(gcd(21,7))

#Method 2
def common_divisor(num1, num2, tracker = 2, common = [1]):
    
    if num1 == num2:
        return num1
    else:
        if num1 % tracker == 0 and num2 % tracker == 0:
            common.append(tracker)
        
        if tracker == min(num1,num2):
            return max(common)
        else:
            return common_divisor(num1,num2, tracker + 1)

print(common_divisor(50,25))