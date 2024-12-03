# Question 1
# retrieve score input (in float)
# use if, elif, else: (for score, to determine grade)
# match grade: (print output) 
score = float(input("Enter a score: ")) #retrieve from user input
grade = ""

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

# complete for other score
match grade:
    case 'A'|'F':
        print("You got an ", grade, " for the test")
    case 'B'|'C'|'D':
        print("You got a ", grade, " for the test")
    case _:
        print("You entered wrong input")

# Question 2
import random

#If user input is 0, quit this while loop - break
while True:
  answer= random.randint(1,2)

  guess = int(input("Enter your guess as 1 for a head, 2 for a tail, or 0 to exit: "))

  if guess == 0:
    print("Thank you for playing game!\n")
    break
  elif guess == 1 or guess == 2:
    if answer == guess:
      print("Your guess is correct!\n")
    else:
      print("Your guess is incorrect!\n")
  else: 
    print("Please enter again (only choose from 0,1 or 2)\n")

# Question 3
HOURLY_RATE = 40
OT_REGULAR_RATE = HOURLY_RATE * 1.5
OT_EXCESS_RATE = HOURLY_RATE * 2
HOURLY_RATE_LIMIT = 35
EXCESS_RATE_LIMIT = 25

# input hour <- int
hours = float(input("Enter working hours: "))

# if hours <= 35, regular pay, update hour
if hours <= 35:
  regular_pay = hours * HOURLY_RATE
else:
  regular_pay = HOURLY_RATE_LIMIT * HOURLY_RATE
  hours -= HOURLY_RATE_LIMIT

if hours <= 25:
  overtime_pay = hours * OT_REGULAR_RATE
else:
  regular_pay = EXCESS_RATE_LIMIT * OT_REGULAR_RATE
  hours -= EXCESS_RATE_LIMIT

# calculate OT
overtime_pay += hours * OT_EXCESS_RATE

print("{:15s}: RM{:.2f}".format("Total Salary", regular_pay + overtime_pay))
print("{:15s}: RM{:.2f}".format("Regular Pay" , regular_pay))
print("{:15s}: RM{:.2f}".format("Overtime Pay" , overtime_pay))

# Question 4
CAT_1_RATE = 0.01
CAT_2_RATE = 0.05
CAT_3_RATE = 0.10

CAT_1_CAPPED = 1000
CAT_2_CAPPED = 10000
CAT_3_CAPPED = 100000

CAT_1_COMM = CAT_1_CAPPED * CAT_1_RATE                  # 10
CAT_2_COMM = (CAT_2_CAPPED - CAT_1_CAPPED) * CAT_2_RATE # 450
CAT_3_COMM = (CAT_3_CAPPED - CAT_2_CAPPED) * CAT_3_RATE # 9000

# Read a sales value from the user
sales = float(input("Enter sales value (RM): ")) 

if sales >= 99999:
    commission = CAT_1_COMM + CAT_2_COMM + CAT_3_COMM
elif sales > 10000:
    commission = CAT_1_COMM + CAT_2_COMM + (sales - 10000) * CAT_3_RATE
elif sales > 1000:
    commission = CAT_1_COMM + (sales - 1000) * CAT_2_RATE
else:  
    commission = sales * CAT_1_RATE

print("{:s}: RM{:.2f}".format("Total commission", commission))

# Question 5
size = int(input("Enter the number of students: "))

highest = -1
second_highest = -1
total = 0.0

for count in range(1, size + 1):
    if count >= 11 and count <= 13:
        suffix = "th"
    else:
        match (count % 10):
            case 1:
                suffix = "st"
            case 2: 
                suffix = "nd"
            case 3:
                suffix = "rd"
            case _:
                suffix = "th"
    message = "Enter the score of the {}{} student: ".format(str(count), suffix)
    
    score = float(input(message))
    total += score
    
    if score > highest:
        second_highest = highest
        highest = score
    else:
        if score > second_highest:
            second_highest = score

# Output: Print average score
print("\nThe highest score       : {:.0f}%".format(highest))
print("The second highest score: {:.2f}%".format(second_highest))
print("The average score       : {:.2f}%".format(total / size))

