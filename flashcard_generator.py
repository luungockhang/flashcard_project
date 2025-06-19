import json
from obj import class_deck
import sys
import const

# Load modules from other directories
sys.path.append('./obj')
sys.path.append('./obj/class_card.py')


card_deck = class_deck.Deck()

card_deck.import_from_text(title="Dotoyevsky's life", text=const.SAMPLE)

card_deck.export_json()

