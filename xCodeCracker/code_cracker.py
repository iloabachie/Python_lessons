import random
import json
import time
import os

KEYS = ("2-DIGITS", "3-DIGITS", "4-DIGITS", "5-DIGITS")
player_registered = False


def printing(text, delay=0.07, new_line=True, rev=False):
    if not rev:
        for _ in range(len(text)):
            print(text[:_ + 1], end='\r')
            time.sleep(delay)
    if rev:
        for _ in range(len(text)):
            print(text[-1 - _:], end='\r')
            time.sleep(delay)
    if new_line:
        print()


def flashprint(text, flashes=5, delay=0.2, stay=True):
    for _ in range(flashes):
        print(text, end=('\r')), time.sleep(delay)
        print(' ' * len(text), end='\r'), time.sleep(delay)
    if stay:
        print(text)


def flashtext(phrase, text, index=-1, flashes=3, delay=0.2):
    textb = ' ' * len(text)
    for _ in range(flashes):
        print(phrase[:index] + text + phrase[index:],
              end='\r'), time.sleep(delay)
        print(phrase[:index] + textb + phrase[index:],
              end='\r'), time.sleep(delay)
    print(phrase[:index] + text + phrase[index:])


def animate(text, symbol="#"):
    symbol = len(text) * symbol
    flashprint(symbol, flashes=2, stay=False)
    flashprint(text, flashes=2, stay=True)


def time_display(time, digits=True):
    time = round(time)
    minute, sec = divmod(time, 60)
    second = '{:02d}'.format(sec)
    minute1 = "minute" if minute in [0, 1] else "minutes"
    second1 = "second" if sec in [0, 1] else "seconds"
    if digits:
        return f'{minute}:{second}'
    else:
        return f'{minute} {minute1} and {second} {second1}'


def launch():
    os.system('cls')
    print()
    printing("{:>40}".format('Welcome to CODE BREAKER'),
             delay=0.1, new_line=False, rev=True), time.sleep(0.3)
    flashprint("{:^57}".format('Welcome to CODE BREAKER'),
               delay=0.3, flashes=3), time.sleep(0.3)
    print()
    print("=" * 57), time.sleep(0.1)
    print("{:^57}".format("***CLUES***")), time.sleep(0.2)
    print("MATCH: at least one correct digit in the correct position"), time.sleep(0.2)
    print("CLOSE: at least one correct digit but in wrong position"), time.sleep(0.2)
    print("NOPE:  no correct digit in your guess"), time.sleep(0.2)
    flashprint("=" * 57, flashes=1), time.sleep(1)


def load_records():
    global records
    try:  # Attempts to extract the records dictionary from JSON file
        with open(r'xCodeCracker/records.json', 'r') as file:
            records = json.load(file)
    except:  # Sets high score and best time to infinity if record does not exist or JSON file absend
        # Sets the dictionary of the records for first time play
        records = {"high_scores": {}, "best_times": {}}


def records_display():
    print()
    print("{:>34}".format('**Leader Board**')), time.sleep(0.05)
    print('+----------+' + '---------------------+' * 2), time.sleep(0.05)
    print('| {:^8} | {:^19} | {:^19} |'.format('Game', 'Steps Record', 'Time Record')), time.sleep(0.05)
    for key in KEYS:
        try:
            name1, high_score = records["high_scores"][key]
            name2, best_time = records["best_times"][key]
        except:
            name1 = name2 = "--"
            high_score = best_time = 0
        minute, sec = divmod(best_time, 60)
        print('+----------' * 5 + '+'), time.sleep(0.05)
        print('| {:8} | {:8} |{:9d} | {:8} |{:6d}:{:02d} |'.format(
            key, name1, high_score, name2, minute, sec)), time.sleep(0.05)
    print('+----------' * 5 + '+\n'), time.sleep(0.05)


def player_capture():
    global player, player_registered
    printing('Enter your name: ', new_line=False)  # Captures player name
    while True:
        player = input('Enter your name: ').strip()
        if player.isalpha() and len(player) <= 8:
            player = player.capitalize()
            print()
            animate(f'Welcome to Code Breaker {player.upper()}')
            player_registered = not player_registered
            break
        else:
            print("Invalid name. Must be maximum 8 characters and contain only letters")
    print()


def reset():
    reset = input("Would you like to reset the Leader board? y or n: ")
    if reset.lower() == 'y':
        confirm = input("  Are you sure? y or n: ")
        if confirm == 'y':
            for rkey in KEYS:
                records["high_scores"][rkey] = ['--', 0]
                records["best_times"][rkey] = ['--', 0]
            with open(r'xCodeCracker/records.json', 'w') as file:
                json.dump(records, file, indent=2, sort_keys=True)
            time.sleep(0.5)
            flashprint("    ...Records cleared...", flashes=2)
            records_display()
        else:
            flashprint('Records unchanged', flashes=2)
    else:
        print()
        flashprint('Records unchanged', flashes=2)
    print(), time.sleep(1)


def code_length():
    global num_digits, key
    while True:
        num_digits = input("Choose the hidden code length: ").strip()
        if num_digits.isnumeric() and 2 <= int(num_digits) <= 5:
            num_digits = int(num_digits)
            break
        else:
            print("Error. Choose a number between 2 and 5 inclusive")
    match num_digits:  # Sets the key value for KEY
        case 2: key = '2-DIGITS'
        case 3: key = '3-DIGITS'
        case 4: key = '4-DIGITS'
        case 5: key = '5-DIGITS'
    print()
    flashtext("You have chosen  ", f"'{key}'")