# Question 6
counter = 0
number_pos = 0
number_neg = 0
total = 0

while True:
  numberInput = int(input("Enter a number: "))

  match numberInput:
    case 0:
      break
    case _:
      counter +=1
      total += numberInput

      if numberInput >0:
        number_pos += 1
      else:
        number_neg += 1
          
print("\nNo. of positive numbers: {:d}".format(number_pos))
print("No. of negative numbers: {:d}".format(number_neg))
print("Sum of all numbers     : {:d}".format(total))
print("Average of all numbers : {:.2f}".format((total/counter)))

# Question 7
ANNUAL_INTEREST = 0.05
monthly_interest = ANNUAL_INTEREST / 12

base_value = 0
total = 0
repitition = 6

base_value = int(input("Enter the monthly saving amount: "))

for count in range(repitition):
  total = (base_value + total) * (1 + monthly_interest)

print("{:s} {:.2f}".format("After the sixth month, the account value is RM", total))

# Question 8
emoji_code_right = 128072
emoji_code_left = 128073
separator = ""

number = int(input("Enter a positive integer: "))

print("\n" + chr(emoji_code_left), "Shape #1", chr(emoji_code_right))
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n" + chr(emoji_code_left), "Shape #2", chr(emoji_code_right))
for i in range(1, number + 1):
    for j in range(1, (number + 2) - i):
        print(j, end=" ")
    print()

print("\n" + chr(emoji_code_left), "Shape #3", chr(emoji_code_right))
for i in range(1, number + 1):
    for j in range(number, 0, -1):
        if i < j:
            print(" ", end=" ")
        else:            
            print(j, end=" ")
    print()

print("\n" + chr(emoji_code_left), "Shape #4", chr(emoji_code_right))
for i in range(1, number + 1):
    for j in range(1, number + 1):
        if i > j:
            print(" ", end=" ")
        else:            
            print(j, end=" ")
    print()
    
# Question 9

number = int(input("Enter a positive integer: "))

for i in range(1, number + 1):
    total = 0
    for j in range(1, i + 1):
        if j == i:
            print(j, end="")
        else:
            print(j, "+ ", end="")
        total += j
    print(" =", total)
    
# Question 10
QUANTITY = 4
counter = 0

print("QUIZ")

for i in range(QUANTITY):
    print("-" * QUANTITY * 10)
    print("Q" + str(i + 1) + ":", end=" ")

    match i:
        case 0:
            print("12 + 8 = ?")
            print("A. 14\tB. 16\tC. 18\tD. 20")
            answer = input("\nEnter your answer (A or B or C or D): ")
            
            if answer == "D" or answer == "d":
                print("Correct!")
                counter += 1
            else:
                print("Wrong!")

        case 1: 
            print("15 - 7 = ?")
            print("A. 6\tB. 7\tC. 8\tD. 9")
            answer = input("\nEnter your answer (A or B or C or D): ")
            
            if answer == "C" or answer == "c":
                print("Correct!")
                counter += 1
            else:
                print("Wrong!")
            
        case 2:
            print("9 x 6 = ?")
            print("A. 45\tB. 48\tC. 54\tD. 60")
            answer = input("\nEnter your answer (A or B or C or D): ")
            
            if answer == "C" or answer == "c":
                print("Correct!")
                counter += 1
            else:
                print("Wrong!")
            
        case 3:
            print("40 / 5 = ?")
            print("A. 7\tB. 8\tC. 9\tD. 10")
            answer = input("\nEnter your answer (A or B or C or D): ")
            
            if answer == "B" or answer == "b":
                print("Correct!")
                counter += 1
            else:
                print("Wrong!")
            
    if i == QUANTITY - 1:
        print("-" * 40)
    
if counter == 4:
    print("Conclusion: Congratulations! You answered all the questions correctly!")
else:
    print("Conclusion: Keep practicing, and you'll improve!")
    
# Question 11
import random

counter = 0
user_win = 0
user_lose = 0
draw = 0

