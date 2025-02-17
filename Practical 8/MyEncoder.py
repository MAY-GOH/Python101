from MyInputReaders import *
import string

items_1 = ""
items_2 = ""
size = 0

def define_letters():
    global items_1
    global items_2
    global size
    
    items_1 = string.ascii_letters + string.digits + " " + string.punctuation
    items_2 = items_1[::-1]
    size = len(items_1)

def print_menu():
    print("1. Encoding\n2. Decoding\n3. Exit")

def select_operation():
    while True:
        choice = read_integer("Enter an option (1, 2 or 3): ")
        if choice == 1 or choice == 2 or choice == 3:
            return choice
        else:
            print("Only 1, 2 ans 3 are acceptable!")
    
def encoder_simulator():
    define_letters()
    
    while True:
        print_menu()
        operation = select_operation()
        
        match operation:
            case 1:
                print("\n--------------------Encoding--------------------")
                text = read_string("Enter a message to be encoded: ")
                key = read_integer("Enter a key: ")
                code = encoding(text, key)
                print_output(operation, code)
            case 2:
                print("\n--------------------Decoding--------------------")
                text = read_string("Enter a message to be decoded: ")
                key = read_integer("Enter a key: ")
                decode = decoding(text, key)
                print_output(operation, decode)
            case 3:
                print("\nThank you! See you again!")
                break
    
def encoding(text, key):
    global items_1
    global size
    
    char_list = list(text)
    code = ""
    
    for char in char_list:
        position = items_1.index(char)
        new_position = position + key
        new_position = new_position % size
        code += items_1[new_position]
    
    return code

def decoding(text, key):
    global items_2
    global size
    
    char_list = list(text)
    decode = ""
    
    for char in char_list:
        position = items_2.index(char)
        new_position = position + key
        new_position = new_position % size
        decode += items_2[new_position] 
        
    return decode
    
def print_output(operation, text):
    print("The {} message is '{}'\n".format("encoded" if operation == 1 else "decoded", text))