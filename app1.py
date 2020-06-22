import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(w):
    w=w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),cutoff=0.8)) > 0:
        yn = input('Did you mean {0} instead?Enter y if yes or n for no'.format(get_close_matches(w,data.keys())[0]))
        if yn.lower() == 'y':
            return data[get_close_matches(w,data.keys())[0]]
        else:
            return 'The word doesnt exist!please double check'
    else:
        return 'please enter correct word!Word doesnt exist'

word = input('Enter a word to know its meaning: ')
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)