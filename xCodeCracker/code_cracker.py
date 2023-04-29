import random
import json
import time
import os

KEYS = ("2-DIGITS", "3-DIGITS", "4-DIGITS", "5-DIGITS")

def printing(text, delay=0.07, new_line=True, rev=False):
    if not rev:
        for _ in range(len(text)):
            print(text[:_ + 1], end='\r')
            time.sleep(delay)
    if rev:    
        for _ in range(len(text)):
            print(text[-1 - _:], end='\r')
            time.sleep(delay)
    if new_line: print()

def flashprint(text, flashes=5, delay=0.2, stay=True):
    for _ in range(flashes):
        print(text, end=('\r')), time.sleep(delay)
        print(' ' * len(text), end='\r'), time.sleep(delay)
    if stay: print(text)

def launch():
    os.system('cls')
    print()
    printing("{:^57}".format('Welcome to CODE BREAKER'), delay=0.1, new_line=False, rev=True), time.sleep(0.3)
    flashprint("{:^57}".format('Welcome to CODE BREAKER'), delay=0.4, flashes=3), time.sleep(0.5)
    print()
    print("=" * 57), time.sleep(0.1)
    print("{:^57}".format("***CLUES***")), time.sleep(0.2)
    print("MATCH: at least one correct digit in the correct position"), time.sleep(0.2)
    print("CLOSE: at least one correct digit but in wrong position"), time.sleep(0.2)
    print("NOPE:  no correct digit in your guess"), time.sleep(0.2)
    flashprint("=" * 57, flashes=1), time.sleep(1)

def records_dict():
    global records
    try: # Attempts to extract the records dictionary from JSON file
        with open(r'xCodeCracker/records.json', 'r') as file:
            records = json.load(file)
    except:  # Sets high score and best time to infinity if record does not exist or JSON file absend
        records = {"high_scores": {}, "best_times": {}} # Sets the dictionary of the records for first time play
        
def display_records():
    print()
    print("{:>34}".format('**Leader Board**')), time.sleep(0.05)
    print('+----------+' + '---------------------+' * 2), time.sleep(0.05)
    print('| {:8} | {:19} | {:19} |'.format('Game', 'Steps Record', 'Time Record')), time.sleep(0.05)
    for key in KEYS:
        try:
            name1, high_score = records["high_scores"][key]
            name2, best_time = records["best_times"][key]
        except:
            name1 = name2 = "--"
            high_score = best_time = 0
        minute, sec = divmod(best_time, 60)  
        print('+----------' * 5 + '+'), time.sleep(0.05)
        print('| {:8} | {:8} |{:9d} | {:8} |{:6d}:{:02d} |'.format(key, name1, high_score, name2, minute, sec)), time.sleep(0.05)
    print('+----------' * 5 + '+\n'), time.sleep(0.05)

def player_capture():
    global player, animate
    printing('Enter your name: ', new_line=False) # Captures player name
    while True:
        player = input('Enter your name: ')
        if player.isalpha() and len(player) <= 8:
            player = player.capitalize()
            print()
            animate = '#' * len(player) + '\b' * len(player)
            printing(f'Welcome to Code Breaker {animate}{player}    ')
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
            display_records() 
        else:
            flashprint('Records unchanged')    
    else:
        print()
        flashprint('Records unchanged')  
    print(), time.sleep(1)

def code_length():
    global num_digits, key
    while True:
        num_digits = input("Choose the hidden code length: ")
        if num_digits.isnumeric() and 2 <= int(num_digits) <= 5:
            num_digits = int(num_digits)
            break
        else:
            print("Error. Choose a number between 2 and 5 inclusive")
    match num_digits: # Sets the key value for KEY
        case 2: key = '2-DIGITS'
        case 3: key = '3-DIGITS'
        case 4: key = '4-DIGITS'
        case 5: key = '5-DIGITS'  
    for _ in range(3):
        print(f"You have chosen '{key}'", end="\r"), time.sleep(0.2)
        print("You have chosen           ", end="\r"), time.sleep(0.2)
    print(f"You have chosen '{key}'")

