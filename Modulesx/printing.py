import time

def printing(text, delay=0.05, style='letter', new_line=True): 
    """printing style"""
    if style.lower() == 'letter':   
        for _ in range(len(text)):
            print(text[:_ + 1], end='\r')
            time.sleep(delay)
        if new_line: print()
    elif style.lower() == 'word':
        text = text.split(' ')
        for _ in range(len(text)):
            print(' '.join(text[:_ + 1]), end='\r')
            time.sleep(delay)
        if new_line: print()
        


match __name__:
    case "__main__": 
        printing("word by word printing for udemezue iloabachie", style='word', delay=0.5)
        printing("letter by letter printing for udemezue iloabachie", delay=0.06)


        printing("{:^57}".format('Welcome to CODE BREAKER')), time.sleep(1.3)
        printing("""=========================================================
                            ***CLUES***
        MATCH: at least one correct digit in the correct position
        CLOSE: at least one correct digit but in wrong position
        NOPE:  no correct digit in guess
        ========================================================="""), time.sleep(1)