# Return the sum of all numbers
def calculate_sum(numbers):
    return sum(numbers)

# Return the average of all numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Return the number of positive and negative numbers
def count_positive_negative(numbers):
    pos, neg = 0, 0
    for number in numbers:
        if number > 0:
            pos += 1
        else:
            neg += 1
    return (pos, neg)

# Print the number of positive and negative numbers, and the sum and average of all numbers
def print_summary(numbers):   
    pos, neg = count_positive_negative(numbers)
    print("\nNo. of positive numbers: {:d}".format(pos))
    print("No. of negative numbers: {:d}".format(neg))
    print("Sum of all numbers     : {:d}".format(calculate_sum(numbers)))
    print("Average of all numbers : {:.2f}".format(calculate_average(numbers)))