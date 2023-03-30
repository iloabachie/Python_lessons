'''
This is a fun number game to play
'''

import random
import json
import time
# import sys
# sys.path.append("D:\Documents\Python lessons\AngelaYu\Modulesx")
# from countdown import countdown

print("""\n\nwelcome to CODE BREAKER
      
***CLUES***
MATCH: at least one correct digit in the correct position
CLOSE: at least one correct digit but in wrong position
NOPE: no correct digit in guess""")


while True:
    player = input('\nEnter your name: ')
    if player.isalpha():
        player = player.capitalize()
        break
    else:
        print("Invalid name.  Name must be only letters")
        
        
# To get teh number of digits of pc code
while True:
    num_digits = input("Enter number of digits to crack: ")
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
# pc_code = '12'  # for testing the code

records = {"high_scores": {}, "best_times": {}}

try: # Attempts to open saved file
    with open(r'xPCAP-prep\scores.json', 'r') as file:
        records = json.load(file)
        name1, high_score = records["high_scores"][key]
        name2, best_time = records["best_times"][key]
        seconds = f'0{best_time % 60}' if 0 <= best_time % 60 <= 9 else best_time % 60
        print("\n**Leader Board**")
        print(f"Best steps for {key} = {high_score} set by {name1}")  
        print(f"Best time for {key} = {best_time//60} minute(s) {seconds} second(s) set by {name2}")      
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
seconds = f'0{end % 60}' if 0 <= end%60 <= 9 else end % 60
print(f"\nCODE CRACKED in {count} {attempt} and took {end//60} minute(s) and {seconds} second(s)")

# Saves only the fasted score or time in JSON file
with open(r'xPCAP-prep\scores.json', 'w') as file:
    if count < high_score:
        high_score = count 
        records["high_scores"][key] = [player, high_score]
        print(f"This is a new steps record for '{key}'")  
    if end < best_time:
        best_time = end 
        records["best_times"][key] = [player, best_time]
        print(f"This is a new time record for '{key}'")  
    json.dump(records, file, indent = 2)  


# print(json.dumps(records, indent=3))