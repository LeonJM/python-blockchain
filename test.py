import datetime
import hashlib
import json
from flask import Flask, jsonify

class Blockchain:

    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(proof=100, previous_hash='0') # genesis block

    
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

    
    def proof_of_work(self, previous_proof):
        difficulty = 4
        new_proof = 1
        check_proof = False

        while check_proof is False:
            guess = str(new_proof**2 - previous_proof**2).encode()
            guess_hash = hashlib.sha256(guess).hexdigest()

            if guess_hash[:difficulty] == '0' * difficulty:
                check_proof = True
            else:
                new_proof += 1
    
        return new_proof

    
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()


def mine(blockchain):
    previous_block = blockchain.previous_block()
    
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)

    previous_hash = blockchain.hash(previous_block)
    
    block = blockchain.create_block(proof, previous_hash)
    

if __name__ == '__main__':
    blockchain = Blockchain()

    blockchain.new_transaction('Alice', 'Bob', 40)
    mine(blockchain)

    blockchain.new_transaction('Charlie', 'Bob', 200)
    blockchain.new_transaction('Bob', 'Alice', 320)
    mine(blockchain)

    print(json.dumps(blockchain.chain, indent=4))