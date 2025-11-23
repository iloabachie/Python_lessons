import random
import json

white_possibles = list(range(1, 70))
red_possibles = list(range(1, 27))

tickets_per_drawing = 10
num_drawings = 36

total_spent = 0
earnings = 0

times_won = {
    "5+P": 0,
    "5": 0,
    "4+P": 0,
    "4": 0,
    "3+P": 0,
    "3": 0,
    "2+P": 0,
    "1+P": 0,
    "P": 0,
    "0": 0,
}


def calc_win_amt(my_numbers, winning_numbers):
    win_amt = 0

    white_matches = len(my_numbers["whites"].intersection(winning_numbers["whites"]))
    power_match = my_numbers["red"] == winning_numbers["red"]

    if white_matches == 5:
        if power_match:
            win_amt = 2_000_000_000
            times_won["5+P"] += 1
        else:
            win_amt = 1_000_000
            times_won["5"] += 1
    elif white_matches == 4:
        if power_match:
            win_amt = 50_000
            times_won["4+P"] += 1
        else:
            win_amt = 100
            times_won["4"] += 1
    elif white_matches == 3:
        if power_match:
            win_amt = 100
            times_won["3+P"] += 1
        else:
            win_amt = 7
            times_won["3"] += 1
    elif white_matches == 2 and power_match:
        win_amt = 7
        times_won["2+P"] += 1
    elif white_matches == 1 and power_match:
        win_amt = 4
        times_won["1+P"] += 1
    elif power_match:
        win_amt = 4
        times_won["P"] += 1
    else:
        times_won["0"] += 1

    return win_amt


# for drawing in range(num_drawings):
hit_jp = False
drawings = 0
years = 0
while not hit_jp:
    drawings += 1
    white_drawing = set(random.sample(white_possibles, k=5))
    red_drawing = random.choice(red_possibles)

    winning_numbers = {"whites": white_drawing, "red": red_drawing}

    for ticket in range(tickets_per_drawing):
        total_spent += 2
        my_whites = set(random.sample(white_possibles, k=5))
        my_red = random.choice(red_possibles)

        my_numbers = {"whites": my_whites, "red": my_red}
        # my_numbers = {"whites": {31, 10, 44, 27, 56}, "red": 15}

        win_amt = calc_win_amt(my_numbers, winning_numbers)
        earnings += win_amt

        if win_amt == 2_000_000_000:
            hit_jp = True
            break

    if drawings % 156 == 0:
        years += 1
        print(f' {years:,} years', end='\r')


print(f'\nSpent: ${total_spent:,}')
print(f'Earnings: ${earnings:,}')

print(json.dumps(times_won, indent=2))
print(times_won)



def generate_649():
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()
    return numbers

# Generate a set of 6 numbers for 6/49 lottery
lottery_numbers_649 = generate_649()
print("Ontario 6/49 Lottery Numbers:", lottery_numbers_649)


def generate_lotto_max():
    numbers = random.sample(range(1, 50), 7)  # 7 numbers are selected for Lotto Max
    bonus_number = random.randint(1, 50)  # Bonus number selection
    numbers.sort()
    return numbers, bonus_number

# Generate numbers and bonus for Lotto Max
lottery_numbers_lotto_max, bonus_number = generate_lotto_max()
print("Ontario Lotto Max Lottery Numbers:", lottery_numbers_lotto_max)
print("Bonus Number:", bonus_number)
