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
