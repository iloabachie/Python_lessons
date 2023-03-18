import random
small = 15
medium = 20
large = 25

pepper_small = 2
pepper_lar = 3
cheese = 1
price = 0

welcome = input(
    'welcome to pizza purchase. Press enter to proceed or Type help for assistance\n>> ').upper()

# size = random.choice(['s', 'm', 'l', 'z']).upper()
# extras = random.choice(['y', 'n']).upper()
# melt_cheese = random.choice(['y', 'n']).upper()

if welcome == 'HELP':
    print(f'follow instrutions and type s for small, m for mediium, l for large\nand y for yes and n for no.')
    size = input('What size of pizza do you want?\n>>  ').upper()
    extras = input('Would you like pepperoni?\n>> ').upper()
    melt_cheese = input("How about some cheese?\n>> ").upper()
else:
    size = input('What size of pizza do you want?\n>>  ').upper()
    extras = input('Would you like pepperoni?\n>> ').upper()
    melt_cheese = input("How about some cheese?\n>> ").upper()

if size == 'S':
    price += small
elif size == 'M':
    price += medium
elif size == 'L':
    price += large

print(price)
if price == 0:
    print("your input is incorrect start over")

else:
    if extras == 'Y':
        if size == 'S':
            price += pepper_small
        else:
            price += pepper_lar

    if melt_cheese == 'Y':
        price += cheese

print(
    f'the price for\nsize = {size}, peperoni = {extras} & cheese = {melt_cheese} is ${price}')
