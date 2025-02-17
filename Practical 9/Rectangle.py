class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return "Width: {:.2f}, Height: {:.2f}, Area: {:.2f}, Perimeter: {:.2f}".format(self.width, 
                                                                                       self.height, self.get_area(), self.get_perimeter)