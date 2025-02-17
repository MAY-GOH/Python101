# Return the highest and the second highest scores from a list of scores.
def get_top_two_scores(scores):
    scores.sort(reverse = True)
    return scores[:2]

# Return the average of all scores contained in a list of scores.
def calculate_average(scores):
    return sum(scores) / len(scores)

# Return the appropriate ordinal suffix for a given number.
def get_ordinal_suffix(number):
    if number >= 11 and number <= 13:
        return "th"
    else:
        match (number % 10):
            case 1:
                return "st"
            case 2: 
                return "nd"
            case 3:
                return "rd"
            case _:
                return "th"