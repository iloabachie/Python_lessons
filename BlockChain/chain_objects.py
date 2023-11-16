import hashlib
import datetime
import json

class Block():
    def __init__(self, data:dict, previous_hash:str, index_num:int) -> None:
        self.index_num = str(index_num)
        self.time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data = json.dumps(data, indent=2)
        self.previous_hash = previous_hash
        self.hash = self.__calculate_hash(self.index_num, self.time_stamp, self.data, self.previous_hash)
    
    def __str__(self):
        return f'Block index: {self.index_num}  Block Time: {self.time_stamp}'
    
    def __repr__(self):
        return f"Block({self.data}, {self.previous_hash}, {self.index_num})"
    
    def __calculate_hash(self, index_num, time_stamp, data, previous_hash) -> str:
        combined_data = index_num + time_stamp + data + previous_hash
        sha256_hash = hashlib.sha256()
        input_data = combined_data.encode('utf-8')        
        sha256_hash.update(input_data)        
        return sha256_hash.hexdigest()
    
class BlockChain():
    def __init__(self) -> None:
        self.chain = []
        self.__create_block()
    
    def __str__(self):
        return f'Block chain of {len(self.chain)} blocks'
    
    def __repr__(self):
        return "BlockChain()"
        
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
    
    def chain_integrity(self):
        compromised = []
        for ind in range(len(self.chain) - 1, 0, -1):
            try:
                assert self.chain[ind].previous_hash == self.chain[ind - 1].hash == self.chain[ind - 1]._Block__calculate_hash(self.chain[ind - 1].index_num, self.chain[ind - 1].time_stamp, self.chain[ind - 1].data, self.chain[ind - 1].previous_hash)
            except AssertionError:
                compromised.append(ind)
            else:
                continue
        return compromised if compromised else True
            
class Wallet():
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
    
    def add(self, amount:float):
        self.balance += amount
    
    def subtract(self, amount:float):
        self.balance -= amount


class Trader():
    def __init__(self, name:str, age:int, location:str, deposit:float=0) -> None:
        self.name = name
        self.age = age
        self.location = location
        self.deposit = deposit
        self.wallet = Wallet(self.name, self.deposit)
    
    def __str__(self):
        return f'{self.name=}, {self.age=}, {self.wallet.balance=}'
    
class Transfer():
    def __init__(self, chain:BlockChain, sender:Trader, receiver:Trader, amount:int, reference:str) -> None:
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.reference = reference
        self.chain = chain
        if (ind:=chain.chain_integrity()) is True:
            if self.sender.wallet.balance >= self.amount:
                self.sender.wallet.subtract(self.amount)
                self.receiver.wallet.add(self.amount)
                self.block_data = {
                    'Sender': self.sender.name,
                    'Recipient': self.receiver.name,
                    'Amount': f'Successful {self.amount}',
                    'Reference': self.reference
                }        
            else:
                self.block_data = {
                    'Sender': self.sender.name,
                    'Recipient': self.receiver.name,
                    'Amount': f'Insufficient funds {self.amount}',
                    'Reference': self.reference
                } 
            self.chain.add_new_block(self.block_data)
        else:
            print(f'\033[31mBlock index {ind} is compromised\n\033[0m')