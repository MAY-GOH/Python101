# Question 1
while True:
    # Prompt the user to enter a score
    score = input("Enter a score or 'Q'/'q' to exit: ")

    if score == 'Q' or score == 'q':
        break
        
    try:
        score = float(score)
        
    except ValueError:
        print("Only number is allowed!")
        
    else:
        if not (score >=0 and score <=100):
            print("Only 0 ≤ number ≤ 100 inclusive are allowed!\n")
        else:
            # Determine the grade based on the score
            if score >= 90 and score <= 100:
                grade = 'A'
            elif score >= 80 and score < 90:
                grade = 'B'
            elif score >= 70 and score < 80:
                grade = 'C'
            elif score >= 60 and score < 70:
                grade = 'D'
            elif score >= 0 and score < 60:
                grade = 'F'
            else:
                grade = ''

            # Print an output for the grade determined
            match grade:
                case 'A' | 'F':
                    print("You got an", grade, "for the test!")
                case 'B' | 'C' | 'D':
                    print("You got a", grade, "for the test!")
                case _: 
                    print("You have entered a wrong input!")

print("Thank you!")

# Question 2
while True:
    # Prompt the user to enter a score
    score = input("Enter a score or 'Q'/'q' to exit: ")

    if score == 'Q' or score == 'q':
        break
        
    elif not score.replace(".","").isnumeric():
      print("Only positive number is allowed")
        
    else:
        score = float(score)

        if not (score >=0 and score <=100):
            print("Only 0 ≤ number ≤ 100 inclusive are allowed!\n")
        else:
            # Determine the grade based on the score
            if score >= 90 and score <= 100:
                grade = 'A'
            elif score >= 80 and score < 90:
                grade = 'B'
            elif score >= 70 and score < 80:
                grade = 'C'
            elif score >= 60 and score < 70:
                grade = 'D'
            elif score >= 0 and score < 60:
                grade = 'F'
            else:
                grade = ''

            # Print an output for the grade determined
            match grade:
                case 'A' | 'F':
                    print("You got an", grade, "for the test!")
                case 'B' | 'C' | 'D':
                    print("You got a", grade, "for the test!")
                case _: 
                    print("You have entered a wrong input!")

print("Thank you!")

# Question 3
numbers = []

while True:
  number = input("Enter an integer or 'Q'/'q' to exit: ")

  if number == "Q" or number == "q":
    break

  try:
    numbers.append(int(number))

  except ValueError:
    print("Only integer in allowed!")

if len(numbers):
  numbers = numbers[::-1]

  print("\n Integers in reversed order:", end=" ")
  for num in numbers:
    print(num, end=" ")

else:
  print("No integers")

# Question 4

import random

answers = []
guesses = []
outputs = []

while True:
    answer = random.randint(1, 2)

    guess = input("Enter your guess as 1 for a head, 2 for a tail, or 0 to exit: ")

    if guess.isdigit():
        guess = int(guess)
        
        if not (guess >= 0 and guess <= 2):
            print("Please enter 0, 1, or 2.\n") 
        else:
            if guess == 0:
                print("Thank you for playing the game!\n")
                break
            else:
                answers.append(answer)
                guesses.append(guess)
                
                if answer == guess:
                    print("Correct!\n")
                    outputs.append(True)
                else:
                    print("Wrong!\n")
                    outputs.append(False)
    else:
        print("Please enter 0, 1, or 2.\n")

correct = [output for output in outputs if output]        
incorrect = [output for output in outputs if not output]  
    
print("RESULTS")
print("-------")
print("You have made {} correct guess{} ".format(len(correct), "es" if len(correct) > 1 else ""), end="")
print("and {} incorrect guess{}.\n".format(len(incorrect), "es" if len(incorrect) > 1 else ""))

for i in range(len(answers)):
    print("Round #{:d}".format(i + 1))
    print(" Answer: {:s}".format("Head" if answers[i] == 1 else "Tail"))
    print(" Guess : {:s}".format("Head" if guesses[i] == 1 else "Tail"))
    print(" Result: {:s}".format("Correct" if outputs[i] else "Wrong"))
    print()

