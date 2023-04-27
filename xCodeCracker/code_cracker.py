import random
import json
import time
import os

os.system('cls')

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

print()
for _ in range(3):
    if _ == 0: printing("{:^57}".format('Welcome to CODE BREAKER'), new_line=False, rev=True), time.sleep(0.3)
    if _ == 0: print(" " * 57, end='\r'), time.sleep(0.2)
    print("{:^57}".format('Welcome to CODE BREAKER'), end='\r'), time.sleep(0.5)
    if _ != 2: print(" " * 57, end='\r'), time.sleep(0.2)
print()
print("=" * 57), time.sleep(0.1)
print("{:^57}".format("***CLUES***")), time.sleep(0.1)
print("MATCH: at least one correct digit in the correct position"), time.sleep(0.1)
print("CLOSE: at least one correct digit but in wrong position"), time.sleep(0.1)
print("NOPE:  no correct digit in your guess"), time.sleep(0.1)
print("=" * 57, end='\r'), time.sleep(0.1)
print(" " * 57, end='\r'), time.sleep(0.2)
print("=" * 57 + "\n"), time.sleep(1)

# Captures player name
printing('Enter your name: ', new_line=False)
while True:
    player = input('Enter your name: ')
    if player.isalpha() and len(player) <= 8:
        player = player.capitalize()
        print()
        animate = '#' * len(player) + '\b' * len(player)
        printing(f'Welcome Code Breaker {animate}{player}    ')
        break
    else:
        print("Invalid name. Must be max 8 characters and letters only\n")
        
# To get the number of digits of the Code to crack
while True:
    num_digits = input("\nEnter number of digits to crack: ")
    if num_digits.isnumeric() and 2 <= int(num_digits) <= 4:
        num_digits = int(num_digits)
        break
    else:
        print("Error. Choose a number between 2 and 4 inclusive")    

# Sets the key value for keeping high score
match num_digits:
    case 2: key = 'TWO'
    case 3: key = 'THREE'
    case 4: key = 'FOUR'

# Picks a random code with the number of specified digits       
pc_code = "".join(random.sample([str(_) for _ in range(10)], num_digits))

# Sets the dictionary of the records for first time play
records = {"high_scores": {}, "best_times": {}}

try: # Attempts to extract the records dictionary from JSON file
    with open(r'xCodeCracker/records.json', 'r') as file:
        records = json.load(file)
        high_score = records["high_scores"][key][1]
        best_time = records["best_times"][key][1]
except Exception:
    # Sets high score and best time to infinity if record does not exist or JSON file absend
    high_score = best_time = float('inf') 

count = 1 # Sets the counter variable for counting steps
used_hint = False

def display_records():
    print("\n{:>34}".format('**Leader Board**')), time.sleep(0.05)
    print('+----------+' + '---------------------+' * 2), time.sleep(0.05)
    print('| {:8} | {:19} | {:19} |'.format('Game', 'Steps Record', 'Time Record')), time.sleep(0.05)
    keys = ("TWO", "THREE", "FOUR")
    for key in keys:
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

display_records()  

reset = input("Would you like to reset the Leader board? y or n: ") 

if reset.lower() == 'y':
    confirm = input("Are you sure? y or n: ")
    if confirm == 'y':
        keys = ("TWO", "THREE", "FOUR")
        for rkey in keys:
            records["high_scores"][rkey] = ['--', 0]
            records["best_times"][rkey] = ['--', 0]
        with open(r'xCodeCracker/records.json', 'w') as file:
            json.dump(records, file, indent=2, sort_keys=True)
        print('Records cleared...') 
        display_records() 
    else:
        print('\nRecords unchanged')
    

# Game core
game_on = input("\nPress 'Enter' to start Code Cracking: ")  # Ensures that timer only starts counting when player is ready

start = time.time()  # Sets start time
while True:
    attempt = "attempt" if count == 1 else "attempts" 
    guess = input(f"\nMake a {num_digits}-digit number guess or type hint or quit: ")    
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
        hint_index = random.randint(0, num_digits - 1) 
        print("|", end="")
        for _ in range(num_digits):                
            if _ != hint_index:
                print("_", end="|")
            else:
                print(pc_code[_], end="|")
        print()
        used_hint = True            
    elif guess.lower() == 'hint' and used_hint:
        print("Sorry, you have used your hint")                
    elif guess.lower() == 'quit':
        print()
        printing("Exiting game...")
        break
    else:
        print(f"Guess Error, guess must contain {num_digits} distinct numbers")

if guess.lower() != 'quit':
    end = round(time.time() - start)  # Captures end time
    minute, sec = divmod(end, 60)
    seconds = '{:02d}'.format(sec)
    print(f"\n***CODE CRACKED***\nCompleted in {count} {attempt} and took {minute} minute(s) and {seconds} second(s)")

    # Saves only the fastest score or time in JSON file    
    with open(r'xCodeCracker/records.json', 'w') as file:
        also = "ALSO " if (high_score == 0 or count < high_score) and (best_time == 0 or end < best_time) else ""
        if high_score == 0 or count < high_score:
            high_score = count 
            records["high_scores"][key] = [player, high_score]
            printing(f"**Congratulations {animate}{player}!!! You broke the steps record for '{key}'")  
        if best_time == 0 or end < best_time:
            best_time = end 
            records["best_times"][key] = [player, best_time]
            printing(f"**Congratulations {animate}{player}!!! You {also}broke the time record for '{key}'")  
        json.dump(records, file, indent = 2, sort_keys=True)  

display_records()