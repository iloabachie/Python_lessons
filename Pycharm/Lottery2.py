import random


def cls():
    from os import system
    return system('cls')


cls()


ticket = True
while ticket:
    lot_type = input(
        'Which game, m for Max, 6 for 649 or g for Grand:\n> ').lower()
    ticket_number = int(
        input('How many tickets do you need:\n> '))

    if lot_type == 'm':
        number_of_random = 7
        min_range = 1
        max_range = 50
    elif lot_type == '6':
        number_of_random = 6
        min_range = 1
        max_range = 49
    elif lot_type == 'g':
        number_of_random = 5
        min_range = 1
        max_range = 49
    else:
        number_of_random = 5
        min_range = 1
        max_range = 3
        print('Enter m for Max, 6 for 649 or g for Grand')

    if (max_range - min_range + 1) < number_of_random:
        print('Input Error')
    else:
        print("The lucky numbers are: ")
        lot_array = []
        for x in range(ticket_number):
            lottery = []

            while (len(lottery) < (number_of_random)):
                num1 = random.randint(min_range, max_range)
                if num1 in lottery:
                    num1 = random.randint(min_range, max_range)
                else:
                    lottery.append(num1)
                    lottery.sort()

            lot_array.append(lottery)
            if number_of_random == 5:
                grand = list(str(random.randint(1, 7)))
                grand[0] = int(grand[0])
                print(f'>> {lottery} and grand number is {grand}')
            else:
                print(f'>> {lottery}')
        print(f' here is {lot_array} with {len(lot_array)} tickets')
        # super_ticket = []
        # sum = 0
        # for tic in lot_array:
        #     for numb in tic:
        #         sum += numb
        #     average = sum/len(lot_array)
        #     super_ticket.append(average)
    correct = True
    while correct:
        cont = input(
            'Do you want to generate another ticket?\nEnter y for yes or n for no\n> ').lower()
        if cont == 'y':
            ticket = True
            correct = False
        elif cont == 'n':
            ticket = False
            correct = False
        else:
            print('Invalid answer...')
print('Hope you win with one of them... :)')
