# Read the first 9 digits of an ISBN-10 number from user input.
def read_input():
    while True:
        number = input("Enter the first 9 digits of an ISBN-10: ").strip()
        if number.isdigit() and len(number) == 9:
            return int(number)
        else:
            print("Error: Only positive 9-digits integer are allowed!\n")

# Return the checksum of 9 digits of the ISBN-10 number.
def calculate_checksum(number):
    checksum = 0
    counter = 9

    while counter != 0:
        checksum += ((number % 10) * counter)
        counter -= 1
        number = number // 10
        
    return checksum % 11

# Print the complete ISBN-10 number.
def print_isbn10(number, checksum):
    print("The ISBN-10 number is", str(number) + (str(checksum) if checksum < 10 else "X"))