def read_integer(prompt="Enter an integer: ", error="Error: Wrong input!\n", minimum=-(10**10), maximum=10**10):
    """
    Purpose:
        Reads an integer from user input.
    
    Parameters:
        prompt (str) : The prompt message, defaulting to 'Enter an integer: '
        error (str)  : The error message, defaulting to 'Error: Wrong input!'
        minimum (int): The lower bound of user input, defaulting to -(10**10).
        maximum (int): The upper bound of user input, defaulting to 10**10.
        
    Returns:
        int: The integer entered by the user.
    """
    while True:
        number = input(prompt)
        try:
            number = int(number)
            if number >= minimum and number <= maximum:
                return number
            else:
                print(error)
        except ValueError:
            print("Error: Only integers are allowed!\n")

# Reads a floating-point number from user input.
def read_float(prompt="Enter a number: ", error="Error: Wrong input!\n", minimum=float('-inf'), maximum=float('inf')):
    """
    Purpose:
        Reads a floating-point number from user input, defaulting to a positive value.
    
    Parameters:
        prompt (str)   : The prompt message, defaulting to 'Enter a number: '
        error (str)    : The error message, defaulting to 'Error: Wrong input!'
        minimum (float): The lower bound of user input, defaulting to float('-inf').
        maximum (int)  : The upper bound of user input, defaulting to float('inf').
        
    Returns:
        int: The floating-point number entered by the user.
    """
    while True:
        try:
            number = float(input(prompt))
            if number >= minimum and number <= maximum:
                return number
            else:
                print(error)
        except ValueError:
            print("Error: Only floating-point numbers are allowed!\n")

# Return a series of integers read from the user.
def read_integers(prompt="Enter an integer: ", error="Error: Wrong input!\n", minimum=-(10**10), maximum=10**10, stop='q', loop=10**10):
    """
    Purpose:
        Reads a series of integers from user input.
    
    Parameters:
        prompt (str) : The prompt message, defaulting to 'Enter an integer: '
        error (str)  : The error message, defaulting to 'Error: Wrong input!'
        minimum (int): The lower bound of user input, defaulting to -(10**10).
        maximum (int): The upper bound of user input, defaulting to 10**10.
        stop (str)   : The stopping condition indicated by a letter.
        loop (int)   : The 'loop' number of iteration to be excuted to read 'loop' number of input values.
        
    Returns:
        list: A series of integers entered by the user.
    """
    integers = []  
    count = 0
    stop = str(stop)
    
    while True:
        integer = input(prompt)
        if integer.lower() == stop.lower():
            return integers
        try: 
            integer = int(integer) 
            if integer >= minimum and integer <= maximum:
                integers.append(integer)
                count += 1
                if count == loop:
                    return integers
            else:
                print(error)
        except ValueError:
            print("Error: Only integers are allowed!\n") 

# Return a series of floating-point numbers read from the user.
def read_floats(prompt="Enter a number: ", error="Error: Wrong input!\n", minimum=float('-inf'), maximum=float('inf'), 
                stop='q', loop=10**10):
    """
    Purpose:
        Reads a series of floating-point numbers from user input.
    
    Parameters:
        prompt (str) : The prompt message, defaulting to 'Enter a number: '
        error (str)  : The error message, defaulting to 'Error: Wrong input!'
        minimum (int): The lower bound of user input, defaulting to float('-inf').
        maximum (int): The upper bound of user input, defaulting to float('inf').
        stop (str)   : The stopping condition indicated by a letter.
        loop (int)   : The 'loop' number of iteration to be excuted to read 'loop' number of input values.
        
    Returns:
        list: A series of floating-point numbers entered by the user.
    """
    floats = []  
    count = 0
        
    while True:
        number = input(prompt)
        if number.lower() == stop.lower():
            return floats
        try: 
            number = float(number) 
            if number >= minimum and number <= maximum:
                floats.append(number)
                count += 1
                if count == loop:
                    return floats
            else:
                print(error)
        except ValueError:
            print("Error: Only floating-point numbers are allowed!\n") 
            
# Reads a string from user input.
def read_string(prompt="Enter a string: "):
    return input(prompt).strip()
