import random

class Card:   
    def __init__(self, suit='♠', value='A'):        
        self.suit = suit
        self.value = value
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.value
     
    def get_suit_value(self):
        return (self.get_suit(), self.get_value())
        
    def set_suit(self, suit):
        self.suit = suit
    
    def set_value(self, value):
        self.value = value
        
    def random_pick(self):
        suits = ['♠', '♥', '♣', '♦']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        
        self.set_suit(random.sample(suits, 1)[0])
        self.set_value(random.sample(values, 1)[0])