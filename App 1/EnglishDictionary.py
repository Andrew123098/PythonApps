import json      #Library lets us manipulate .json files
import difflib   #Library lets us find words that are close to e/o and numerically rank how similar they are
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))  #Open .json file using library 

########################################################################################################################################
# Value Finder Function:                               #
# This function takes in a word given my the user and  #
# either returns that the word does not exist, returns #
# the definition(s) of the word (including pronouns    #
# and acronyms) in a list or, finds the most similar   #
# word and asks you if you meant to type that word.    # 
########################################################
def valueFinder(keyValue):
    if keyValue in data:
        return data[keyValue]
    elif keyValue.title() in data:
        return data[keyValue.title()]
    elif keyValue.upper() in data:
        return data[keyValue.upper()]
    elif len(get_close_matches(keyValue, data.keys())) > 0:
        print(f"Did you mean {get_close_matches(keyValue, data.keys())[0]} instead? ")
        yes_no = input(" Please enter Y/N: ").lower()
        if yes_no == "y":
            return data[get_close_matches(keyValue, data.keys())[0]]
        elif yes_no == "n":
            return "Word does not exist."
        else: 
            print("We did not understand your entry.")
    else: 
        return "Word does not exist."
#################################################################################################################################### 

user_key = input("Enter word: ").lower()  #Ask the user to input a word and convert it to lowercase

definition = valueFinder(user_key)    #Call the function we made


if type(definition) == list:  #Differentiate b/w strings and a list of definitions.
    for item in definition:   #Loops through items in the definitions list
        print(item)           #Prints all items in the list
else:
    print(definition)
