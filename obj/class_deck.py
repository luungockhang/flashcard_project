import json
import http

class Deck:
    def __init__(self, id, title, date_created):
        self.id = ""
        self.title = title
        self.date_created = date_created
        self.flashcards = {}

    def new_deck_from_text(self, text, url=""):
        self.__init__()
    def update_from_text(self, text, url=""):
        if url != "":
            pass # This is for url parsing from API
        
    def update_new_words(self):
        pass

class Card:
    # Allows the text to be initialized with only the text itself
    def __init__(self,text, dictionary_id=0, time_seen=0,ignored=False,back="<x>"):
        self.id = ""
        self.dictionary_id = dictionary_id
        self.front = text
        self.ignored = ignored
        self.time_seen = time_seen
        self.back = back

    # Override print method
    def __repr__(self):
        return f"""{self.front}
- Back: {self.back}
- Ignored: {self.ignored}
- Time seen: {self.time_seen}
"""
    
    # Return a dict (json-convertable object) of the class for dumping to json
    def __json__(self):
        return {'front': self.front,
                'back': self.back,
                'timeSeen': self.time_seen,
                'ignored': self.ignored}