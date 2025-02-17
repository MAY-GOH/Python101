from Circle import *
import math

class Sphere(Circle):
    PI = math.pi
    
    def __init__(self, colour='white', filled=False, radius=1.0):
        super().__init__(colour, filled, radius)
        
    def get_surface_area(self):
        return 4 * super().get_area()
    
    def get_volume(self):
        return 4 / 3 * Sphere.PI * pow(self.radius, 3)
    
    def __str__(self):
        return super().__str__()