# Question 5
scores = []

while True:     
    number = input("Enter the number of students: ")
    
    if number.isdigit():
        number = int(number)
        if number == 0:
            print("Only positive integer is allowed!\n")
            continue
        else:
            count = 1
            scores = []
            
            print("\nEnter the {:s}.".format("students' scores" if number > 1 else "student's score"))
            while count <= number:
                match (count % 10):
                    case 1:
                        suffix = "st"
                    case 2: 
                        suffix = "nd"
                    case 3:
                        suffix = "rd"
                    case _:
                        suffix = "th"
                message = "{:>3s}{} student: ".format(str(count), suffix)

                try:
                    score = float(input(message))  
                    if score < 0:
                        print("Only zero or positive value is allowed!\n")
                    else:
                        scores.append(score)
                        count += 1
                except ValueError:
                    print("Only number is allowed!\n")
                    
            if count > number:
                break         
    else:
        print("Only positive integer is allowed!\n")

scores.sort(reverse=True)

print("\nThe highest score       : {:.0f}%".format(scores[0]))
print("The second highest score: {:.2f}%".format(scores[1]))
print("The average score       : {:.2f}%".format(sum(scores) / len(scores)))

# Question 6
numbers = []
pos_count = 0
neg_count = 0

while True:
    try: 
        number = int(input("Enter a number: "))
        if number == 0:
            break
        else:
            numbers.append(number)
    except:
        print("Only integers are acceptable!")

for number in numbers:
    if number > 0:
        pos_count += 1
    else:
        neg_count += 1
        
print("\nNo. of positive numbers: {:d}".format(pos_count))
print("No. of negative numbers: {:d}".format(neg_count))
print("Sum of all numbers     : {:d}".format(sum(numbers)))
print("Average of all numbers : {:.2f}".format((sum(numbers)/len(numbers))))

# Question 7

while True:
  print("Enter a line of whitespace separated integers...")
  numbers = input("Integers: ")
  numbers = numbers.split()
  try:
    numbers = [int(number) for number in numbers]
    if len(numbers) > 0:
      break
    else:
      print("No input is provided!\n")

  except:
    print("Only integers are acceptable!\n")

numbers = set(numbers) #Take away duplicated value, if any
numbers = list(numbers)
numbers.sort()

print("Numbers (ascending order): ", end= "")
for number in numbers:
  print(number, end = " ")

# Question 8
import random

state_capital = {
    "Johor": "Johor Bahru", "Kedah": "Alor Setar", "Kelantan": "Kota Bharu",
    "Malacca": "Malacca City", "Negeri Sembilan": "Seremban",
    "Pahang": "Kuantan", "Penang": "George Town", "Perak": "Ipoh",
    "Perlis": "Kangar", "Sabah": "Kota Kinabalu", "Sarawak": "Kuching",
    "Selangor": "Shah Alam", "Terengganu": "Kuala Terengganu",
    "Kuala Lumpur": "Kuala Lumpur", "Labuan": "Victoria", "Putrajaya": "Putrajaya"
}

count = 0
keys = list(state_capital.keys())
random.shuffle(keys)

print("Identify the capital of following states:")
for i in range(len(keys)):
    string = "\nEnter the capital of {:16}: ".format(keys[i])    
    if input(string).lower() == state_capital[keys[i]].lower():
        print("Correct")
        count += 1
    else:
        print("Wrong")

print("\nYou answered {:d} {:s} correctly!".format(count, "questions" if count > 1 else "question"))

# Question 9
import random

digit_1 = random.randint(0, 9) 
digit_2 = random.randint(0, 9) 
digit_3 = random.randint(0, 9) 

print("Lottery number:", str(digit_1) + str(digit_2) + str(digit_3))
digits = [digit_1, digit_2, digit_3]

while True:
    try:
        guess = int(input("Enter a 3-digit integer: "))
    except:
        print("Only integers are acceptable!\n")
    else:
        if guess > 999:
            print("Only 3-digit integers are acceptable!\n")
        else:
            break

