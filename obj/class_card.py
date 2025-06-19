import datetime

# Card class - There will be different card types but it's not implemented now.
class Card:
    # Allows the text to be initialized with only the text itself
    def __init__(self,front, card_id=0, deck_id=0,ignored=False,back="<x>", box=1):
        self.card_id = card_id
        self.deck_id = deck_id          # ID for tying a card to one deck. In case there are two words in different decks.
        self.front = front              # The word string that is the front of this card, also the key of this card.
        self.ignored = ignored          # If the user decides not to review this, it is True.
        self.back = back                # The "back" of this card, which usually has the definition of the word.
        self._date_reviewed = datetime.datetime.now()
        self._box = 0                   # The "box" to put this card in, for spaced repetition simulation of flashcard usage. 0 means user never saw this one before
        self._issues = ""               # Error logger - string
        self.time_seen = 0

    # Override print method
    def __repr__(self):
        return f"""{self.front}
- Back: {self.back}
- Ignored: {self.ignored}
- Time seen: {self.time_seen}
"""
    
    # Json export format. Must update this when changing the fields in class.
    def __json__(self):
        return {'id': self.card_id,
                'deck_id': self.deck_id,
                'front': self.front,
                'back': self.back,
                'box': self._box,
                'ignored': self.ignored,
                'issues': self._issues,
                'time_seen': self.time_seen}