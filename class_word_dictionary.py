import json


class Word:
    # Allows the text to be initialized with only the text itself
    def __init__(self,text,time_seen=0,ignored=False,meaning="<x>"):
        self.text = text
        self.ignored = ignored
        self.time_seen = time_seen
        self.meaning = meaning

    # Override print method
    def __repr__(self):
        return f"""{self.text}
- Meaning: {self.meaning}
- Ignored: {self.ignored}
- Time seen: {self.time_seen}
"""
    
    # Return a dict (json-convertable object) of the class for dumping to json
    def __json__(self):
        return {'text': self.text,
                'meaning': self.meaning,
                'timeSeen': self.time_seen,
                'ignored': self.ignored}