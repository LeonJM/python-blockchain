import datetime
import hashlib
import json
import re

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
        new_proof = 0
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


def main():
    blockchain = Blockchain()
    print("Welcome to Cheapcoin")
    while True:
        command = input("")
        if command == "mine":
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

                print(json.dumps(response, indent = 4))

        elif command == "chain":
                response = {
                    'chain': blockchain.chain
                }

                print(json.dumps(response, indent = 4))

        elif command == "valid":
            valid = blockchain.chain_valid()

            if valid:
                print('The blockchain is valid.')
            else:
                print('The blockchain is NOT valid.')

        elif len(command.split()) == 4:
            command = command.split()
            if command[1] != "send" or not command[3].isnumeric():
                print("not a command")
                continue
            
            blockchain.new_transaction(command[0], command[2], command[3])
            print("transaction put through")

        else:
            print("not a command")
                

if __name__ == "__main__":
    main()