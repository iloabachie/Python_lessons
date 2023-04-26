import random
import json
import time
import os

os.system('clear')

print("\n{:^57}".format('Welcome to CODE BREAKER')), time.sleep(1.3)
print("""=========================================================
                    ***CLUES***
MATCH: at least one correct digit in the correct position
CLOSE: at least one correct digit but in wrong position
NOPE:  no correct digit in guess
========================================================="""), time.sleep(1)

# Captures player name
while True:
    player = input('\nEnter your name: ')
    if player.isalpha() and len(player) <= 8:
        player = player.capitalize()
        break
    else:
        print("Invalid name. Must be max 8 characters and letters only")
        
# To get the number of digits of the Code to crack
while True:
    num_digits = input(f"\nWelcome {player}, enter number of digits to crack: ")
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

def display_records():
    print("\n{:>34}".format('**Leader Board**'))
    print('+----------+' + '---------------------+' * 2)
    print('| {:8} | {:19} | {:19} |'.format('Game', 'Steps Record', 'Time Record'))
    keys = ("TWO", "THREE", "FOUR")
    for key in keys:
        try:
            name1, high_score = records["high_scores"][key]
            name2, best_time = records["best_times"][key]
        except:
            name1 = name2 = "--"
            high_score = best_time = 0
        minute, sec = divmod(best_time, 60)  
        print('+----------' * 5 + '+')
        print('| {:8} | {:8} |{:9d} | {:8} |{:6d}:{:02d} |'.format(key, name1, high_score, name2, minute, sec))
    print('+----------' * 5 + '+\n')

def printing(text, delay=0.05):
    for _ in range(len(text)):
        print(text[:_ + 1], end='\r'), time.sleep(delay)
    print()

display_records()   
    
game_on = input("Press 'Enter' to start or type 'reset' to clear score record: ")  # Ensures that timer only starts counting when player is ready

if game_on.lower() == 'reset':
    confirm = input("Are you sure? y or n: ")
    if confirm == 'y':
        keys = ("TWO", "THREE", "FOUR")
        for rkey in keys:
            records["high_scores"][rkey] = ['--', 0]
            records["best_times"][rkey] = ['--', 0]
        with open(r'xCodeCracker/records.json', 'w') as file:
            json.dump(records, file, indent=2, sort_keys=True)
        print('Records cleared...')     
    else:
        print('\nRecords unchanged')
    display_records()    
        
else:
    # Game core
    start = time.time()  # Sets start time
    while True:
        attempt = "attempt" if count == 1 else "attempts" 
        guess = input(f"\nMake a {num_digits}-digit number guess: ")    
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
        elif guess.lower() == 'quit':
            print("\nExiting game...")
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
                printing(f"**Congratulations {player}!!! You broke the steps record for '{key}'")  
            if best_time == 0 or end < best_time:
                best_time = end 
                records["best_times"][key] = [player, best_time]
                printing(f"**Congratulations {player}!!! You {also}broke the time record for '{key}'")  
            json.dump(records, file, indent = 2, sort_keys=True)  

    display_records()