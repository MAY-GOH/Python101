from MyRectangle import *

def read_filename():
    prompt = "A filename consists of a name and its extension (e.g., document.txt)\nEnter a filename: "
    return input(prompt).strip()

def is_header(row):
    # Basic checks for header characteristics
    # Modify this function based on your specific header criteria
    # Here we check if the row contains only strings (assuming headers are non-numeric)
    return all(cell.isalpha() or cell.isspace() for cell in row.split())

def open_file(filename, mode):
    return open(filename, mode)

def read_file(file):
    return [line.strip() for line in file.readlines() if not is_header(line)]

def print_rectangle(width, height):
    print("{:10s}: {:.2f}".format("Width", width))
    print("{:10s}: {:.2f}".format("Height", height))
    print("{:10s}: {:.2f}".format("Area", get_area(width, height)))
    print("{:10s}: {:.2f}".format("Perimeter", get_perimeter(width, height)))
    
def process_rectangles(contents):
    for i in range(len(contents)):
        width, height = contents[i].strip().split()

        try:
            width = float(width)
            height = float(height)
        except ValueError:
            print("\nError: Invalid width or height values!")
        else:
            print("\n{:s} {:d}".format("Rectangle", i + 1))
            print_rectangle(width, height)
    
def main():
    try:
        file = open_file(read_filename(), 'r')
    except:
        print("\nError: Something went wrong while opening the file!")
    else:
        try: 
            contents = read_file(file)
        except IOError:
            print("\nError: Something went wrong while reading the file!")
        else:
            if len(contents) == 0:
                print("\nError: The file is empty!")
            else:
                process_rectangles(contents)
        finally:
            file.close()

main()
