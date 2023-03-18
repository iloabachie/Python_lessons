from main import question_bank

class Ask():
    def ask():
        score = 0
        asked = 0
        for x in question_bank:
            print(x.text)
            ans = input('t or f: ')
            if ans == x.answwer:
                print('right')
                score += 1
                asked +=1
            else:
                print('wrong')
                asked ==1
        print(' yu scored bla bla')
    

# ask questions


# check if answer correct



# check if at end