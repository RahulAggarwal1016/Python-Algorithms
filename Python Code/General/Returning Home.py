"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

"""

numInstructions = int(input("How many instructions do you want to give: "))*2

instructionList = []

for i in range(1, numInstructions + 1):
    user_input = input()
    instructionList.append(user_input)

instructionList.reverse()

school = instructionList.pop(0)
instructionList += ["Home"]

temp = 0

for temp in range(numInstructions):
    if instructionList[temp] == "L":
        instructionList[temp] = "R"
    elif instructionList[temp] == "R":
        instructionList[temp]= "L"
    temp += 1

for i in instructionList:
    print(i)