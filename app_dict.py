import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    """Function that searches definitions of a given word in the dictionary"""

    if word.title():
        if not word[1:].isupper():
            word = word[0] + word[1:].lower()
    else:
        word = word.lower()

    if word in data:
        return data[word]
    else:
        matches = get_close_matches(word, data.keys())
        if matches:
            for match in matches:
                answer = input("Did you mean {} instead? Enter yes or no: ".format(match)).lower()
                if answer in {"y", "yes"}:
                    return data[match]
                elif answer in {"n", "no"}:
                    continue
                else:
                    return "We didn't understand your entry."

        return "The word doesn't exist. Please double check it."

word_to_found = input("Enter word: ")

while word_to_found:
    output = translate(word_to_found)
    if isinstance(output, list):
        for item in output:
            print(item)
    else:
        print(output)
    word_to_found = input("\nEnter word: ")
