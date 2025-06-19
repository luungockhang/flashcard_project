import json
class AppConfig:
    def __init__(self):
        self.data = {}
        self.decks = []

    def load_decks(self):
        for key in 