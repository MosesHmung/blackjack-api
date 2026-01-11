from models.deck import Deck
from models.hand import Hand

class Game:
    # Controls one round of Blackjack as a state machine (actions change state)
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.is_over = False
        self.result = None  # "player", "dealer", "tie" (or None)

    def start_round(self):
        # Reset everything for a new round
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.is_over = False
        self.result = None

        # Deal 2 cards each
        self.player_hand.add_card(self.deck.draw())
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())

        if self.player_hand.is_blackjack() and self.dealer_hand.is_blackjack():
            self.is_over = True
            self.result = "tie"
        elif self.player_hand.is_blackjack():
            self.is_over = True
            self.result = "player"
        elif self.dealer_hand.is_blackjack():
            self.is_over = True
            self.result = "dealer"
    def player_hit(self):
        # Player requests a hit (one action)
        if self.is_over:
            return

        self.player_hand.add_card(self.deck.draw())
        if self.player_hand.is_bust():
            self.is_over = True
            self.result = "dealer"

    def player_stand(self):
        # Player stands; dealer plays out and we decide winner
        if self.is_over:
            return

        # Dealer hits until 17+
        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.draw())

        # Decide outcome
        self.is_over = True
        self.result = self._determine_winner()

    def _determine_winner(self):
        if self.dealer_hand.is_bust():
            return "player"

        pv = self.player_hand.value()
        dv = self.dealer_hand.value()

        if pv > dv:
            return "player"
        elif pv < dv:
            return "dealer"
        else:
            return "tie"

    def get_public_state(self):
        # What you can show mid-round (hide dealer 2nd card)
        return {
            "player_cards": [str(c) for c in self.player_hand.cards],
            "player_value": self.player_hand.value(),
            "dealer_cards": [str(self.dealer_hand.cards[0]), "[Hidden]"] if len(self.dealer_hand.cards) >= 2 else [],
            "dealer_value": None,  # hidden until game over
            "is_over": self.is_over,
            "result": self.result
        }

    def get_full_state(self):
        # What you can show when round ends
        return {
            "player_cards": [str(c) for c in self.player_hand.cards],
            "player_value": self.player_hand.value(),
            "dealer_cards": [str(c) for c in self.dealer_hand.cards],
            "dealer_value": self.dealer_hand.value(),
            "is_over": self.is_over,
            "result": self.result
        }