'''
This is a fun number game to play
'''

import random
import json
import time


print("""\n\nwelcome to CODE BREAKER
      
***CLUES***
MATCH: at least one correct digit in the correct position
CLOSE: at least one correct digit but in wrong position
NOPE: no correct digit in guess""")


while True:
    player = input('\nEnter your name: ')
    if player.isalpha() and len(player) <= 8:
        player = player.capitalize()
        break
    else:
        print("Invalid name.  Must be max 8 characters and letters only")
        
        
# To get teh number of digits of pc code
while True:
    num_digits = input(f"\nWelcome {player}, enter number of digits to crack: ")
    if num_digits.isnumeric() and 2 <= int(num_digits) <= 4:
        num_digits = int(num_digits)
        break
    else:
        print("Error. Choose a number between 2 and 4 inclusive")    

# Sets the key value for keeping high score
if num_digits == 2: key = 'two'
if num_digits == 3: key = 'three'
if num_digits == 4: key = 'four'
        
# Picks a random code with the number of specified digits       
pc_code = "".join(random.sample([str(_) for _ in range(10)], num_digits))

records = {"high_scores": {}, "best_times": {}}

try: # Attempts to open saved file
    with open(r'xPCAP-prep\scores.json', 'r') as file:
        records = json.load(file)
        name1, high_score = records["high_scores"][key]
        name2, best_time = records["best_times"][key]
        minute, sec = divmod(best_time, 60)
        print(f"\n**Leader Board for '{key.upper()}'**")
        print("     Steps Record")
        print('+----------+----------+')
        print('| {:8} |       {:2d} |'.format(name1, high_score))
        print('+----------+----------+')
        print("     Time Record")    
        print('+----------+----------+')
        print('| {:8} |    {:2d}:{:02d} |'.format(name2, minute, sec))
        print('+----------+----------+')  
except Exception as e:  # If saved fine not found or other error
    # print(e)
    high_score = best_time = float('inf')
    print(f'\nBest steps and time for {key} digits is not yet attained')
    
count = 1 # Sets the counter variable for counting steps

input("\nPress 'Enter' to start")

start = time.time()  # Sets start time

# Game core
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
    else:
        print(f"Guess Error, guess must contain {num_digits} distinct numbers")

end = round(time.time() - start)
minute, sec = divmod(end, 60)
seconds = '{:02d}'.format(sec)
print(f"\nCODE CRACKED in {count} {attempt} and took {minute} minute(s) and {seconds} second(s)")

# Saves only the fastest score or time in JSON file
with open(r'xPCAP-prep\scores.json', 'w') as file:
    if count < high_score:
        high_score = count 
        records["high_scores"][key] = [player, high_score]
        print(f"**Congratulations!!! New steps record for '{key.upper()}'")  
    if end < best_time:
        best_time = end 
        records["best_times"][key] = [player, best_time]
        print(f"**Congratulations!!! New time record for '{key.upper()}'")  
    json.dump(records, file, indent = 2)  


# print(json.dumps(records, indent=3))