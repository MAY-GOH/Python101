# Return the appropriate article for a given grade.
def get_article(grade):
    match grade:
        case 'A' | 'F':
            return "an"
        case 'B' | 'C' | 'D':
            return "a"

# Return a grade based on the provided score.
def get_grade(score):
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    return grade