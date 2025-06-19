import json
import const
class AppConfig:
    def __init__(self, username=""):
        self.username = username
        self.data = {}      # Hold the whole json object, and config data
        self.decks = []     # List of decks in the json

    def load_data(self, path=const.DEFAULT_PATH):
        try:
            with open(path,'r') as f:
                self.data = json.loads(f.read())
                for deck in self.data:
                    self.decks.append(deck)
        except Exception as e:
            print("Load error: ", str(e))
    
    def save_data_to_json(self,path=const.DEFAULT_PATH):
        try:
            with open(path, 'w') as f:
                json.dump(self, f, default=lambda x: x.__json__() if hasattr(x, '__json__') else None)
        except Exception  as e:
            print("Save error: ", str(e))

    def debug_output_deck(self):
        print(self.decks[0])