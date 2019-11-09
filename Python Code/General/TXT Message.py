"""
Creator: Rahul Aggarwal
Email Address: rahulaggarwal1016@gmail.com

Purpose of Code:
To convert texting language and symbols into common english phrases and words
"""

loop = True
inputs = []

while loop:
  user_input = input()
  inputs.append(user_input)
  if user_input == "TTYL":
      loop = False

listLen = len(inputs)

counter = 0
for start in range (1, listLen + 1):
  place = inputs[counter]
  temporary = ""
  if place == "CU":
    temporary = "see you"
  elif place == ":-)":
    temporary = "I'm happy"
  elif place == ":-(":
    temporary = "I'm unhappy"
  elif place == ";-)":
    temporary = "wink"
  elif place == ":-P":
    temporary = "stick out my tongue"
  elif place == "(~.~)":
    temporary = "sleepy"
  elif place == "TA":
    temporary = "totally awesome"
  elif place == "CCC":
    temporary = "Canadian Computing Contest"
  elif place == "CUZ":
    temporary = "because"
  elif place == "TY":
    temporary = "thank-you"
  elif place == "YW":
    temporary = "you're welcome"
  elif place == "TTYL":
    temporary = "talk to you later"
  else:
    temporary = place
  print(temporary)
  counter += 1