# py -m pip install ConsolePrint
# Test codes.  Ensure you have installed the module first using: pip install ConsolePrint

# animate.py
import ConsolePrint.animate as prt

prt.printing("hello this should print letter by letter", delay=0.05, style="letter", stay=True, rev=False)
prt.printing("hello this should print word by word but in reverse", delay=0.05, style="word", stay=True, rev=True)
prt.flashprint("The entire text should flash", blinks=5, delay=0.2, stay=True)
prt.flashtext("The text in  will flash", "UPPER CASE", blinks=5, index=12, delay=0.2)
prt.animate1("This text is animated with #", symbol="#")
prt.animate2("Prints letter by letter but masked with # first", symbol="#", delay=0.05)
prt.text_box("C O D E  B R E A K E R", symbol="#", padding=True, wall=True, align="right")
prt.star_square(8, symbol="@")

# console2file.pt
import ConsolePrint.console2file as file
import calendar

file.startConsoleSave()

print("Printing Calendar")
print(calendar.calendar(2023))

file.endConsoleSave()  

# loading.py
import ConsolePrint.loading as load

load.countdown(5)
print()
load.loading1(20)  
print()
load.loading2(5, 'thinking...')
print()
load.loading3(5)



