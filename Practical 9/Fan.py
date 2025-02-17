class Fan:
    SLOW, MEDIUM, FAST = 1, 2, 3
    
    def __init__(self, radius=5, colour='White', on=False, speed=SLOW):
        self.radius = radius
        self.colour = colour
        self.on = on
        self.speed = speed

    def get_radius(self):
        return self.radius

    def get_colour(self):
        return self.colour
    
    def is_on(self):
        return self.on
    
    def get_speed(self):
        return self.speed
    
    def set_on(self, on):
        self.on = on
    
    def set_speed(self, speed):
        self.speed = speed