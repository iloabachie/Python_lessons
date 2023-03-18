import random
print("welcome to CODE BREAKER")
print("""***Clues***
MATCH: at least one correct digit in the correct position
CLOSE: at least one correct digit but in wrong position
NOPE: no correct digit""")

pc_code = "".join(random.sample([str(_) for _ in [*range(10)]], 3))
# print(pc_code)

match = False
count = 1
guess_cred = True

while True:
    attempt = "attempt" if count == 1 else "attempts" 
    guess = input("\nMake a guess: ")
    
    for _ in guess:
        if _ not in [str(x) for x in [*range(10)]]:
            guess_cred = False
    
    while len(guess) != 3 or not guess_cred:
        guess = input("Invalid guess.\nMake a guess: ")
        guess_cred = True
        for _ in guess:
            if _ not in [str(x) for x in [*range(10)]]:
                guess_cred = False
    
    if guess == pc_code:
        break
    elif pc_code[0] == guess[0] or pc_code[1] == guess[1] or pc_code[2] == guess[2]:
        print(f"MATCH: {attempt}={count}")
    else:
        for _ in pc_code:
            if _ in guess:
                match = True
        if match == True: 
            print(f"CLOSE: {attempt}={count}")
            match = False
        else: 
            print(f"NOPE: {attempt}={count}")  
    count += 1

print(f"CODE CRACKED in {count} {attempt}\n")