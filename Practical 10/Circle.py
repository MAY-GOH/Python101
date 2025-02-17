from GeometricObject import *
import math

class Circle(GeometricObject):
    PI = math.pi
    
    def __init__(self, colour='white', filled=False, radius=1.0):
        self.radius = radius
        super().__init__(colour, filled)

    def get_radius(self):
        return self.radius
    
    def set_radius(self, radius):
        self.radius = radius
        
    def get_area(self):
        return Circle.PI * pow(self.radius, 2)
    
    def get_perimeter(self):
        return 2 * Circle.PI * self.radius
    
    def __str__(self):
        return super().__str__() + ", radius: {:.2f}".format(self.radius)