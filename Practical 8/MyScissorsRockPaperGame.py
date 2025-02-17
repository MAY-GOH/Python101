import random

# Initialize the number win, lose and draw as 0
user_win = 0
user_lose = 0
draw = 0

# Initialize the counter to be used as a stopper as 0
counter = 0

# Generate 0, 1, or 2 randomly represents "scissors", "rock", and "paper" respectively
def generate_answer():
    return random.randint(0, 2) 

# Return a guess from user input, where typo is allowed as long as the first 2 letters are correct
def read_input():
    while True:
        choice = input("Enter your choice (scissor/rock/paper): ").strip().lower()
        if choice[:2] == "sc" or choice[:2] == "ro" or choice[:2] == "pa":
            match choice[:2]:
                case "sc":
                    return 0
                case "ro": 
                    return 1
                case "pa":
                    return 2
            break
        else:
            print("Wrong input...")
            
# Calculate the number of wins, losses and draws
def win_draw_or_lose(choice, answer):
    global draw
    global user_win
    global user_lose
    
    if choice == answer:
        print("Draw!")
        draw += 1
    elif (choice == 0 and answer == 2) or (choice == 1 and answer == 0) or (choice == 2 and answer == 1):
        print("You win!")
        user_win += 1 
    else:
        print("You lose!")
        user_lose += 1

# Print computer's choice where 0, 1, or 2 randomly represents "scissors", "rock", and "paper" respectively
def print_computer_choice(answer):
    match answer:
        case 0:
            print("Computer's choice: Scissors")
        case 1: 
            print("Computer's choice: Rock")
        case 2:
            print("Computer's choice: Paper")

# Print the details of the gameplay
def print_summary():
    global counter 
    if (counter > 2) and (user_win != user_lose):
        print("\nYou won", user_win, "times" if user_win > 1 else "time", end=" ")
        print("and computer won", user_lose, "times." if user_lose > 1 else  "time.")
        if user_win > user_lose:
            print("You are the final winner!")
        else:
            print("Computer is the final winner!")
        return True

# Keep track of the gameplay
def counter_increment():
    global counter 
    counter += 1

# Simulate the scissors rock paper game 
def scissors_rock_paper_game():
    while True:
        answer = generate_answer()
        choice = read_input()
        print_computer_choice(answer)
        win_draw_or_lose(choice, answer)
        counter_increment()
        end = print_summary()
        if end:
            break