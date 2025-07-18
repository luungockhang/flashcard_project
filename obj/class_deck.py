import const
from .class_card import Card
import json
import http
import datetime
from json import JSONEncoder



# Global helper functions
def is_alpha_word(word):
    for char in word:
        if not char.isalpha():
            return False
    return True

# Deck class - Saves the dict of a flashcard deck.
# Contains: ID for database index, User-defined title, date of update/creation.  
class Deck:
    def __init__(self, title="", id=0, flashcards={}):
        self._id = id               # ID for indexing
        self.title = title          # Title of this deck
        self.date = datetime.datetime.now()            # Date updated
        self.flashcards = {}        # The deck content
        # When binding user, there needs to be a user_id here also.

    ### Creation methods ###
    # Import flashcards from a passage of text. Title and text must be filled.
    # Note: Remove Text?
    def import_from_text(self, title="", text="", url=""):
        if url != "":
            # Logic for text parsing from API etc. Not implemented.
            # In which case the text is parsed from the url and assigned here.
            # Title could also be assigned here if the API logic is smart enough (?)
            pass

        # Raise an error if missing text or title
        if text == "" or title == "":
            raise Exception("Missing title or content.") # Handle this with str(e) with e being Exception literal
        
        self.title = title
        # Reinit could be redundant here.
        words = map(lambda word: word.strip(const.SPECIAL_CHARACTERS),
                    text.lower().split())   # -> list of words
        count = 0
        for word in words:
            if not is_alpha_word(word):
                continue
            if word not in self.flashcards.keys():
                self.flashcards[word] = Card(word, card_id=count,deck_id=self._id)
                count += 1

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
        with open(const.DEFAULT_PATH, 'w') as fp:
            json.dump(self, fp, default=lambda x: x.__json__() if hasattr(x, '__json__') else None)
    
    def __repr__(self):
        return f"--- Deck info ---\nTitle: {self.title}\nCards:{self.flashcards}"

    # Json export format. Must update this when changing the fields in class.
    # Check if it can save
    def __json__(self):
        return {'id': self._id,
                'title': self.title,
                'date': str(self.date),
                'flashcards': self.flashcards}

