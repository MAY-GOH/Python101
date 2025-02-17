# Set the interest rates
ANNUAL_INTEREST_RATE = 0.05
MONTHLY_INTEREST_RATE = ANNUAL_INTEREST_RATE / 12

# Return an integer that represents quantity of students
def read_months(prompt_msg):
    while True:
        quantity = input(prompt_msg)
        if quantity.isdigit():
            quantity = int(quantity)
            if quantity <= 0:
                print("error: Only positive integer is allowed!\n")
            else:
                return quantity
        else:
            print("Error: Only positive integer is allowed!\n")
            
# Return an integer that represents quantity of students
def read_base(prompt_msg):
    while True:
        try:
            base = float(input(prompt_msg))
            if base <= 0:
                print("Error: Only positive numbers are allowed!\n")
            else:
                return base
        except:
            print("Error: Only numbers are allowed!\n")

# Return the amount of monthly saving.  
def calculate_monthly_saving(base, total):
    return (base + total) * (1 + MONTHLY_INTEREST_RATE)
   
# Print the amount of monthly saving for quantity number of months. 
def print_monthly_savings(base, quantity):
    print("\n{:12s}{:12s}".format("Month", "Total"))
    total = 0
    for count in range(1, quantity + 1):
        total = calculate_monthly_saving(base, total)
        print("{:12s}RM {:<10.2f}".format(get_ordinal_suffix(count), total))

# Return the appropriate ordinal suffix for a given number.
def get_ordinal_suffix(number):
    if number >= 11 and number <= 13:
        return str(number) + "th"
    else:
        match (number % 10):
            case 1:
                return str(number) + "st"
            case 2:
                return str(number) + "nd"
            case 3: 
                return str(number) + "rd"
            case _:
                return str(number) + "th"