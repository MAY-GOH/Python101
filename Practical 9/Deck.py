import random
from Card import *

class Deck:    
    def __init__(self):  
        self.cards = []
        suits = ['♠', '♥', '♣', '♦']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards.append(card)

    def get_cards(self):
        return self.cards
            
    def get_card(self, card=Card()):
        return card.get_suit_value()
    
    def shuffle_deck(self):
        random.shuffle(self.cards)