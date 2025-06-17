import json
import class_word_dictionary as clwd
from sample_data import *

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
    words = text.lower().split()
    for word in words:
        word = word.strip(',.;?/\'\"\\+-_= ')
        if not is_a_word(word):
            continue
        if word not in word_dictionary.keys():
            word_dictionary[word] = clwd.Word(word)
    return word_dictionary


dictionary_from_string = initialize_dictionary_from_text(SAMPLE)
print(dictionary_from_string)

with open('result.json', 'w') as fp:
    json.dump(dictionary_from_string, fp, default=lambda x: x.__json__() if hasattr(x, '__json__') else None)
