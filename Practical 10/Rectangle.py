from GeometricObject import *

class Rectangle(GeometricObject):
    def __init__(self, colour='white', filled=False, width=1, height=2):
        self.width = width
        self.height = height
        super().__init__(colour, filled)

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return super().__str__() + ", width: {:.2f}, height: {:.2f}".format(self.width, self.height)