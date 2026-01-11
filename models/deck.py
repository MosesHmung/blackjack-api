import random
from models.card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.cards = []

        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        # Create one card for each rank-suit combination
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

        self.shuffle()

    # Randomly shuffles the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Removes and returns the top card from the deck
    def draw(self):
        return self.cards.pop()






