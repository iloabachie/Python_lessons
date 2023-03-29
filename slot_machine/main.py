

def deposit():
    amount = input('insert deposit: ')
    


def scroll():
    import time
    options = [*range(20)]
    while True:
        t = 0.01
        for _ in options * 10:
            print(_ if len(str(_)) == 2 else f'0{_}', end='\r')
            time.sleep(t)
        t = 0.1
        for _ in options * 8:
            print(_ if len(str(_)) == 2 else f'0{_}', end='\r')
            time.sleep(t)
        t = 0.6
        for _ in options * 3:
            print(_ if len(str(_)) == 2 else f'0{_}', end='\r')
            time.sleep(t)
        t = 0.9
        for _ in options * 1:
            print(_ if len(str(_)) == 2 else f'0{_}', end='\r')
            time.sleep(t)
        t = 1.3
        break

scroll()