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





card_deck = class_deck.Deck()

card_deck.import_from_text(title="Dotoyevsky's life", text=const.SAMPLE)

card_deck.export_json()

