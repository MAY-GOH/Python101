class GeometricObject:
    def __init__(self, colour, filled):
        self.colour = colour
        self.filled = filled
    
    def get_colour(self):
        return self.colour
    
    def get_filled(self):
        return self.filled
    
    def set_colour(self, colour):
        self.colour = colour
        
    def set_filled(self, filled):
        self.filled = filled
    
    def __str__(self):
        return "colour: {:s}, filled: {:s}".format(self.colour, str(self.filled))