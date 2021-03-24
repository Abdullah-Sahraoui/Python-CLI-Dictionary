import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
  user = "ardit700_student",
  password = "ardit700_student",
  host = "108.167.140.122",
  database = "ardit700_pm1database"
)

cursor = con.cursor()

def numberOfDefinitions(word, results):
  # case of multiple definitions:
  if len(results) > 1:
    print("The word is: {}\nThe definitions are:\n".format(word))
    for res in results:
      print("\033[1;32;40m\t*" + res[1])
    return
  
  # case of single definition:
  else:
    print("The word is: {}\nThe definition is:\n\t\033[1;32;40m*{}".format(results[0][0], results[0][1]))
    return

def lookUp(userWord):
  query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(userWord))

  # "results" returns a list of tuples for different definitions of the same word.
  results = cursor.fetchall()
  closeMatches = get_close_matches(userWord, results)

  # allows for proper nouns like "Paris" and acronyms like "USA" to be looked up successfully:
  if userWord.capitalize() in results:
    numberOfDefinitions(userWord.capitalize(), results)
    return
  elif userWord.upper() in results:
    numberOfDefinitions(userWord.upper(), results)
    return

  if results:
    numberOfDefinitions(userWord, results)
  else:
    print("The word is: {}\nThe definition is: \t\033[1;32;40m*{}".format(userWord, results[0][1]))


userInput = input("Please input the word whose meaning you would like to know below.\n").lower()
lookUp(userInput)