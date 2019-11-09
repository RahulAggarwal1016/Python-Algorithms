"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To convert an integer into it's word form
"""

def name(number):
    str_num = str(number)
    if len(str_num) == 4:
        return "OneThousand"
    else:
        name_string = ""
        if len(str_num) == 3:
            a_list = list(str_num)
            counter = 0
            while counter <= 2:
                if counter == 0 or counter == 2:
                    if a_list[counter] == "1":
                        name_string += "one"
                    elif a_list[counter] == "2":
                        name_string += "two"
                    elif a_list[counter] == "3":
                        name_string += "three"
                    elif a_list[counter] == "4":
                        name_string += "four"
                    elif a_list[counter] == "5":
                        name_string += "five"
                    elif a_list[counter] == "6":
                        name_string += "six"
                    elif a_list[counter] == "7":
                        name_string+= "seven"
                    elif a_list[counter] == "8":
                        name_string += "eight"
                    elif a_list[counter] == "9":
                        name_string += "nine"
                    if counter == 0:
                        name_string += "hundred"
                if counter == 1:
                    if a_list[counter] == "1":
                        if a_list[counter +1] == "0":
                            name_string += "ten"
                        if a_list[counter + 1] == "1":
                            name_string += "eleven"
                        if a_list[counter + 1] == "2":
                            name_string += "twelve"
                        if a_list[counter + 1] == "3":
                            name_string += "thirteen"
                        if a_list[counter + 1] == "4":
                            name_string += "fourteen"
                        if a_list[counter + 1] == "5":
                            name_string += "fifteen"
                        if a_list[counter + 1] == "6":
                            name_string += "sixteen"
                        if a_list[counter + 1] == "7":
                            name_string += "seventeen"
                        if a_list[counter + 1] == "8":
                            name_string += "eighteen"
                        if a_list[counter + 1] == "9":
                            name_string += "nineteen"
                        return name_string
                    else:
                        if a_list[counter] == "2":
                            name_string += "twenty"
                        if a_list[counter] == "3":
                            name_string += "thirty"
                        if a_list[counter] == "4":
                            name_string += "forty"
                        if a_list[counter] == "5":
                            name_string += "fifty"
                        if a_list[counter] == "6":
                            name_string += "sixty"
                        if a_list[counter] == "7":
                            name_string += "seventy"
                        if a_list[counter] == "8":
                            name_string += "eighty"
                        if a_list[counter] == "9":
                            name_string += "ninety"
                counter += 1

        if len(str_num) == 2:
            a_list = list(str_num)
            counter2 = 0
            while counter2 <= 1:
                if counter2 == 0:
                    if a_list[counter2] == "1":
                        if a_list[counter2] == "0":
                            name_string += "ten"
                        if a_list[counter2] == "1":
                            name_string += "eleven"
                        if a_list[counter2] == "2":
                            name_string += "twelve"
                        if a_list[counter2] == "3":
                            name_string += "thirteen"
                        if a_list[counter2] == "4":
                            name_string += "fourteen"
                        if a_list[counter2] == "5":
                            name_string += "fifteen"
                        if a_list[counter2] == "6":
                            name_string += "sixteen"
                        if a_list[counter2] == "7":
                            name_string += "seventeen"
                        if a_list[counter2] == "8":
                            name_string += "eighteen"
                        if a_list[counter2] == "9":
                            name_string += "nineteen"
                        return name_string
                if counter2 == 1:
                    if a_list[counter2] == "1":
                        if a_list[counter2] == "1":
                            name_string += "one"
                        if a_list[counter2] == "2":
                            name_string += "two"
                        if a_list[counter2] == "3":
                            name_string += "three"
                        if a_list[counter2] == "4":
                            name_string += "four"
                        if a_list[counter2] == "5":
                            name_string += "ficw"
                        if a_list[counter2] == "6":
                            name_string += "six"
                        if a_list[counter2] == "7":
                            name_string += "seven"
                        if a_list[counter2] == "8":
                            name_string += "eight"
                        if a_list[counter2] == "9":
                            name_string += "nine"
                    
                else:
                    if a_list[counter2] == "2":
                        name_string += "twenty"
                    if a_list[counter2] == "3":
                        name_string += "thirty"
                    if a_list[counter2] == "4":
                        name_string += "forty"
                    if a_list[counter2] == "5":
                        name_string += "fifty"
                    if a_list[counter2] == "6":
                        name_string += "sixty"
                    if a_list[counter2] == "7":
                        name_string += "seventy"
                    if a_list[counter2] == "8":
                        name_string += "eighty"
                    if a_list[counter2] == "9":
                        name_string += "ninety"
                counter2 += 1

        if len(str_num) == 1:
            if str_num == "1":
                name_string += "one"
            if str_num == "2":
                name_string += "two"
            if str_num == "3":
                name_string += "three"
            if str_num == "4":
                name_string += "four"
            if str_num == "5":
                name_string += "five"
            if str_num == "6":
                name_string += "six"
            if str_num == "7":
                name_string += "seven"
            if str_num == "8":
                name_string += "eight"
            if str_num == "9":
                name_string += "nine"
    return name_string

biggest_word = ""
biggest_length = 0 

for i in range(1, 1000+1):
    word = name(i)
    if len(word) >= biggest_length:
        biggest_word = word
        biggest_length = len(word)

print(biggest_word)                    