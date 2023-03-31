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
        print("Invalid name. Must be max 8 characters and letters only")
        
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
    with open(r'xCodeCracker/records.json', 'r') as file:
        records = json.load(file)
        high_score = records["high_scores"][key][1]
        best_time = records["best_times"][key][1]
except Exception as e:
    high_score = best_time = float('inf')
    
count = 1 # Sets the counter variable for counting steps

def display_records():
    print(f"\n                    **Leader Board**")
    print('+----------+---------------------+---------------------+')
    print('| Game     | Steps Record        | Time Record         |')
    keys = ("two", "three", "four")
    for key in keys:
        try:
            name1, high_score = records["high_scores"][key]  
            name2, best_time = records["best_times"][key]
        except:
            name1 = name2 = "-"
            high_score = best_time = 0
        minute, sec = divmod(best_time, 60) 
        game = key.upper()  
        print('+----------+----------+----------+----------+----------+')
        print('| {:8} | {:8} |       {:2d} | {:8} |    {:2d}:{:02d} |'.format(game, name1, high_score, name2, minute, sec))
    print('+----------+----------+----------+----------+----------+')

display_records()

input("\nPress 'Enter' to start")

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
    else:
        print(f"Guess Error, guess must contain {num_digits} distinct numbers")

end = round(time.time() - start)
minute, sec = divmod(end, 60)
seconds = '{:02d}'.format(sec)
print(f"\n***CODE CRACKED***\nCompleted in {count} {attempt} and took {minute} minute(s) and {seconds} second(s)")

# Saves only the fastest score or time in JSON file
with open(r'xCodeCracker/records.json', 'w') as file:
    if count < high_score:
        high_score = count 
        records["high_scores"][key] = [player, high_score]
        print(f"**Congratulations!!! New steps record for '{key.upper()}'")  
    if end < best_time:
        best_time = end 
        records["best_times"][key] = [player, best_time]
        print(f"**Congratulations!!! New time record for '{key.upper()}'")  
    json.dump(records, file, indent = 2)  

display_records()