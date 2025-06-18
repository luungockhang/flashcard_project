import json
import http
import datetime
from json import JSONEncoder

# Global helper functions
def is_a_word(text):
    for char in text:
        if not char.isalpha():
            return False
    return True

# Deck class - Saves the dict of a flashcard deck.
# Contains: ID for database index, User-defined title, date of update/creation.  
class Deck:
    def __init__(self, title="", date=datetime.datetime.now(), id=0, flashcards={}):
        self._id = id               # ID for indexing
        self.title = title          # Title of this deck
        self.date = date            # Date updated
        self.flashcards = {}        # The deck content

    ### Creation methods ###
    # Import flashcards from a passage of text. Title and text must be filled.
    def import_from_text(self, title="", text="", url=""):
        if url != "":
            # Logic for text parsing from API etc. Not implemented.
            # In which case the text is parsed from the url and assigned here.
            # Title could also be assigned here if the API logic is smart enough (?)
            pass

        # Raise an error if missing text or title
        if text == "" or title == "":
            raise Exception("Missing title or content.")

        # Reinit could be redundant here.
        new_deck = self.__init__(title=title)
        words = map(lambda word: word.strip(',.;?/\'\"\\+-_= '),
                    text.lower().split())   # -> list of words
        for word in words:
            if not is_a_word(word):
                continue
            if word not in self.flashcards.keys():
                self.flashcards[word] = Card(word)

    # Manual creation of decks by user
    # TODO

    ### Update methods ###
    # Update deck from text
    # TODO
    
    # Update deck by user input
    # TODO
    
    # Update individual card by user input
    # TODO

    
    def export_json(self):
        with open('result.json', 'w') as fp:
            json.dump(self, fp, default=lambda x: x.__json__() if hasattr(x, '__json__') else None)
    


    # Json export format. Must update this when changing the fields in class.
    # Check if it can save
    def __json__(self):
        return {'id': self._id,
                'title': self.title,
                'date': self.date,
                'flashcards': self.flashcards}

# Card class - There will be different card types but it's not implemented now.
class Card:
    # Allows the text to be initialized with only the text itself
    def __init__(self,front, deck_id=0,ignored=False,back="<x>", box=1):
        self.id = 0
        self.deck_id = deck_id          # ID for tying a card to one deck. In case there are two words in different decks.
        self.front = front              # The word string that is the front of this card, also the key of this card.
        self.ignored = ignored          # If the user decides not to review this, it is True.
        self.back = back                # The "back" of this card, which usually has the definition of the word.
        self._box = 1                   # The "box" to put this card in, for spaced repetition simulation of flashcard usage.

    # Override print method
    def __repr__(self):
        return f"""{self.front}
- Back: {self.back}
- Ignored: {self.ignored}
- Time seen: {self._time_seen}
"""
    
    # Json export format. Must update this when changing the fields in class.
    def __json__(self):
        return {'id': self.id,
                'deck_id': self.deck_id,
                'front': self.front,
                'back': self.back,
                'box': self._box,
                'ignored': self.ignored}