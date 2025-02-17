# Return the number of words in the input_string.
def count_words(input_string):
    return len(input_string.split())

# Return the number of vowels in the input_string.
def count_vowels(input_string):    
    return len([character for character in input_string if character.lower() in ['a', 'e', 'i', 'o', 'u']])   

# Return the number of vowel 'a', 'e', 'i', 'o' and 'u' separately.
def count_vowel_aeiou(input_string):
    input_string = input_string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    a = input_string.count("a") 
    e = input_string.count("e") 
    i = input_string.count("i")
    o = input_string.count("o")
    u = input_string.count("u")    
    frequency = [a, e, i, o, u]
    
    return dict(zip(vowels, frequency))

# Return the average of word length in the input_string.
def calculate_average_word_length(input_string):
    total = 0
    for token in input_string.split():
        total += len(token)
    return (total / len(input_string.split()))