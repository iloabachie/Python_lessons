# Import the modules
import hashlib
import json
import time
import requests
from flask import Flask, jsonify, request
from urllib.parse import urlparse

# Define the blockchain class
class Blockchain:

    def __init__(self):
        # Initialize the chain, the transactions, and the nodes
        self.chain = []
        self.transactions = []
        self.nodes = set()
        # Create the genesis block
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        # Create a new block with the given proof and previous hash
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        # Clear the current transactions
        self.transactions = []
        # Add the block to the chain
        self.chain.append(block)
        return block

    def get_previous_block(self):
        # Return the last block in the chain
        return self.chain[-1]

    def validate_block(self, block, previous_block):
        # Check if the index, previous hash, and proof of a block are valid
        return (block['index'] == previous_block['index'] + 1 and
                block['previous_hash'] == self.hash(previous_block) and
                block['proof'] == self.proof_of_work(previous_block['proof']))

    def add_block(self, block):
        # Add a block to the chain if it is valid
        previous_block = self.get_previous_block()
        if self.validate_block(block, previous_block):
            self.chain.append(block)
            return True
        return False

    def proof_of_work(self, previous_proof):
        # Find a proof that satisfies the hash-based puzzle
        new_proof = 1
        check_proof = False
        while check_proof is False:
            # Calculate the hash of the proof
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            # Check if the hash starts with four zeros
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        # Return the hash of a block
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        # Check if the chain is valid
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            # Check if the block is valid
            if not self.validate_block(block, previous_block):
                return False
            previous_block = block
            block_index += 1
        return True

    def add_transaction(self, transaction):
        # Add a transaction to the current transactions
        self.transactions.append(transaction)
        # Return the index of the block that will contain the transaction
        return self.get_previous_block()['index'] + 1

    def add_node(self, address):
        # Add a node to the network
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        # Replace the chain with the longest and valid chain in the network
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        # Iterate over all the nodes in the network
        for node in network:
            # Get the chain of the node
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                # Get the length and the chain
                length = response.json()['length']
                chain = response.json()['chain']
                # Check if the length is greater and the chain is valid
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        # Replace the chain if a longer and valid chain is found
        if longest_chain:
            self.chain = longest_chain
            return True
        return False

# Define the transaction class
class Transaction:

    def __init__(self, sender, receiver, amount):
        # Initialize the sender, receiver, and amount
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def create_transaction(self):
        # Create a transaction with the given sender, receiver, and amount
        transaction = {
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount
        }
        return transaction

    def validate_transaction(self, transaction):
        # Check if the transaction is valid
        return (transaction['sender'] != transaction['receiver'] and
                transaction['amount'] > 0)

# Create an instance of the blockchain
blockchain = Blockchain()

# Create a Flask app
app = Flask(__name__)

# Create an endpoint to mine a new block
@app.route('/mine_block', methods=['GET'])
def mine_block():
    # Get the previous block and its proof
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    # Find a new proof
    proof = blockchain.proof_of_work(previous_proof)
    # Get the previous hash
    previous_hash = blockchain.hash(previous_block)
    # Create a new block
    block = blockchain.create_block(proof, previous_hash)
    # Create a response
    response = {
        'message': 'Congratulations, you just mined a block!',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200

# Create an endpoint to get the chain
@app.route('/get_chain', methods=['GET'])
def get_chain():
    # Get the chain
    chain = blockchain.chain
    # Create a response
    response = {
        'chain': chain,
        'length': len(chain)
    }
    return jsonify(response), 200

# Create an endpoint to check the validity of the chain
@app.route('/is_valid', methods=['GET'])
def is_valid():
    # Check the validity of the chain
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    # Create a response
    if is_valid:
        response = {'message': 'The chain is valid.'}
    else:
        response = {'message': 'The chain is not valid.'}
    return jsonify(response), 200

# Create an endpoint to add a transaction
@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    # Get the request data
    json = request.get_json()
    # Check if the data has the required fields
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in json for key in transaction_keys):
        return 'Some elements of the transaction are missing', 400
    # Create a transaction
    transaction = Transaction(json['sender'], json['receiver'], json['amount']).create_transaction()
    # Validate the transaction
    if not Transaction(json['sender'], json['receiver'], json['amount']).validate_transaction(transaction):
        return 'Invalid transaction', 400
    # Add the transaction to the current transactions
    index = blockchain.add_transaction(transaction)
    # Create a response
    response = {'message': f'This transaction will be added to Block {index}'}
    return jsonify(response), 201

# Create an endpoint to connect a new node
@app.route('/connect_node', methods=['POST'])
def connect_node():
    # Get the request data
    json = request.get_json()
    # Check if the data has the required field
    nodes = json.get('nodes')
    if nodes is None:
        return 'No node', 400
    # Add the nodes to the network
    for node in nodes:
        blockchain.add_node(node)
    # Create a response
    response = {
        'message': 'All the nodes are now connected.',
        'total_nodes': list(blockchain.nodes)
    }
    return jsonify(response), 201

if __name__ == '__main__':
    app.run()