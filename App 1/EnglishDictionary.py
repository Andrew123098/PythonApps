import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

data = json.load(open("data.json"))

def valueFinder(keyValue):
    if keyValue in data:
        return data[keyValue]
    elif len(get_close_matches(keyValue, data.keys())) > 0:
        print(f"Did you mean {get_close_matches(keyValue, data.keys())[0]} instead? ")
        yes_no = input(" Please enter Y/N: ").lower()
        if yes_no == 'y':
            keyValue = get_close_matches(keyValue, data.keys())[0]
            return data[keyValue]
        else:
            return "Word does not exist"
    else: 
        return "Word does not exist."

    

user_key = input("Enter word: ").lower()

definition = valueFinder(user_key)
print(definition)

