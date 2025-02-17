import random

# Define a dictionary mapping each state in Malaysia to its corresponding capital city as a constant.
STATE_CAPITAL = {
    "Johor": "Johor Bahru", "Kedah": "Alor Setar", "Kelantan": "Kota Bharu",
    "Malacca": "Malacca City", "Negeri Sembilan": "Seremban",
    "Pahang": "Kuantan", "Penang": "George Town", "Perak": "Ipoh",
    "Perlis": "Kangar", "Sabah": "Kota Kinabalu", "Sarawak": "Kuching",
    "Selangor": "Shah Alam", "Terengganu": "Kuala Terengganu",
    "Kuala Lumpur": "Kuala Lumpur", "Labuan": "Victoria", "Putrajaya": "Putrajaya"
}

# Return a shuffled list of dictionary's keys.
def shuffling():
    keys = list(STATE_CAPITAL.keys())
    random.shuffle(keys)
    
    return keys

# Return a capital from user input.
def read_capital(state):
    return input("\nEnter the capital of {:16}: ".format(state)).strip()
    
# Simulate the quiz of guessing the capital cities of different states.
def guess_capitals_quiz():
    keys = shuffling()
    count = 0

    print("Identify the capital of following states:")
    for i in range(len(keys)):
        capital = read_capital(keys[i])    
        if capital.lower() == STATE_CAPITAL[keys[i]].lower():
            print("Correct")
            count += 1
        else:
            print("Wrong")

    print("\nYou answered {:d} {:s} correctly!".format(count, "questions" if count > 1 else "question"))