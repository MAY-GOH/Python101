# Define different pay rates as CONSTANT
HOURLY_RATE = 40
OT_REGULAR_RATE = HOURLY_RATE * 1.5
OT_EXCESS_RATE = HOURLY_RATE * 2

# Define the upper limit of different pay rates as CONSTANT
HOURLY_RATE_LIMIT = 35
REGULAR_RATE_LIMIT = 25

# Return the amount of total wage.
def calculate_total_wage(hours):
    return calculate_regular_pay(hours) + calculate_OT_pay(hours)

# Return the amount of regular pay.
def calculate_regular_pay(hours):    
    if hours <= HOURLY_RATE_LIMIT:
        return hours * HOURLY_RATE
    else:
        return HOURLY_RATE_LIMIT * HOURLY_RATE

# Return the total amount of OT.
def calculate_OT_pay(hours):
    return calculate_regular_OT_pay(hours) + calculate_excess_OT_pay(hours)

# Return the amount of regular OT.
def calculate_regular_OT_pay(hours):
    if hours <= HOURLY_RATE_LIMIT:
        return 0
    elif hours <= (HOURLY_RATE_LIMIT + REGULAR_RATE_LIMIT):
        return (hours - HOURLY_RATE_LIMIT) * OT_REGULAR_RATE
    else:
        return REGULAR_RATE_LIMIT * OT_REGULAR_RATE

# Return the amount of excessive OT.
def calculate_excess_OT_pay(hours):
    if hours <= HOURLY_RATE_LIMIT:
        return 0
    elif hours <= (HOURLY_RATE_LIMIT + REGULAR_RATE_LIMIT):
        return 0
    else:
        return (hours - HOURLY_RATE_LIMIT - REGULAR_RATE_LIMIT) * OT_EXCESS_RATE