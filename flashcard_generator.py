import json
from obj import class_deck
import sys
import const

# Load modules from other directories
sys.path.insert(0,'./obj')


"""
Function: is_a_word
Description: Check if a text string is a word. If it contains a number or symbol, return False.
Parameters:
    - text (string): A string of word.
Return: boolean
"""
def is_a_word(text):
    for char in text:
        if not char.isalpha():
            return False
    return True


"""
Function: initialize_dictionary_from_text
Description: Initialize a dictionary of words. 
Parameters:
    - text (string): A string of text.
Return: dict
"""
def initialize_dictionary_from_text(text):
    word_dictionary={}
    words = map(lambda word:word.strip(',.;?/\'\"\\+-_= '),
                text.lower().split())

    for word in words:
        if not is_a_word(word):
            continue

        if word not in word_dictionary.keys():
            word_dictionary[word] = class_deck.Card(word)

    return word_dictionary


dictionary_from_string = initialize_dictionary_from_text(const.SAMPLE)
print(dictionary_from_string)


with open('result.json', 'w') as fp:
    json.dump(dictionary_from_string, fp, default=lambda x: x.__json__() if hasattr(x, '__json__') else None)
