import random

answers = []
guesses = []
results = []

# Return a random number to simulate heads and tails.
def generate_random_number():
    return random.randint(1, 2) 

# Return a guess as a number from user input.
def read_guess():
    while True:
        number = input("Enter 1 for a head, 2 for a tail, or 0 to exit: ")
        if number.isdigit():
            number = int(number)
            if number >= 0 and number <= 2:
                return number
            else:
                print("Error: Only 0, 1 and 2 are allowed!\n")
        else:
            print("Error: Only 0, 1 and 2 are allowed!\n")

# Return True to indicate a correct guess, otherwise, return False.
def win_or_lose(answer, guess):
    if answer == guess:
        print("Correct!")
        return True
    else:
        print("Wrong!")
        return False

# Record the details of a single game round.
def record_game(answer, guess, result):
    answers.append(answer)
    guesses.append(guess)
    results.append(result)
         
# Return the total number of correct guesses.
def count_correct():
    return len([result for result in results if result])

# Return the total number of incorrect guesses.           
def count_incorrect():
    return len([result for result in results if not result])
        
# Print the details of all game rounds
def print_records():
    print("RESULTS")
    print("-------")
    print("You have made {:d} correct guess{:s} ".format(count_correct(), "es" if count_correct() > 1 else ""), end="")
    print("and {:d} incorrect guess{:s}.\n".format(count_incorrect(), "es" if count_incorrect() > 1 else ""))
    
    for i in range(len(answers)):
        print("Round #{:d}".format(i + 1))
        print(" Answer: {:s}".format("Head" if answers[i] == 1 else "Tail"))
        print(" Guess : {:s}".format("Head" if guesses[i] == 1 else "Tail"))
        print(" Result: {:s}".format("Correct" if results[i] else "Wrong"))
        print()
        
# Simulate the gameplay of a coin flipping game
def flip_coin_game():
    while True:
        answer = generate_random_number()
        guess = read_guess()
        if guess == 0:
            break
        else:
            result = win_or_lose(answer, guess)
            record_game(answer, guess, result)
            
    print("\nThank you for playing coin-flipping game!\n") 
    print_records()