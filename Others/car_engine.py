from tracemalloc import start

if_start = "Car started... Ready to Go!!!"
if_stop = "Car stopped"
if_quit = "Exiting now..."
if_else = "Invalid command, type 'help' for asistance"
command = ""
started = False

print("***Welcome to your COROLLA***")
print("""
                        _..-------++._
                    _.-'/ |      _||  \ --._
            __.--'`._/_\j_____/_||___\    `----.
        _.--'_____    |          \     _____    /
    _j    /,---.\   |        =o |   /,---.\   |_
    [__]==// .-. \ ==`===========/==// .-. \ =[__]
        `-._|\ `-' /|___\_________/___|\ `-' /|_.'     hjw
            `---'                     `---'
""")

while True:
    command = input("> ").upper()
    if command == "START":
        if started == False:
            print(if_start)
            started = not started
        else:
            print("Engine already running!!!")
    elif command == "STOP":
        if started == True:
            print(if_stop)
            started = not started
        else:
            print("Engine already stopped!!!")
    elif command == "HELP":
        print("""Type:
Start - to start the car 
Stop - to stop the car
Quit - to turn off engine""")
    elif command == "QUIT":
        if started == True:
            print('Stop the engine first')
        else:
            print(if_quit)
            break
    else:
        print(if_else)
print("***Ensure you fold your side mirrors!!!***")
