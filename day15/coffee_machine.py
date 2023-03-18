import time
import os
import sys
sys.path.append('D:\\Documents\\Python lessons\\AngelaYu\\Modulesx')
from countdown import *


def clear():    
    return os.system('cls')

clear()

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 0,
    "milk": 0,
    "coffee": 0,
}

coins = {
    'penny': 0,
    'nickel': 0,
    'dime': 0,
    'quarter': 0
}


def coffee_machine(menu, com1, res):
    def check_payment(input, menu, t):
        if t < menu[input]['cost']:
            return [False, round(t, 2)]
        else:
            balance = t - menu[input]['cost']
            return [True, round(balance, 2), round(t, 2)]

    def check_resources(com, res, menu):
        if menu[com]['ingredients']['water'] <= res['water'] and menu[com]['ingredients']['milk'] <= res['milk'] and menu[com]['ingredients']['coffee'] <= res['coffee']:
            return True
        else:
            return False

    def coins_balance(p, n, d, q, bank):
        bank['penny'] += p
        bank['nickel'] += n
        bank['dime'] += d
        bank['quarter'] += q

    def resource_balance(res, com, menu):
        res['water'] -= menu[com]['ingredients']['water']
        res['milk'] -= menu[com]['ingredients']['milk']
        res['coffee'] -= menu[com]['ingredients']['coffee']

    print(f"A cup of {com1} costs ${round((menu[com1]['cost']/100), 2)}")
    print('Insert coins')
    penny = int(input('Penny: '))
    nickel = int(input('Nickel: '))
    dime = int(input('Dime: '))
    quarter = int(input('Quarter: '))
    total = penny * 1 + nickel * 5 + dime * 10 + quarter * 25
    clear()
    print(f'\nYou inserted ${round((total/100), 2)}')
    enough_resources = check_resources(com1, res, menu)
    enough_money = check_payment(com1, menu, total)
    if enough_resources and enough_money[0]:
        clear()
        print(f'\nHere is your coffee...\nYour change is: ${enough_money[1]/100}\n')
        coins_balance(penny, nickel, dime, quarter, coins)
        resource_balance(resources, command, MENU)
    elif enough_resources and not enough_money[0]:
        clear()
        print(f'Not enough funds, here is your refund: ${enough_money[1]/100}')
    elif not enough_resources and enough_money[0]:
        clear()
        print(f'Not enough resources, here is your refund: ${enough_money[2]/100}')
    else:
        clear()
        print(f'Not enough resources or funds. Your refund is: ${enough_money[1]/100}')


on = input('Enter 1 for on or 2 for off:\n>> ')
if on == '1':
    on = True
    loading1(5)
else:
    on = False

while on:
    clear()
    command = input('\nTo choose your preferred coffee\nPick a number from the list below:\n1. Espresso\n2. Latte\n3. Capuccino\n4. Settings\n----------\n>> ')
    loading2(3)
    if command == '4':
        settings_menu = True
        while settings_menu:
            clear()
            settings = input('\nSettings menu\nChoose from below:\na. Refill\nb. Check Quantity\nc. Check Money\nd. Previous menu\ne. Turn off\n----------\n>> ').lower()
            loading2(3)
            if settings == 'e':
                clear()
                confirm = input('Are you sure you want to turn off? y or n:\n>> ').lower()
                if confirm == 'y':
                    on = False
                    break
                else:
                    on = True
            elif settings == 'd':
                settings_menu = not settings_menu
            elif settings == 'c':
                clear()
                for coin in coins:
                    print(f'{coin}: {coins[coin]}')
                penny = coins['penny'] * 1
                nickel = coins['nickel'] * 5
                dime = coins['dime'] * 10
                quarter = coins['quarter'] * 25
                print(
                    f'Amount = ${round(((penny + nickel + dime + quarter)/100), 2)}')
                time.sleep(2)
            elif settings == 'b':
                clear()
                for resource in resources:
                    print(f'{resource}: {resources[resource]}')
                time.sleep(2)
            else:
                clear()
                water = int(input('Water in ml:\n>> '))
                milk = int(input('Milk in ml:\n>> '))
                coffee = int(input('Coffee in g:\n>> '))
                resources['water'] = resources['water'] + water
                resources['milk'] = resources['milk'] + milk
                resources['coffee'] = resources['coffee'] + coffee
                clear()
                print('-------------------------------')
                for resource in resources:
                    print(f'{resource}: {resources[resource]}')
                print('-------------------------------')
                time.sleep(2)
    elif command == '3':
        command = 'cappuccino'
        coffee_machine(MENU, command, resources)
    elif command == '2':
        command = 'latte'
        coffee_machine(MENU, command, resources)
    else:
        command = 'espresso'
        coffee_machine(MENU, command, resources)
    clear()
    print('\n--------------------------------------')
    print(resources)
    print(coins)
    print('--------------------------------------')
    time.sleep(2)
countdown(3)
print('\nTurning off...\nThank you for using our dispenser')
