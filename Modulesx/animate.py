import time
import os
from formats import *
# import shutil
# terminal_width, terminal_height = shutil.get_terminal_size()


if __name__ == "__main__":
    os.system('cls')
    print((terminal_size:=os.get_terminal_size()))
    print(f'{terminal_size.columns = }, {terminal_size.lines = }')
    print()

terminal_width = os.get_terminal_size().columns

def printing(text: str, delay=0.05, style='letter', stay=True, rev=False, color=reset):
    """Prints text to console letter by letter or word by word"""
    print(color, end='\r')
    text = text.strip()
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
    if stay:
        print()
    print(reset, end='\r')


def flashprint(text: str, blinks=5, delay=0.2, stay=True, color=reset):
    """Gets printed output to blink"""
    print(color, end='\r')
    text = text.strip()
    for _ in range(blinks):
        print(text, end='\r'), time.sleep(delay)
        print(' ' * len(text), end='\r'), time.sleep(delay)
    if stay:
        print(text)
    print(reset, end='\r')


def flashtext(phrase: str, text: str, index='end', blinks=5, delay=0.2, color=reset):
    """Hilights key word by flashing it"""
    print(color, end='\r')
    text = text.strip()
    phrase = phrase.strip()
    textb = ' ' * len(text)
    if index == 'end':
        phrase1 = phrase
        phrase2 = ''
    else:
        phrase1 = phrase[:index]
        phrase2 = phrase[index:]

    for _ in range(blinks):
        print(phrase1 + text + phrase2, end='\r')
        time.sleep(delay)
        print(phrase1 + textb + phrase2, end='\r')
        time.sleep(delay)
    print(phrase1 + text + phrase2)
    print(reset, end='\r')


def animate1(text: str, symbol="#", color=reset):
    """Flashing masked text to transition to flasing text"""
    print(color, end='\r')
    text = text.strip()
    symbol = len(text) * symbol
    flashprint(symbol, blinks=3, stay=False)
    flashprint(text, blinks=2, stay=True)
    print(reset, end='\r')


def animate2(text: str, symbol="#", delay=0.05, color=reset):
    """Reveals all characters text by text but first masked then flashes"""
    print(color, end='\r')
    text = text.strip()
    symbol = len(text) * symbol
    for _ in symbol + "\r" + text + "\r":
        print(_, end="", flush=True)
        time.sleep(delay)
    flashprint(text, blinks=2, stay=True, color=color)
    print(reset, end='\r')

def text_box(text: str, symbol="#", padding: bool=False, wall: bool=True, align="center", color=reset):
    """Prints text in a box of symbols.
If the align parameter is a number then the box is indented by the number count"""
    print(color, end='\r')
    text = text.strip()
    end = 5 if padding else 3
    text_row = 3 if padding else 2
    length = len(text) + 8
    left_border = text_row - 1  if padding else text_row
    right_border = text_row + 1 if padding else text_row
    
    if align == "left": indent = 0
    elif align == "right": indent = terminal_width - length
    elif align == "center": indent = terminal_width//2 - length//2
    elif isinstance(align, int) and align <= (terminal_width - length): indent = align
    else: raise Exception(f"Error in the align argument: {align=}")  
    
    for row in range(1, end + 1):
        for col in range(1, length + 1):
            if col == 1:
                print(reset + (" " * indent) + color, end="")
            if row == 1 or row == end or col == 1 or col == length:
                if wall:
                    print(symbol, end="")
                else:
                    if left_border <= row <= right_border:
                        print(" ", end="") 
                    else:
                        print(symbol, end="")
            elif row == text_row:
                if col == 3:
                    print("{:^{}}".format(text, length-2), end="")
            else:
                print(" ", end="")  
            if col == length:
                print()
    print(reset, end='\r')
                
                
def star_square(num: int, symbol: str="#", align: str='center', flush: bool=True, color=reset):
    print(color, end='\r')
    if num < 5 or num > terminal_width or not isinstance(num, int):
        raise Exception(f"Invalid square size. Number must be an integer greater than 4 and less than the terminal width: {terminal_width}")
    elif align == 'center':
        indent = reset + (' ' * (terminal_width//2 - num//2)) + color
    elif align == 'right':
        indent = reset + (' ' * (terminal_width - num)) + color
    elif align == 'left':
        indent = ''  
    elif isinstance(align, int) and terminal_width - align > num:
        indent = reset + (" " * align) + color
    else:
        raise Exception("Align parameter is invalid")    
          
    for row in range(1, num + 1):
        # time.sleep(0.04)
        print(indent, end="")
        for col in range(1, num + 1):
            if flush: time.sleep(0.04)                
            if row == 1 or col == 1 or row == num or col == num:
                print(symbol, end="", flush=flush)
            elif row == col:
                print(symbol, end="", flush=flush)
            elif row + col == num + 1:
                print(symbol, end="", flush=flush)  
            else:
                print(" ", end="", flush=flush)              
            if col == num:
                print()
    print(reset, end='\r')
    

def format(text: str, align: str="left", underscore: bool=False, color=reset):
    print(color, end='\r')
    text = text.strip()
    length = len(text)
    
    if align == 'center':
        indent = ' ' * (terminal_width//2 - length//2)
    elif align == 'right':
        indent = ' ' * (terminal_width - length)
    elif align == 'left':
        indent = ''
    else:
        raise Exception("Align argument error") 
    print(indent + text)
    if underscore:
        print(indent + '*' * length)
    print(reset, end='\r')
    

# Code test
if __name__ == "__main__":
    printing("hello this should print letter by letter      ", delay=0.05, style="letter", stay=True, rev=False, color=magenta)
    printing("hello this should print word by word but in reverse", delay=0.3, style="word", stay=True, rev=True, color=red)
    flashprint("The entire text should flash", blinks=5, delay=0.2, stay=True, color=green)
    flashtext("The text in  will flash", "UPPER CASE", blinks=5, index=12, delay=0.2, color=yellow)
    animate1("This text is animated with #", symbol="#", color=white)
    animate2("Prints letter by letter but masked with # first  ", symbol="#", delay=0.05, color="\033[48;5;150m")
    text_box("C O D E  B R E A K E R", symbol="#", padding=True, wall=True, align='right', color='\033[48;5;4m')
    star_square(10, symbol="@", align=15, flush="True", color="\033[104m")
    format('\n\n\n  udemezue is going to become a programmer one day  ', align='center', underscore=True, color=cyan)
    
    


