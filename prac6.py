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

