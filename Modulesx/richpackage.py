# test rich by typing in terminal: py -m rich

from rich.console import Console  # py -m pip install rich  
from time import sleep

console = Console()

for i in range(5):
    console.print(f"Frame {i}")
    sleep(0.5)
    console.clear()



console = Console()

for i in range(5):
    console.print(f"[bold red]{i}[/bold red]")
    sleep(0.5)
    console.clear()
    
    

from rich.syntax import Syntax

code = """def greet(name):
    print(f"Hello, {name}!")

greet("world")"""

syntax = Syntax(code, "python", theme="monokai", line_numbers=True)

console.print(syntax)


from rich.console import Console
from time import sleep

console = Console()

for i in range(5):
    console.print(f"[bold red]{i}[/bold red]")
    sleep(0.5)
    console.clear()


from rich.console import Console
from rich.text import Text

console = Console()

text = Text("This text is underlined.")
# text.underlined = True

console.print(text)


a = "{:^57}".format("***CLUES***")

print(a)