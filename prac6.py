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
