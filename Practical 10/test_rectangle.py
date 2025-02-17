from Rectangle import *

def main():
    rectangle1 = Rectangle(colour="red", filled=False, width=4, height=40)
    rectangle2 = Rectangle(colour="yellow", filled=True, width=3.5, height=35.7)
    rectangles = [rectangle1, rectangle2]
    
    for i in range(len(rectangles)):
        print("{:s} {:d}".format("Rectangle", i + 1))
        print(rectangles[i], "\n")