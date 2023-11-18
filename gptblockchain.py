import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

    def calculate_hash(self):
        data_str = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}"
        return hashlib.sha256(data_str.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(0, "0", time.time(), "Genesis Block", self.calculate_hash(0, "0", time.time(), "Genesis Block"))
        self.chain.append(genesis_block)

    def add_block(self, data):
        index = len(self.chain)
        previous_hash = self.chain[-1].hash
        timestamp = time.time()
        hash = self.calculate_hash(index, previous_hash, timestamp, data)
        new_block = Block(index, previous_hash, timestamp, data, hash)
        self.chain.append(new_block)

    def calculate_hash(self, index, previous_hash, timestamp, data):
        data_str = f"{index}{previous_hash}{timestamp}{data}"
        return hashlib.sha256(data_str.encode()).hexdigest()

# Example usage:
if __name__ == "__main__":
    # Create a blockchain
    my_blockchain = Blockchain()

    # Add blocks to the blockchain
    my_blockchain.add_block("Block 1 Data")
    my_blockchain.add_block("Block 2 Data")
    my_blockchain.add_block("Block 3 Data")

    # Print the blockchain
    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print("\n")
