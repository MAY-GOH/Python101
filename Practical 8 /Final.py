from MyInputReaders import *
from MyStringProcessor import *

def main():
    # Read a string from user input
    text = read_string("Enter a string: ")

    # Print the number of words
    print("\nNo. of words:", count_words(text))

    # Print the average word length
    print("Average word length: {:.2f}\n".format(calculate_average_word_length(text)))

    # Print the number of each of the vowels separately
    for vowel, frequency in count_vowel_aeiou(text).items():
        print("No. of {}: {:d}".format(vowel, frequency))

main()
