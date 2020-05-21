import json
import difflib
from difflib import get_close_matches
import datetime

data = json.load(open("data.json"))

def define(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    #elif len(get_close_matches(word, data.keys())) > 0:
        #return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
    else:
        suggestions = get_close_matches(word, data.keys())
        if len(suggestions) > 0:
            retry = input("Did you mean %s instead? Enter Y for Yes, N for No:" % suggestions[0])
            if retry == "Y":
                return data[suggestions[0]]
            elif retry == "N":
                return word + " does not exist in the dictionary. Please double check it."
            else:
                return "Sorry. I do not understand your response."
        else:
            return word + " does not exist in the dictionary. Please double check it."

user_key = input("Enter word:")

output = define(user_key)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)