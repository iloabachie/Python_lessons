def pass_gen():
    import random
    a = random.randint(13,18) #int(input("pasword length: "))
    b = 4 #int(input('how many symbols: '))
    c = 4 #int(input('how many numbers: '))
    d = (a - (b + c)) // 4 #int(input('how many upper: '))
    big_let = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sma_let = 'abcdefghijklmnopqrstuvwxyz'
    number = '1234567890'
    symbol = '!@#$%^&*'
    pass_word = ''
    
    for _ in range(d):
        ran_let = random.randint(0, 25)
        pass_word = pass_word + big_let[ran_let]
    for _ in range(a-(b+c+d)):
        ran_let = random.randint(0, 25)
        pass_word = pass_word + sma_let[ran_let]
    for _ in range(b):
        ran_symbol = random.randint(0, 7)
        pass_word = pass_word + symbol[ran_symbol]
    for _ in range(c):
        ran_num = random.randint(0, 9)
        pass_word = pass_word + number[ran_num]
    mix = list(pass_word)
    random.shuffle(mix)
    password = ''.join(mix)
    return password