while True:
    # 0, 1, or 2 represents "scissors", "rock", and "paper" respectively
    answer = random.randint(0, 2) 
    
    print("0: scissors, 1: rock, and 2: paper")
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 0 or choice == 1 or choice == 2:
            break
        else:
            print("Wrong input...")
    
    match answer:
        case 0:
            print("Computer's choice: Scissors")
        case 1: 
            print("Computer's choice: Rock")
        case 2:
            print("Computer's choice: Paper")
    
    if choice == answer:
        print("Draw!")
        draw += 1
    elif (choice == 0 and answer == 2) or (choice == 1 and answer == 0) or (choice == 2 and answer == 1):
        print("You win!")
        user_win += 1 
    else:
        print("You lose!")
        user_lose += 1
    
    counter += 1
    
    print()
    if (counter > 2) and (user_win != user_lose):
        print("You won", user_win, "times" if user_win > 1 else "time", end=" ")
        print("and computer won", user_lose, "times." if user_lose > 1 else  "time.")
        if user_win > user_lose:
            print("You are the final winner!")
        else:
            print("Computer is the final winner!")
        break
        
# Question 12

import random

digit_1 = random.randint(0, 9) 
digit_2 = random.randint(0, 9) 
digit_3 = random.randint(0, 9) 

guess = int(input("Enter a 3-digit integer: "))

guess_3 = guess % 10
answer = guess // 10
guess_2 = answer % 10
guess_1 = answer // 10

if digit_1 == guess_1 and digit_2 == guess_2 and digit_3 == guess_3:
    print("Congratulations! You won RM10,000!")
elif (digit_1 == guess_1 and digit_2 == guess_3 and digit_3 == guess_2) or \
     (digit_1 == guess_2 and digit_2 == guess_1 and digit_3 == guess_3) or \
     (digit_1 == guess_2 and digit_2 == guess_3 and digit_3 == guess_1) or \
     (digit_1 == guess_3 and digit_2 == guess_2 and digit_3 == guess_1) or \
     (digit_1 == guess_3 and digit_2 == guess_1 and digit_3 == guess_2):
    print("Congratulations! You win RM3,000!") 
elif (digit_1 == guess_1 and digit_2 != guess_2 and digit_3 != guess_3) or \
     (digit_1 == guess_1 and digit_2 != guess_3 and digit_3 != guess_2) or \
     (digit_1 == guess_2 and digit_2 != guess_1 and digit_3 != guess_3) or \
     (digit_1 == guess_2 and digit_2 != guess_3 and digit_3 != guess_1) or \
     (digit_1 == guess_3 and digit_2 != guess_2 and digit_3 != guess_1) or \
     (digit_1 == guess_3 and digit_2 != guess_1 and digit_3 != guess_2) or \
     (digit_2 == guess_1 and digit_1 != guess_2 and digit_3 != guess_3) or \
     (digit_2 == guess_1 and digit_1 != guess_3 and digit_3 != guess_2) or \
     (digit_2 == guess_2 and digit_1 != guess_1 and digit_3 != guess_3) or \
     (digit_2 == guess_2 and digit_1 != guess_3 and digit_3 != guess_1) or \
     (digit_2 == guess_3 and digit_1 != guess_2 and digit_3 != guess_1) or \
     (digit_2 == guess_3 and digit_1 != guess_1 and digit_3 != guess_2) or \
     (digit_3 == guess_1 and digit_2 != guess_2 and digit_1 != guess_3) or \
     (digit_3 == guess_1 and digit_2 != guess_3 and digit_1 != guess_2) or \
     (digit_3 == guess_2 and digit_2 != guess_1 and digit_1 != guess_3) or \
     (digit_3 == guess_2 and digit_2 != guess_3 and digit_1 != guess_1) or \
     (digit_3 == guess_3 and digit_2 != guess_2 and digit_1 != guess_1) or \
     (digit_3 == guess_3 and digit_2 != guess_1 and digit_1 != guess_2):
    print("Congratulations! You win RM1,000!") 
else:
    print("I regret to inform you that your ticket did not win a prize this time.") 
