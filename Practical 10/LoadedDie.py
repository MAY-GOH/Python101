from Die import *
import random

class LoadedDie(Die):
    def __init__(self, value=1):
        super().__init__(value)
        
    def roll(self):
        self.value = random.randint(2, 6)