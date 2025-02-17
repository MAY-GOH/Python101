from Triangle import *
from MyInputReaders import *

def read_sides():    
    print("Enter the 3 sides of a triangle.")
    return read_floats(prompt="Enter a side: ", minimum=0.1, loop=3)

def read_colour():
    return read_string(prompt="\nEnter a colour: ")

def read_filled():
    while True:
        print("Is the triangle filled? Yes (y) or No (n)?")
        value = read_string(prompt="Enter either y (Yes) or n (No): ")
        if value.lower() == 'y':
            return True
        elif value.lower() == 'n':
            return False
        else:
            print("Error: Wrong input!\n")  

def read_inputs():
    sides = read_sides()
    sides.append(read_colour())
    sides.append(read_filled())
    
    return sides

def main():
    side1, side2, side3, colour, filled = read_inputs()
    triangle = Triangle(side1=side1, side2=side2, side3=side3, colour=colour, filled=str(filled))
    print("\nTriangle")
    print(triangle, end=", ")
    print("area: {:.2f}, perimeter: {:.2f}\n".format(triangle.get_area(), triangle.get_perimeter()))