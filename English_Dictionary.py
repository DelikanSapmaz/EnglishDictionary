import json
from difflib import get_close_matches as match



data=json.load(open("data.json"))

def dictionary(word):
    word = word.lower()
    if(word in data):
        return data[word]
    elif(len(match(word,data.keys(),cutoff=0.7))>0):
        answer=input("Did you mean {} instead? Enter Y if yes, or N if no:".format(match(word,data.keys())[0]))
        if answer=="Y":
            return data[match(word,data.keys())[0]]
        else:
            return "The word doesn't exist. Please double check it."

word=input('Enter a word:')

answers_received=dictionary(word)
if type(answers_received)==list:
    for i in answers_received:
        print(i)
else:
    print(answers_received)