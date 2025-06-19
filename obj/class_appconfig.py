import json
import const
import os
from .class_deck import Deck

class AppConfig:
    def __init__(self, username=""):
        self.username = username
        self.data = {}      # dict() for loading the data from a json file.
        # self.decks = []     # List of decks for passing the data inside the app. Deprecated. Use data['decks'] instead.

    ### Add new deck to current config
    # Add deck (Use array length + 1 for deck ID)
    

    ### Save and Load
    # Loading for the first time (helper of load_data)
    def first_load(self, path=const.DEFAULT_PATH):
        try:
            with open(path,'w') as f:
                self.data['decks'] = []
                new_deck = Deck()
                new_deck.import_from_text(title="default",text=const.SAMPLE)
                self.data['decks'].append(new_deck)
                self.username = "defaultuser"
        except Exception as e:
            print("Load error: ", str(e))

    # Load the json data as python object
    def load_data(self, path=const.DEFAULT_PATH):
        if os.path.exists(path) and len(self.data.keys()) > 0:
            try:
                with open(path,'r') as f:
                    self.data = json.loads(f.read())
                    self.username = self.data['username']       
            except Exception as e:
                print("Load error: ", str(e))
        else:
            self.first_load(path)

    # Save current data object to json for storage
    def save_data_to_json(self,path=const.DEFAULT_PATH):
        try:
            with open(path, 'w') as f:
                json.dump(self, f, default=lambda x: x.__json__() if hasattr(x, '__json__') else None)
        except Exception  as e:
            print("Save error: ", str(e))

    # JSON representation
    def __json__(self):
        return {
            'username': self.username,
            'decks': self.data['decks']
        }


    #### Debugging helper
    def debug_output_first_deck(self):
        print(self.data['decks'][0])