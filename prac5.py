# Question 1
message = input("Enter a string: ").strip()

words = message.split()
acronym = ""

for word in words:
    acronym += word[0].upper()
    
print("The acronym for '{}' is '{}'".format(message.strip(), acronym))

# Question 2
message = input("Enter a string: ").strip()

# Count the number of words using count()
words = message.split()
print("\nNo. of words:", len(words))

# Count the number of vowels
vowel = "aeiou"
message = message.lower()
print()
for character in vowel:
    print("No. of {}: {:d}".format(character, message.count(character)))
    
# Calculate the average word length
total = 0
for word in words:
    total += len(word)
print("\nAverage: {:.2f}".format(total / len(words)))

# Question 3
# Set the interest rates
annual_interest = 0.05
monthly_interest = annual_interest / 12

# Set the amount to be saved monthly
base = 100
total = 0
repetition = 10
month = ""

print("{:10s}{:10s}".format("Month", "Total"))
for count in range(repetition):
    total = (base + total) * (1 + monthly_interest)
    
    match (count + 1) % 10:
        case 1:
            month = str(count + 1) + "st"
        case 2:
            month = str(count + 1) + "nd"
        case 3: 
            month = str(count + 1) + "rd"
        case _:
            month = str(count + 1) + "th"
    
    print("{:10s}RM {:<10.2f}".format(month, total))

# Question 4
str1 = input("Enter a string: ").strip()
str2 = str1.lower()

for letter in str2:
    if not letter.isalpha():
        str2 = str2.replace(letter, '')

length = len(str2)
result = True
        
for i in range(len(str2)):
    if str2[i] != str2[length - 1 - i]:
        result = False  # Not a palindrome
        break

print("'{}' {} a palindrome!".format(str1, "is" if result else "is not"))

# Question 5
isbn = input("Enter the first 9 digits of an ISBN-10 as a string: ").strip()
number = int(isbn)
total = 0
counter = 9

while counter != 0:
    total += ((number % 10) * counter)
    counter -= 1
    number = number // 10

check_sum = total % 11
print("The ISBN-10 number is", isbn + (str(check_sum) if check_sum < 10 else "X"))

# Question 6
while True:
    condition1 = False
    condition2 = False
    condition3 = False
    
    pw1 = input("Enter a password: ")

    if (len(pw1) >= 8 and len(pw1) <= 12):
        condition1 = True
    else:
        print("The password must have at least 8 characters and at most 12 characters.")
        
    non_alnum = [character for character in pw1 if not character.isalnum()]
    if len(non_alnum) == 0:
        condition2 = True
    else:
        print("The password must consist of only letters and digits.")
        
    digit = 0
    letter = 0
    for character in pw1:
        if character.isdigit():
            digit += 1
        if character.isalpha():
            letter += 1
    if digit > 0 and letter > 0:
        condition3 = True
    else:
        print("The password must contain at least one letter and one digit.")
    
    if condition1 and condition2 and condition3:
        pw2 = input("Enter the password again: ")
        
        if pw1 == pw2:
            print("Congratulations! Your password is created successfully!")
        else:
            print("The two password do not match each other...\n")
            continue
        
        break
    else:
        print()

  # Question 7
  while True:
    print("1. Encoding\n2. Decoding\n3. Exit")
    option = int(input("Enter an option (1, 2 or 3): "))

    match option:
        case 1:
            print("\n--------------------Encoding--------------------")
            message = input("Enter a message to be encoded: ").strip()
            key = int(input("Enter a key: "))
            
            code = ""
            
            char_list = list(message)
            for char in char_list:
                code += chr(ord(char) + key)
            
            print("The encoded message is '{}'\n".format(code))
            
        case 2:
            print("\n--------------------Decoding--------------------")
            message = input("Enter a message to be decoded: ").strip()
            key = int(input("Enter a key: "))
            
            decode = ""
            
            char_list = list(message)
            for char in char_list:
                decode += chr(ord(char) - key)            
            
            print("The decoded message is '{}'\n".format(decode))
            
        case 3:
            print("\nThank you! See you again!")
            break
            
        case _:
            print("\nWrong input!\n")
