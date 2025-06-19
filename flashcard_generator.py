import json
from obj import class_deck
import sys
import const
from obj import class_appconfig

# Load modules from other directories
sys.path.append('./obj')
sys.path.append('./obj/class_card.py')

cfg = class_appconfig.AppConfig()
cfg.load_data()
cfg.debug_output_deck()
# card_deck = class_deck.Deck()

# card_deck.import_from_text(title="Dotoyevsky's life", text=const.SAMPLE)

# card_deck.export_json()

