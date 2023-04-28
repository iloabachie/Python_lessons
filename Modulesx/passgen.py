def pass_gen(length=15, symbol=4, numbers=4):
    import random
    a = random.randint(13,18) #int(input("pasword length: "))
    a = length
    b = symbol
    c = numbers
    d = (a - (b + c)) // 4 # uppercase letters
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

if __name__ == "__main__":
    print(pass_gen(21))
    print(pass_gen())