# Question 8
import string

items_1 = string.ascii_letters + string.digits + " " + string.punctuation
items_2 = items_1[::-1]
size = len(items_1)

while True:
    print("1. Encoding\n2. Decoding\n3. Exit")
    option = int(input("Enter an option (1, 2 or 3): "))

    match option:
        case 1:
            print("\n--------------------Encoding--------------------")
            message = input("Enter a message to be encoded: ").strip()
            key = int(input("Enter a key: "))
            
            code = ""
            
            char_list = list(message)
            for char in char_list:
                position = items_1.index(char)
                new_position = position + key
                new_position = new_position % size
                code += items_1[new_position]
            
            print("The encoded message is '{}'\n".format(code))
            
        case 2:
            print("\n--------------------Decoding--------------------")
            message = input("Enter a message to be decoded: ").strip()
            key = int(input("Enter a key: "))
            
            decode = ""
            
            char_list = list(message)
            for char in char_list:
                position = items_2.index(char)
                new_position = position + key
                new_position = new_position % size
                decode += items_2[new_position]               
            
            print("The decoded message is '{}'\n".format(decode))
            
        case 3:
            print("\nThank you! See you again!")
            break
            
        case _:
            print("\nWrong input!\n")

# Question 9
import random

counter = 0
user_win = 0
user_lose = 0
draw = 0

while True:
    # 0, 1, or 2 represents "scissor", "rock", and "paper" respectively
    answer = random.randint(0, 2) 

    while True:
        choice = input("Enter your choice (scissor/rock/paper): ").strip().lower()
        if choice[:2] == "sc" or choice[:2] == "ro" or choice[:2] == "pa":
            match choice[:2]:
                case "sc":
                    choice = 0
                case "ro": 
                    choice = 1
                case "pa":
                    choice = 2
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

# Question 10
import string

items_1 = string.ascii_letters + string.digits + " " + string.punctuation
items_2 = items_1[::-1]
size = len(items_1)

while True:
    print("1. Encoding\n2. Decoding\n3. Exit")
    while True:
        choice = input("Enter an option (1, 2 or 3): ")
        if choice == '1' or choice == '2' or choice == '3':
            choice = int(choice)
            break
        else:
            print("Wrong input...")
            
    match choice:
        case 1:
            print("\n--------------------Encoding--------------------")
            message = input("Enter a message to be encoded: ").strip()
            
            while True:
                key = input("Enter a key: ")
                if key.isdigit():
                    key = int(key)
                    break
                else:
                    print("Only integer is acceptable...")
            
            code = ""
            
            char_list = list(message)
            for char in char_list:
                position = items_1.index(char)
                new_position = position + key
                new_position = new_position % size
                code += items_1[new_position]
            
            print("The encoded message is '{}'\n".format(code))
            
        case 2:
            print("\n--------------------Decoding--------------------")
            message = input("Enter a message to be decoded: ").strip()
            
            while True:
                key = input("Enter a key: ")
                if key.isdigit():
                    key = int(key)
                    break
                else:
                    print("Only integer is acceptable...")
            
            decode = ""
            
            char_list = list(message)
            for char in char_list:
                position = items_2.index(char)
                new_position = position + key
                new_position = new_position % size
                decode += items_2[new_position]               
            
            print("The decoded message is '{}'\n".format(decode))
            
        case 3:
            print("\nThank you! See you again!")
            break
            
        case _:
            print("\nWrong input!\n")

  # Question 11
  import random

while True:
    answer = random.randint(1, 2)

    guess = input("Enter your guess as 1 for a head, 2 for a tail, or 0 to exit: ")

    if guess.isdigit():
        guess = int(guess)
        if guess == 0:
            print("Thank you for playing the game!\n")
            break
        elif guess == 1 or guess == 2:
            if answer == guess:
                print("Your guess is correct!\n")
            else:
                print("Your guess is incorrect!\n")
        else:
            print("Please enter 0, 1, or 2.\n")
    else:
        print("Please enter 0, 1, or 2.\n")
