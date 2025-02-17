from LoadedDie import *
from MyInputReaders import *
    
class DiceRollingGame:
    QUANTITY = 5
    
    def __init__(self):
        self.simulation()

    def read_mode(self):
        prompt = "Enter a mode (1: Easy 2: Medium 3: Hard): "
        return read_integer(prompt=prompt, minimum=1, maximum=3)

    def conclusion(self, human_total, computer_total):
        print("\nThe sum of your {:d} dice is {:d}.".format(DiceRollingGame.QUANTITY, human_total))
        print("The sum of computer's {:d} dice is {:d}.".format(DiceRollingGame.QUANTITY, computer_total))
        
        if human_total > computer_total:
            print("You win!")
        elif human_total == computer_total:
            print("Draw!")
        else:
            print("Computer wins!")
            
    def humans_turn(self, human_dice):
        human_total = 0
        print("\n{:8s}: ".format("Human"), end="")
        for i in range(len(human_dice)):
            human_dice[i].roll()
            human_total += human_dice[i].get_value()
            print(human_dice[i].get_value(), end=" ")
        print("\n{:8s}: {:d}".format("Total", human_total))
        
        return human_total
            
    def computers_turn(self, computer_dice):
        computer_total = 0
        print("{:8s}: ".format("\nComputer"), end="")
        for i in range(len(computer_dice)):    
            computer_dice[i].roll()
            computer_total += computer_dice[i].get_value()
            print(computer_dice[i].get_value(), end=" ")
        print("\n{:8s}: {:d}".format("Total", computer_total))
        
        return computer_total
    
    def setup(self, mode):
        match mode:
            case 1:
                human_die = LoadedDie()
                computer_die = Die()
            case 2:
                human_die = Die()
                computer_die = Die()
            case 3:
                human_die = Die()
                computer_die = LoadedDie()
                
        return (human_die, computer_die)
    
    def next_round(self):
        return read_string("\nPlease enter 'y' to continue or any key to exit: ").strip()
    
    def print_divider(self):
        print()
        print('-' * pow(DiceRollingGame.QUANTITY, 3)) 
        print()
    
    def simulation(self):
        while True:
            mode = self.read_mode()
            human_die, computer_die = self.setup(mode)

            human_dice = [human_die] * DiceRollingGame.QUANTITY
            computer_dice = [computer_die] * DiceRollingGame.QUANTITY

            human_total = self.humans_turn(human_dice)
            computer_total = self.computers_turn(computer_dice)
            self.conclusion(human_total, computer_total)

            response = self.next_round().lower()
            if response == 'y':
                self.print_divider()
                continue
            else:
                print("\nGood bye!")
                break