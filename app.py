import json
from difflib import get_close_matches

data = json.load(open("C:/Users/Bido2/Downloads/data.json"))

def numberOfDefinitions(word):
  if len(data[word]) > 0:
    print("The word is: {}\nThe definitions are:\n".format(word))
    i = 0
    while i < len(data[word]):
      print(data[word][i])
      i += 1 
    return
  else:
    print("The word is: {}\nThe definition is: \n{}".format(word, data[word]))
    return

def lookUp(word):
  closeMatches = get_close_matches(word, data.keys())

  if word in data.keys():
    # The below function call changes output depending of number of definitions.
    numberOfDefinitions(word)

  # Checking for close matches:
  elif len(closeMatches) > 0:
    userChoice = input("Did you mean {}?\nPlease indicate your choice with (y/n)\n.".format(closeMatches[0]))
    if userChoice.lower() == "y":
      numberOfDefinitions(closeMatches[0])
  
  else:
    print("That word doesn't exist. Please double-check that you have spelt it correctly.")
    return


  
userWord = input("Please input the word whose meaning you would like to know below.\n").lower()
lookUp(userWord)