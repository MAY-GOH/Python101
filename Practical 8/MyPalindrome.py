# Remove irrelevant contents from the input_string.
def remove_noise(input_string):
    return "".join([letter if letter.isalpha() else "" for letter in input_string])
    
# Convert all elements in the input_string to a consistent case.
def normalize_case(input_string):
    return input_string.lower()

# Return true if the input_string is a palindrome.
def is_palindrome(input_string):
    input_string = normalize_case(remove_noise(input_string))
    
    return input_string == input_string[::-1]