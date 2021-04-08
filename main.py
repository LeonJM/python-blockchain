import datetime
import hashlib
import json
from flask import Flask, jsonify, request

class Blockchain:

    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        block = self.create_block(proof=100, previous_hash='0')    # genesis block
        print(json.dumps(block, indent=4))
        self.difficulty = 4    # difficulty for proof of work

    
    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain),
            'timestamp': str(datetime.datetime.now()),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        self.pending_transactions = []
        return block

    
    def new_transaction(self, sender, recipent, amount):
        self.pending_transactions.append({
            'sender': sender,
            'recipent': recipent,
            'amount': amount
        })
    

    def previous_block(self):
        return self.chain[-1]


    def algorithm(self, new_proof, previous_proof):
        return str(new_proof**2 - previous_proof**2)    # algorithm inside of str can be anything the developer wants  

    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False

        while check_proof is False:
            guess = self.algorithm(new_proof, previous_proof).encode()
            guess_hash = hashlib.sha256(guess).hexdigest()

            if guess_hash[:self.difficulty] == '0' * self.difficulty:
                check_proof = True
            else:
                new_proof += 1
    
        return new_proof

    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    
    def chain_valid(self):
        previous_block = self.chain[0]
        block_index = 1

        while block_index < len(self.chain):
            block = self.chain[block_index]

            #checks if leading block contains correct previous hash field
            if block['previous_hash'] != self.hash(previous_block):
                return False
            
            #checks if the proof of work is valid
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(self.algorithm(proof, previous_proof).encode()).hexdigest()
            if hash_operation[:self.difficulty] != '0' * self.difficulty:
                return False

            previous_block = block
            block_index += 1

        return True         

'''
def mine(blockchain):
    time = datetime.datetime.now()
    previous_block = blockchain.previous_block()
    
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)

    previous_hash = blockchain.hash(previous_block)
    
    blockchain.new_transaction('God', 'Miner', 1)
    block = blockchain.create_block(proof, previous_hash)
    print(json.dumps(block, indent=4))
    print(f"time taken: {datetime.datetime.now() - time}")
    

if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.new_transaction('Alice', 'Bob', 40)
    mine(blockchain)

    blockchain.new_transaction('Charlie', 'Bob', 200)
    blockchain.new_transaction('Bob', 'Alice', 320)
    mine(blockchain)

    blockchain.new_transaction('Charlie', 'Alice', 500)
    blockchain.new_transaction('Charlie', 'Alice', 100)
    blockchain.new_transaction('Charlie', 'Bob', 100)
    blockchain.new_transaction('Charlie', 'Dave', 100)
    blockchain.new_transaction('Dave', 'Alice', 40)
    mine(blockchain)

    print(f"\n{blockchain.chain_valid()}")
'''

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

blockchain = Blockchain()

@app.route('/')
def start():
    response = 'Welcome to fakecoin'

    return response, 200

'''
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    print(values)

    return 'test', 201
'''


@app.route('/mine', methods=['GET'])
def mine():
    previous_block = blockchain.previous_block()

    previous_proof = previous_block['proof']
    current_proof = blockchain.proof_of_work(previous_proof)

    previous_hash = blockchain.hash(previous_block)

    blockchain.new_transaction('God', 'Miner', 1)
    block = blockchain.create_block(current_proof, previous_hash)

    response = {
        'message': 'MINED',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
        'hash': blockchain.hash(block)
    }

    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def chain():
    response = {
        'chain': blockchain.chain,
    }

    return jsonify(response), 200


@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid()

    if valid:
        return 'The blockchain is valid.'
    else:
        return 'The blockchain is NOT valid.'


app.run(host='127.0.0.1', port=5000)