import random
import json
import time

print("""welcome to CODE BREAKER
      
***Clues***
MATCH: at least one correct digit in the correct position
CLOSE: at least one correct digit but in wrong position
NOPE: no correct digit in guess""")

# To get teh number of digits of pc code
while True:
    num_digits = input("\nEnter number of digits to crack: ")
    if num_digits.isnumeric() and 2 <= int(num_digits) <= 5:
        num_digits = int(num_digits)
        break
    else:
        print("Error. Choose a number between 2 and 5 inclusive")    

# sets the key value for keeping high score
if num_digits == 2: key = 'two'
if num_digits == 3: key = 'three'
if num_digits == 4: key = 'four'
if num_digits == 5: key = 'five'
        
# Picks a random code with the number of specified digits       
pc_code = "".join(random.sample([str(_) for _ in range(10)], num_digits))
# pc_code = '12'  # for testing the code


# When code is run for the first time, it sets the records object
records = {"high_scores": {}, "best_times": {}}

# sets the counter variable for counting steps
count = 1

try: # Attempts to open saved file
    with open(r'xPCAP-prep\scores.json', 'r') as file:
        records = json.load(file)
        high_score = records["high_scores"][key]
        best_time = records["best_times"][key]
        seconds = f'0{best_time % 60}' if 0 <= best_time % 60 <= 9 else best_time % 60
        print(f"\nBest steps for {key} = {high_score}")  
        print(f"\nBest time for {key} = {best_time//60} minutes {seconds} seconds")      
except Exception as e:  # If saved fine not found or other error
    print(e)
    high_score = best_time = float('inf')
    print(f'\nBest steps and time for {key} digits is not yet attained')
    records = {"high_scores": {}, "best_times": {}}
    
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
        print("Input Error")
end = round(time.time() - start)
seconds = f'0{end % 60}' if 0 <= end%60 <= 9 else end % 60
print(f"\nCODE CRACKED in {count} {attempt} and took {end//60} minutes and {seconds} seconds")


with open(r'xPCAP-prep\scores.json', 'w') as file:
    if count < high_score:
        high_score = count 
        records["high_scores"][key] = high_score
        print(f"This is a new steps record for {key}\n")  
    if end < best_time:
        best_time = end 
        records["best_times"][key] = best_time
        print(f"This is a new time record for {key}\n")  
    json.dump(records, file)  


# print(records)