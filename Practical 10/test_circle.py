from Circle import *

def main():
    circle1 = Circle(radius=4.5)
    circle2 = Circle(radius=7.7)
    circles = [circle1, circle2]
    
    for i in range(len(circles)):
        print("{:s} {:d}".format("Circle", i + 1))
        print(circles[i], end=", ")
        print("area: {:.2f}, perimeter: {:.2f}\n".format(circles[i].get_area(), circles[i].get_perimeter()))