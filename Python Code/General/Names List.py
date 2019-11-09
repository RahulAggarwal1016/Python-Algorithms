"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To sort and perform analytical operations on a list of names 
"""

names = ['olehl Caro', 'hello Chien', 'Cathy Rayburn','Krystyna Perrone','Carlotta Ratti' ,'Francina Gillingham', 'Angela Beyers', 'Elly Boutin','Ione Lockridge','Janessa Fleischmann','Charlyn Ryerson','Liberty Mau','Emely Hermosillo','Emmett Robie', 'Estefana Swayze','Georgette Kahle','Melina Weigle','Barbara Giuliano', 'Verline Everts','Lynell Gatlin','Celine Flesher','Marylee Ulm','Un Zucker','Ivelisse Douglas','Vasiliki Fabrizio','Myrtice Legree','Signe Serio','Georgine Wallin','Elda Plantz','Marline Brantley']

def findScore(names):
    scores = []
    for people in names:
        total = 0
        for letter in people:
            if letter.upper() in "AEIOULNSTR":
                total += 1
            elif letter.upper() in "DG":
                total += 2
            elif letter.upper() in "BCMP":
                total += 3
            elif letter.upper() in "FHVWY":
                total += 4
            elif letter.upper() in "K":
                total += 5
            elif letter.upper() in "JX":
                total += 8
            elif letter.upper() in "QZ":
                total += 10
        scores.append(total)
    
    return scores

score_list = findScore(names)
            
biggest_scores = [] 

for i in score_list:
    max_score = max(score_list)
    if i == max_score:
        biggest_scores.append(names[score_list.index(i)] + " - " + str(max_score))
        
print(biggest_scores)
print("   ")
print("   ")

lowest_scores = [] 

for i in score_list:
    small_score = min(score_list)
    if i == small_score:
        lowest_scores.append(names[score_list.index(i)] + " - " + str(small_score))

print(lowest_scores)
print("   ")
print("   ")

mode = 0

for i in score_list:
    occurence = score_list.count(i)
    if occurence >= mode:
        mode = occurence

commonNums = []

for i in score_list:
    if score_list.count(i) == mode and i not in commonNums:
        commonNums.append(i)

tempNames = names.copy()
tempScore = score_list.copy()

modeNames = []

for i in score_list:
  if i in commonNums:
    modeNames.append(tempNames[tempScore.index(i)] + ' - ' + str(i))
    tempNames.remove(tempNames[tempScore.index(i)])
    tempScore.remove(i)    

print(modeNames)
print("   ")
print("   ")

def isAnagram(word,word2):
    word.replace(" ","")
    word2.replace (" ","")
    if len(word) > len(word2) or len(word2) > len(word):
        return False
    else:
        for letter in word:
            if word.count(letter) != word2.count(letter):
                return False
        return True

counter = 0
first_names = []

while counter <= len(names) - 1:
    master_name = names[counter]
    master_name = master_name.split(" ")
    master_name = master_name[0]
    first_names.append(master_name)
    counter += 1

counter2 = 0
number_of_prints = 0

while counter2 <= len(first_names) - 1:
    temp = first_names[counter2]
    anagram_list = []
    anagram_list.append(temp + ":")
    for i in first_names:
        if isAnagram(i,temp) and i != temp:
            anagram_list.append(i)
    if len(anagram_list) != 1:
        print(anagram_list)
        number_of_prints += 1
    counter2 += 1

if number_of_prints == 0:
    print("There are no first names that are anagrams of another first name.")