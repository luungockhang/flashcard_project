from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
import const

app = Flask(__name__)
app.config['TESTING'] = True

data = {}

with open(const.DEFAULT_PATH, 'r') as f:
    data = json.load(f)

# Simple in-memory storage (in production, use a database)
flashcard_dict = data['decks'][0]['flashcards']
flashcards = []
# convert the dict to list
for card in flashcard_dict:
    flashcards.append(flashcard_dict[card])

# {
#     {"id": 1, "front": "What is the capital of France?", "back": "Paris"},
#     {"id": 2, "front": "What is 2 + 2?", "back": "4"},
#     {"id": 3, "front": "Who wrote Romeo and Juliet?", "back": "William Shakespeare"},
#     {"id": 4, "front": "What is the largest planet in our solar system?", "back": "Jupiter"},
# }

@app.route('/')
def index():
    return render_template('index.html', flashcards=flashcards)

@app.route('/api/cards')
def get_cards():
    return jsonify(flashcards)

@app.route('/api/cards', methods=['POST'])
def add_card():
    data = request.get_json()
    new_id = max([card['id'] for card in flashcards]) + 1 if flashcards else 1
    new_card = {
        'id': new_id,
        'front': data['front'].strip(),
        'back': data['back'].strip()
    }
    flashcards.append(new_card)
    return jsonify(new_card), 201

@app.route('/api/cards/<int:card_id>', methods=['DELETE'])
def delete_card(card_id):
    global flashcards
    flashcards = [card for card in flashcards if card['id'] != card_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
