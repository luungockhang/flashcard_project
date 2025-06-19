# Will use when I get to English dictionary integration

class Word:
    def __init__(self, _id, word):
        self._id = _id              # Index in database, start at 1
        self.word = word            # This means the word itself
        self.definitions = []       # A word has many definitions

    # Add one definition
    def add_definition(self, definition):
        self.definitions.append(definition)

    # Add a list of definitions
    def add_definitions(self, definitions):
        self.definitions.extend(definitions)

    # Update definition
    def update_definition(self, index, definition):
        self.definitions[index] = definition

    # Clear definition
    def clear_definitions(self):
        self.definitions = []

# It's very unlikely for each word to have the same definition so no ID?
class Definition:
    def __init__(self,pos="",content=""):
        self.pos = pos
        self.content = content