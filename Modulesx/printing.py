import time

def printing(text, delay=0.05, style='letter', new_line=True, rev=False): 
    """animated text printing"""
    match rev:
        case False:
            if style.lower() == 'letter':   
                for _ in range(len(text)):
                    print(text[:_ + 1], end='\r')
                    time.sleep(delay)    
            elif style.lower() == 'word':
                text = text.split(' ')
                for _ in range(len(text)):
                    print(' '.join(text[:_ + 1]), end='\r')
                    time.sleep(delay)
        case True:
            if style.lower() == 'letter':  
                for _ in range(len(text)):
                    print(text[-1 - _:], end='\r')
                    time.sleep(delay)
            elif style.lower() == 'word':
                text = text.split(' ')
                for _ in range(len(text)):
                    print(' '.join(text[-1 - _:]), end='\r')
                    time.sleep(delay)
    if new_line: print()
        
def prt(text):
    for x in text:
        print(x, end="", flush=True)
        time.sleep(0.05)


# Code test
match __name__:
    case "__main__": 
        texts = "CLOSE: at least one correct digit but in wrong position"
        printing("word by word printing for udemezue iloabachie", style='word', delay=0.5, rev=True)
        printing("letter by letter prin#####\b\b\b\b\bting for udemezue iloaba\bchie with new line false", 0.06, 'letter', False, True)
        print()        
        prt("CLOSE: at least one correct digit but in wrong position")
        print()
        printing(texts, rev=True)