launch() 
records_dict()
display_records()
player_capture()
reset()
code_length()

### Game core ###
try:
    high_score = records["high_scores"][key][1]
    best_time = records["best_times"][key][1]
except:
    high_score = best_time = float('inf')
count = 1 # Sets the counter variable for counting steps
used_hint = False
pc_code = "".join(random.sample([str(_) for _ in range(10)], num_digits))
start = time.time()  # Sets start time   

input("\nPress 'Enter' to start Code Cracking: ")  # Ensures that timer only starts counting when player is ready
while True:
    attempt = "attempt" if count == 1 else "attempts"     
    if not used_hint:
        guess = input(f"\nMake a {num_digits}-digit number guess, type hint or type quit: ")    
    else:
        guess = input(f"\nMake a {num_digits}-digit number guess or type quit: ")
    if guess.isnumeric() and len(guess) == num_digits and len(set(guess)) == num_digits:
        merge = [len(set(_)) for _ in zip(pc_code, guess)]
        if guess == pc_code:
            break        
        elif 1 in merge:
            print(f"MATCH: {attempt}={count}")            
        elif len(guess + pc_code) != len(set(guess + pc_code)):  
            print(f"CLOSE: {attempt}={count}")           
        else:
            print(f"NOPE: {attempt}={count}")
        count += 1
    elif guess.lower() == 'hint' and not used_hint:
        hint = input("  Adds 2 steps and provides a random digit.  Press 'Enter' to proceed or type no to cancel.")
        if hint.lower() == 'no':
            print("No hint. Continue...")
        else:   
            hint_index = random.randint(0, num_digits - 1) 
            print("|", end="")
            for _ in range(num_digits):                
                if _ != hint_index:
                    print("_", end="|")
                else:
                    print(pc_code[_], end="|")
            print()
            used_hint = True  
            count += 2          
    elif guess.lower() == 'hint' and used_hint:
        print("Sorry, you have used your hint") 
    elif guess.lower() == 'python' and used_hint:
        used_hint = False  
    elif guess.lower() == 'test':
        flashprint(pc_code, delay=0.5, stay=False, flashes=1)
    elif guess.lower() == 'quit':
        print()
        printing("Exiting game...")
        break
    else:
        print(f"Guess Error, guess must contain {num_digits} distinct numbers")

if guess.lower() != 'quit':
    end = round(time.time() - start)  # Captures end time
    minute, sec = divmod(end, 60)
    second = '{:02d}'.format(sec)
    minute1 = "minute" if minute in [0, 1] else "minutes" 
    second1 = "second" if sec in [0, 1] else "seconds" 
    
    print()
    flashprint("     ***CODE CRACKED***", flashes=4)
    printing(f"Completed in {count} {attempt} and took {minute} {minute1} and {second} {second1}")

    # Saves only the fastest score or time in JSON file  
    if (high_score == 0 or count < high_score):
        records["high_scores"][key] = [player, count]         
    if (best_time == 0 or end < best_time):
        records["best_times"][key] = [player, end]
        
    if (high_score == 0 or count < high_score) and (best_time == 0 or end < best_time): 
        printing(f"MASTER CODE BREAKER!!! {player}, you SMASHED the steps and time records for '{key}'")
    else:
        if high_score == 0 or count < high_score:
            printing(f"**Congratulations {animate}{player}!!! You broke the steps record for '{key}'")  
        if best_time == 0 or end < best_time:
            printing(f"**Congratulations {animate}{player}!!! You broke the time record for '{key}'")         
        
    if (high_score == 0 or count < high_score) or (best_time == 0 or end < best_time):    
        with open(r'xCodeCracker/records.json', 'w') as file:             
            json.dump(records, file, indent = 2, sort_keys=True)  

display_records()