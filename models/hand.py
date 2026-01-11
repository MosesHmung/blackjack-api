
from models.card import Card
from models.deck import Deck

class Hand:
    # Represents a collection of cards held by a player or dealer
    def __init__(self):
        self.cards = []  # list of Card objects

    # Adds a card to the hand
    def add_card(self, card):
        self.cards.append(card)

    # Calculates the Blackjack value of the hand (handles Aces as 1 or 11)
    def value(self):
        total = 0
        aces = 0

        # Add up values, counting Aces
        for card in self.cards:
            total += card.value()
            if card.rank == 'A':
                aces += 1

        # If total is over 21, convert Aces from 11 to 1 as needed
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        return total

    # Returns True if the hand value is over 21
    def is_bust(self):
        return self.value() > 21

    # Returns True if the hand is exactly 21 with 2 cards
    def is_blackjack(self):
        return self.value() == 21 and len(self.cards) == 2

    # Nice printing for the hand
    def __str__(self):
        return ", ".join(str(card) for card in self.cards)
