import hashlib
import datetime
import json
import time

class Block():
    def __init__(self, data:dict, previous_hash:str, index_num:int) -> None:
        self.index_num = str(index_num)
        self.time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = json.dumps(data, indent=2)
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    
    def calculate_hash(self) -> str:
        combined_data = self.index_num + self.time_stamp + self.data + self.previous_hash
        sha256_hash = hashlib.sha256()
        input_data = combined_data.encode('utf-8')        
        sha256_hash.update(input_data)        
        return sha256_hash.hexdigest()
    
    def __str__(self):
        return f'Block index: {self.index_num}  Block Time: {self.time_stamp}'
    
class BlockChain():
    def __init__(self) -> None:
        self.chain = []
        self.__create_block()
        
    def __create_block(self):
        data = "Genesis block"
        sha256_hash = hashlib.sha256()
        sha256_hash.update(data.encode('utf-8'))
        prev_hash = sha256_hash.hexdigest()
        index_num = len(self.chain)
        first_block = Block(data=data, previous_hash=prev_hash, index_num=index_num)
        self.chain.append(first_block)
    
    def get_latest_block(self):
        return self.chain[-1]    
    
    def add_new_block(self, data:dict):
        index_num = len(self.chain)
        prev_hash = self.chain[-1].hash
        new_block = Block(data=data, index_num=index_num, previous_hash=prev_hash)
        self.chain.append(new_block)
        return new_block
    
class Wallet():
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
    
    def add(self, amount:float):
        self.balance += amount
    
    def subtract(self, amount:float):
        self.balance -= amount


class Trader():
    def __init__(self, name, age=35, location='Multiverse', deposit=0) -> None:
        self.name = name
        self.age = age
        self.location = location
        self.deposit = deposit
        self.wallet = Wallet(self.name, self.deposit)
    

class Transfer():
    def __init__(self, sender:Trader, receiver:Trader, amount:int, reference:str) -> None:
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.reference = reference
        self.__balance_ok = self.sender.wallet.balance >= self.amount  
        if self.__balance_ok:
            self.sender.wallet.subtract(self.amount)
            self.receiver.wallet.add(self.amount)
            self.block_data = {
                'Sender': self.sender.name,
                'Recipient': self.receiver.name,
                'Amount': self.amount,
                'Reference': self.reference
            }
        
        else:
            self.block_data = {
                'Sender': self.sender.name,
                'Recipient': self.receiver.name,
                'Amount': f'Not enough balance to transfer {self.amount}',
                'Reference': self.reference
            }
    
            
    
coin = BlockChain()

user1 = Trader('Tony Stark', 55, "Canada", 2000)
user2 = Trader('Black Panther', 41, 'Wakanda', 2000000)
user3 = Trader('Peter Parker', 14, deposit=300)
user4 = Trader('Thanos', 45, 'Knowhere', 5000)


print(*coin.chain, sep='\n')
print(coin.get_latest_block().time_stamp)
print(coin.get_latest_block().data)
print(coin.get_latest_block().previous_hash)
print(coin.get_latest_block().hash)

time.sleep(1)
print('\n+++++++++++++++++++++++++++++++++\n')


transfer1 = Transfer(user1, user2, 500, 'For my suit')

coin.add_new_block(transfer1.block_data)

print(*coin.chain, sep='\n')
print(coin.get_latest_block().time_stamp)
print(coin.get_latest_block().data)
print(coin.get_latest_block().previous_hash)
print(coin.get_latest_block().hash)

time.sleep(1)
print('\n+++++++++++++++++++++++++++++++++\n')

transfer2 = Transfer(user3, user4, 500, 'For the nft purchase')

coin.add_new_block(transfer2.block_data)

print(*coin.chain, sep='\n')
print(coin.get_latest_block().time_stamp)
print(coin.get_latest_block().data)
print(coin.get_latest_block().previous_hash)
print(coin.get_latest_block().hash)

time.sleep(1)
print('\n+++++++++++++++++++++++++++++++++\n')

transfer3 = Transfer(user1, user4, 500, 'for jack sparrow')
coin.add_new_block(transfer3.block_data)

print(*coin.chain, sep='\n')
print(coin.get_latest_block().time_stamp)
print(coin.get_latest_block().data)
print(coin.get_latest_block().previous_hash)
print(coin.get_latest_block().hash)

print(type(json.loads(json.dumps(transfer3.block_data))))


print('\n+++++++++++++++++++++++++++++++++\n')


user3.wallet.add(500)

transfer2 = Transfer(user3, user4, 500, 'For the nft purchase')

coin.add_new_block(transfer2.block_data)

print(*coin.chain, sep='\n')
print(coin.get_latest_block().time_stamp)
print(coin.get_latest_block().data)
print(coin.get_latest_block().previous_hash)
print(coin.get_latest_block().hash)