# py -m pip install ConsolePrint

import ConsolePrint.printing as prt
import ConsolePrint.console2file as file
import ConsolePrint.loading as load

file.startConsoleSave()

from calendar import calendar

print(calendar(2023))

file.endConsoleSave()



prt.printing("hello this should print letter by letter", delay=0.05, style="letter", new_line=True, rev=False)
prt.flashprint("The entire text should flash", flashes=5, delay=0.2, stay=True)
prt.flashtext("The text in  will flash", "UPPER CASE", blinks=5, index=12, delay=0.2)
prt.animate1("This text is animated with #", symbol="#")
prt.animate2("Prints letter by letter but masked with # first", symbol="#", delay=0.5)
load.countdown(5)
load.loading1(10)
print()
load.loading2(10)
print()
load.loading3(10)







