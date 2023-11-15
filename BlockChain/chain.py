from random import choice, randint
import sys, json, time
sys.path.append('BlockChain')
from chain_objects import BlockChain, Trader, Transfer
from fake_data import generate_random_trader

  
    
coin = BlockChain()

user1 = Trader(name='Tony Stark', age=55, location="Canada", deposit=200)
user2 = Trader('Black Panther', 41, 'Wakanda', 2000)
user3 = Trader('Peter Parker', 14, "Narnia", 300)
user4 = Trader('Thanos', 45, 'Knowhere', 5000)


random_traders = [generate_random_trader() for _ in range(25)] + [user1, user2, user3, user4]

for trader in random_traders:
    print(trader)
print('\n+++++++++++++++++++++++++++++++++\n')

for _ in range(15):
    time.sleep(1)
    transfer4 = Transfer(coin, (x:=choice(random_traders)), (y:=choice(random_traders)), randint(100,500), 'For the nft purchase')
    print(x)
    print(y)
    print(*coin.chain, sep='\n')
    print(coin.get_latest_block().time_stamp)
    print(coin.get_latest_block().data)
    print(coin.get_latest_block().previous_hash)
    print(coin.get_latest_block().hash)
    
    print('\n+++++++++++++++++++++++++++++++++\n')

for trader in random_traders:
    print(trader)
    
    

print('\n+++++++++++++++++++++++++++++++++\n')

for _ in range(15):
    time.sleep(1)
    transfer5 = Transfer(coin, generate_random_trader(), generate_random_trader(), randint(100,1000), 'For the nft purchase')

    print(*coin.chain, sep='\n')
    print(coin.get_latest_block().time_stamp)
    print(coin.get_latest_block().data)
    print(coin.get_latest_block().previous_hash)
    print(coin.get_latest_block().hash)
    
    print('\n+++++++++++++++++++++++++++++++++\n')