launch()

while True:
    load_records()
    records_display()
    if not player_registered:
        player_capture()
        reset()
    code_length()

    ### Game core ###
    try:
        high_score = records["high_scores"][key][1]
        best_time = records["best_times"][key][1]
    except:
        high_score = best_time = float('inf')
    count = 0  # Sets the counter variable for counting steps
    hint_count = 3 if num_digits == 5 else 2 if num_digits == 4 else 1 if num_digits == 3 else 0
    pc_code = "".join(random.sample([str(_) for _ in range(10)], num_digits))
    start = time.time()  # Sets start time

    # Ensures that timer only starts counting when player is ready
    input("\nPress 'Enter' to start Code Cracking: ")
    while True:
        attempt = "attempt" if count == 1 else "attempts"
        if hint_count != 0:
            guess = input(f"\nMake a {num_digits}-digit number guess, type hint or type quit: ").strip().lower()
        else:
            guess = input(f"\nMake a {num_digits}-digit number guess or type quit: ").strip().lower()
        if guess.isnumeric() and len(guess) == num_digits and len(set(guess)) == num_digits:
            merge = [len(set(_)) for _ in zip(pc_code, guess)]
            count += 1
            if guess == pc_code:
                break
            elif 1 in merge:
                print(f"M A T C H: {attempt}= {count} | time= {time_display(time.time() - start)} | hints left= {hint_count}")
            elif len(guess + pc_code) != len(set(guess + pc_code)):
                print(f"C L O S E: {attempt}= {count} | time= {time_display(time.time() - start)} | hints left= {hint_count}")
            else:
                print(f"N O P E: {attempt}= {count} | time= {time_display(time.time() - start)} | hints left= {hint_count}")
        elif guess == 'hint' and hint_count != 0:
            hint = input(
                f"Adds {num_digits // 2 } steps and provides a random digit.  Press 'Enter' to proceed or type no to cancel.").strip().lower()
            if hint == 'no':
                print("No hint. Continue...")
            else:
                hint_index = random.randint(0, num_digits - 1)
                print("|", end="")
                for _ in range(num_digits):
                    if _ != hint_index:
                        print("_", end="|")
                    else:
                        print(pc_code[_], end="|")
                hint_count -= 1
                count += num_digits // 2
                print(f'\n{attempt}= {count} | time= {time_display(time.time() - start)} | hints left= {hint_count}')
        elif guess == 'hint' and hint_count == 0:
            print("Sorry, you have used up your hints")
        elif guess == 'python' and hint_count == 0:
            hint_count = 3 if num_digits == 5 else 2 if num_digits == 4 else 1
            count += hint_count
            print(f'{attempt}= {count} | time= {time_display(time.time() - start)} | hints left= {hint_count}')
        elif guess == 'test':
            count += num_digits
            flashprint(pc_code, delay=0.5, stay=False, flashes=1)
        elif guess == 'time':
            print(time_display(time.time() - start))
        elif guess == 'quit':
            print()
            printing("Exiting game...")
            break
        else:
            print(f"Guess Error, guess must contain {num_digits} distinct numbers")

    if guess == "quit":
        break
    else:
        end = round(time.time() - start)  # Captures end time
        duration = time_display(end, digits=False)
        animate1 = '#' * len(player) + '\b' * len(player)

        print()
        flashprint("     ***CODE CRACKED***", flashes=4)
        printing(f"Completed in {count} {attempt} and took {duration}"), time.sleep(1.5)

        # Saves only the fastest score or time in JSON file
        if (high_score == 0 or count < high_score):
            records["high_scores"][key] = [player, count]
        if (best_time == 0 or end < best_time):
            records["best_times"][key] = [player, end]

        if (high_score == 0 or count < high_score) and (best_time == 0 or end < best_time):
            printing(f"MASTER CODE BREAKER!!! {player}, you SMASHED the steps and time records for '{key}'", new_line=False)
            flashtext(f" {player}, you SMASHED the steps and time records for '{key}'", "MASTER CODE BREAKER!!!", index=0, flashes=6)
        else:
            if high_score == 0 or count < high_score:
                printing(f"**Congratulations {animate1}{player}!!! You broke the steps record for '{key}'")
                print(f"But you missed the time record by {duration}")
            if best_time == 0 or end < best_time:
                printing(f"**Congratulations {animate1}{player}!!! You broke the time record for '{key}'")
                print(f'But you missed the steps record by {count_diff} steps')
            if not (high_score == 0 or count < high_score) or (best_time == 0 or end < best_time):
                count_diff, time_diff = count - high_score, end - best_time
                duration = time_display(time_diff, digits=False)
                print(f"You missed the record for {key} by {count_diff} steps\nYou missed the time record by {duration}"), time.sleep(1.5)

        if (high_score == 0 or count < high_score) or (best_time == 0 or end < best_time):
            with open(r'xCodeCracker/records.json', 'w') as file:
                json.dump(records, file, indent=2, sort_keys=True)

    records_display()

    play_again = input("Press 'Enter' to play again or type 'quit' to exit game...").strip().lower()

    if play_again == 'quit':
        break
    os.system('cls')
print()
printing("Thank you for playing CODE BREAKER!!!")
print('©2023\n')
