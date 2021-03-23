import json
from difflib import get_close_matches

data = json.load(open("./data.json"))

# Function for dealing with multiple or single definitions:
def numberOfDefinitions(word):
  if len(data[word]) > 1:
    print("The word is: {}\nThe definitions are:\n".format(word))
    i = 0
    while i < len(data[word]):
      print("\t*" + data[word][i])
      i += 1 
    return
  else:
    print("The word is: {}\nThe definition is: \n\t*{}".format(word, data[word][0]))
    return

def lookUp(word):
  closeMatches = get_close_matches(word, data.keys())

  # Allows for proper nouns such as "Paris" to be looked up successfully:
  if word.capitalize() in data.keys():
    numberOfDefinitions(word.capitalize())
    return
  elif word.upper() in data.keys():
    numberOfDefinitions(word.upper())
    return

  if word in data.keys():
    # Below function call changes output depending on number of definitions.
    numberOfDefinitions(word)

  # Checking for close matches:
  elif len(closeMatches) > 0:
    userChoice = input("Did you mean {}?\nPlease indicate your choice with (y/n)\n".format(closeMatches[0]))
    if userChoice.lower() == "y":
      numberOfDefinitions(closeMatches[0])
  
  else:
    print("That word doesn't exist. Please double-check that you have spelt it correctly.")
    return


  
userWord = input("Please input the word whose meaning you would like to know below.\n").lower()
lookUp(userWord)