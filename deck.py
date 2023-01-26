import random
from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        for suit in range(4):
            for card in range(1, 14):
                new_card = Card(suit, card)
                self.cards.append(new_card)