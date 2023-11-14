import hashlib

class MyBlockChain:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.tansaction_list = transaction_list
        
        self.block_data = "-".join(transaction_list) + "\n-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
    

t1 = "Anna sends 4 NC to Ezue"
t2 = "Bob sends 2.1 NC to Daniel"
t3 = "Daniel sends 2 NC to Mike"
t4 = "Rob sends 0.2 NC to Mike"
t5 = "Nastiia sends 5 NC to Anna"
t6 = "John sends 6 NC to Mike"
t7 = "Bill sends 3 NC to Julia"
t8 = "Julia sends 2 NC to Mike"

initial_block = MyBlockChain("Empty", [t1])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = MyBlockChain(initial_block.block_hash, [t2, t3])

print(second_block.block_data)
print(second_block.block_hash)

third_block = MyBlockChain(initial_block.block_hash, [t4, t5, t6, t7])

print(third_block.block_data)
print(third_block.block_hash)