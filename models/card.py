

class Card:
    # Initialize cards
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def value(self):
        if self.rank in ['J', 'Q', 'K']: # Face cards are 10
            return 10
        if self.rank == 'A': # Defaults Ace to 11 (DON'T FORGET OPTION TO CHANGE TO 1 IN HAND)
            return 11
        return int(self.rank) # Number Cards as is

#Returning cards in string readable
    def __str__(self):
        return self.rank + " of " + self.suit