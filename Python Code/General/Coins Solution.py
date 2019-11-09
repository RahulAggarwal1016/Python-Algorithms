"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To solve the famous coins change question using two different methods
https://www.geeksforgeeks.org/coin-change-dp-7/
"""

def coins(target, coins):

    loop = True
    master_dict = {}

    for i in coins:
       master_dict[i] = 1

    while loop:

        for i in coins:

            for j in master_dict.copy():

                if i + j not in master_dict.keys():
                    master_dict[i+j] = master_dict[j] + 1
                
                if i + j == target:
                    loop = False
                    return master_dict[target]

print(coins(266,[2, 3, 6, 8, 10, 13, 14, 15, 17, 18, 19]))

# Method 2 
"""
def f(target, coins):
    
    target2 = target
    master_list = []
    coins.sort()
    coins2 = coins.copy()

    while len(coins) != 0:

        minimum_coins = []

        while target > 0:
            if len(coins) >= 1:
                if target - coins[-1] >= 0:
                    minimum_coins.append(coins[-1])
                    target -= coins[-1]
                else:
                    coins.remove(coins[-1])
            else:
                break
        
        if target == 0:
            master_list.append(minimum_coins)
            target = target2
            coins2 = coins2[0:-1]
            coins = coins2.copy()
        else:
            target = target2
            coins2 = coins2[0:-1]
            coins = coins2

    new_list = []
    for i in master_list:
        new_list.append(len(i))
    
    return min(new_list)
"""