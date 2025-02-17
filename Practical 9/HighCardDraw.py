from Deck import *

class HighCardDraw:
    def __init__(self):
        self.deck = Deck()
        self.player_win = 0
        self.computer_win = 0
        
    def display_rules(self):
        print("Rule: Each round, shuffle the deck, then a card will be randomly selected for you and the computer player.")
        
    def get_card(self, card):
        return "{:s}{:s}".format(card.get_suit(), card.get_value())
        
    def interpret_value(self, value):
        match value:
            case 'A':
                return 1
            case 'J':
                return 11
            case 'Q':
                return 12
            case 'K':
                return 13
            case _:
                return int(value)
        
    def interpret_suit(self, suit):
        match suit:
            case '♠':
                return 4
            case '♥':
                return 3
            case '♣':
                return 2
            case '♦':
                return 1
        
    def compare_cards(self, player_card, computer_card):        
        if self.interpret_value(player_card[1]) > self.interpret_value(computer_card[1]):
            self.player_win += 1
            return True
        elif self.interpret_value(player_card[1]) == self.interpret_value(computer_card[1]) and \
            self.interpret_suit(player_card[0]) > self.interpret_suit(computer_card[0]):
            self.player_win += 1
            return True
        else:
            self.computer_win += 1
            return False
        
    def gameplay(self):
        self.deck.shuffle_deck()
        cards = self.deck.get_cards()[:2]
        
        player_card = self.get_card(cards[0])
        computer_card = self.get_card(cards[1])
        print("{:15s}: {:s}".format("Your card", player_card))
        print("{:15s}: {:s}".format("Computer's card", computer_card))
       
        result = self.compare_cards(player_card, computer_card)
        print("{:15s}: {:s}".format("Higher card?", "You" if result else "Computer"))   
        
    def conclusion(self):
        print("\nYou drew higher cards {:d} {:s}.".format(self.player_win, "times" if self.player_win > 1 else "time"))
        print("Computer drew higher cards {:d} {:s}.".format(self.computer_win, "times" if self.computer_win > 1 else "time"))
        print("{:s}".format("You win!" if self.player_win > self.computer_win else "Computer wins!"))
        
    def simulation(self):
        computer_wins = 0
        human_wins = 0
        
        self.display_rules()
        for i in range(5):
            while True:
                key = input("\nPress 's' to shuffle the deck: ")
                if key.lower() == 's':
                    print("\nRound {:d}".format(i + 1))
                    self.gameplay()
                    break
                else:
                    print("Error: Invalid input!")
        self.conclusion()