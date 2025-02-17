from Sphere import *
from MyInputReaders import *

def read_inputs():    
    print("Enter the radius of 2 spheres.")
    return read_floats(prompt="Enter a radius: ", minimum=0.1, loop=2)

def main():
    radius1, radius2, = read_inputs()
    sphere1 = Sphere(radius=radius1)
    sphere2 = Sphere(radius=radius2)
    spheres = [sphere1, sphere2]
    
    for i in range(len(spheres)):
        print("\n{:s} {:d}".format("Sphere", i + 1))
        print("radius: {:.2f}, surface area: {:.2f}, volume: {:.2f}".format(spheres[i].get_radius(), 
                                                                            spheres[i].get_surface_area(), 
                                                                            spheres[i].get_volume()))