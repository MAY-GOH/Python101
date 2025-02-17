from GeometricObject import *
import math

class Triangle(GeometricObject):
    def __init__(self, colour='white', filled=False, side1=1.0, side2=1.0, side3=1.0):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        super().__init__(colour, filled)

    def get_side1(self):
        return self.side1
    
    def get_side2(self):
        return self.side2
    
    def get_side3(self):
        return self.side3
    
    def set_side1(self, side):
        self.side1 = side
    
    def set_side2(self, side):
        self.side2 = side
    
    def set_side3(self, side):
        self.side3 = side
        
    def get_area(self):
        semi_p = self.get_perimeter() / 2
        return math.sqrt(semi_p * (semi_p - self.side1) * (semi_p - self.side2) * (semi_p - self.side3))
    
    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def __str__(self):
        return super().__str__() + ", side1: {:.2f}, side2: {:.2f}, side3: {:.2f}".format(self.side1, self.side2, self.side3)