guess_3 = guess % 10
answer = guess // 10
guess_2 = answer % 10
guess_1 = answer // 10        
guesses = [guess_1, guess_2, guess_3]

if digits == guesses:
    print("Congratulations! You won RM10,000!")
elif digits != guesses and sorted(digits) == sorted(guesses):
    print("Congratulations! You win RM3,000!") 
elif len(set(digits) & set(guesses)) > 0: 
    print("Congratulations! You win RM1,000!") 
else:
    print("I regret to inform you that your ticket did not win a prize this time.") 

# Quesiton 10
# ♠ = Spades, ♥ = Hearts, ♣ = Clubs, ♦ = Diamonds
deck = {
    1: ('♠', 'A'), 2: ('♠', '2'), 3: ('♠', '3'), 4: ('♠', '4'), 
    5: ('♠', '5'), 6: ('♠', '6'), 7: ('♠', '7'), 8: ('♠', '8'), 
    9: ('♠', '9'), 10: ('♠', '10'), 11: ('♠', 'J'), 12: ('♠', 'Q'), 
    13: ('♠', 'K'), 14: ('♥', 'A'), 15: ('♥', '2'), 16: ('♥', '3'), 
    17: ('♥', '4'), 18: ('♥', '5'), 19: ('♥', '6'), 20: ('♥', '7'), 
    21: ('♥', '8'), 22: ('♥', '9'), 23: ('♥', '10'), 24: ('♥', 'J'), 
    25: ('♥', 'Q'), 26: ('♥', 'K'), 27: ('♣', 'A'), 28: ('♣', '2'), 
    29: ('♣', '3'), 30: ('♣', '4'), 31: ('♣', '5'), 32: ('♣', '6'), 
    33: ('♣', '7'), 34: ('♣', '8'), 35: ('♣', '9'), 36: ('♣', '10'), 
    37: ('♣', 'J'), 38: ('♣', 'Q'), 39: ('♣', 'K'), 40: ('♦', 'A'), 
    41: ('♦', '2'), 42: ('♦', '3'), 43: ('♦', '4'), 44: ('♦', '5'), 
    45: ('♦', '6'), 46: ('♦', '7'), 47: ('♦', '8'), 48: ('♦', '9'), 
    49: ('♦', '10'), 50: ('♦', 'J'), 51: ('♦', 'Q'), 52: ('♦', 'K')
}

numbers = random.sample(list(deck.keys()), 4)
total = 0

print("Cards: ", end="")
for i in range(len(numbers)):
    print(deck[numbers[i]][0] + deck[numbers[i]][1], end="\n" if i == len(numbers) - 1 else " and ")
    match deck[numbers[i]][1]:
        case 'A':
            total += 1
        case 'J':
            total += 11
        case 'Q':
            total += 12
        case 'K':
            total += 13
        case _:
            total += int(deck[numbers[i]][1])
print("Sum  :", total)

# Question 11
question_1 = "12 + 8 = ?\nA. 14\tB. 16\tC. 18\tD. 20"
question_2 = "15 - 7 = ?\nA. 6\tB. 7\tC. 8\tD. 9"
question_3 = "9 x 6 = ?\nA. 45\tB. 48\tC. 54\tD. 60"
question_4 = "12 + 8 = ?\nA. 14\tB. 16\tC. 18\tD. 20"

quizzes = {1: (question_1, 'D'), 2: (question_2, 'C'), 3: (question_3, 'C'), 4: (question_4, 'B')}
counter = 0

print("QUIZ")

for i in range(len(quizzes.keys())):
    print("-" * len(quizzes) * 10)
    print("Q" + str(i + 1) + ":", quizzes[i+1][0])
    
    while True:
        answer = input("Enter your answer (A or B or C or D): ")
        answer = answer.upper()
        if answer == 'A' or answer == 'B' or answer == 'C' or answer == 'D':
            break

    if answer == quizzes[i+1][1]:
        print("Correct!")
        counter += 1
    else:
        print("The correct answer is", quizzes[i+1][1])
    
print("-" * len(quizzes) * 10)
print("You answered {:d} question{:s} correctly!".format(counter, "" if counter < 2 else "s"))
