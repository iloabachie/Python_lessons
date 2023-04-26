import time

def printing(text, delay=0.05, style='letter'): 
    """printing style"""
    if style.lower() == 'letter':   
        for _ in range(len(text)):
            print(text[:_ + 1], end='\r'), time.sleep(delay)
        print()
    elif style.lower() == 'word':
        text = text.split(' ')
        for _ in range(len(text)):
            print(' '.join(text[:_ + 1]), end='\r'), time.sleep(delay)
        print()
        


match __name__:
    case "__main__": 
        printing("word by word printing for udemezue iloabachie", style='word', delay=0.5)
        printing("letter by letter printing for udemezue iloabachie", delay=0.06)
