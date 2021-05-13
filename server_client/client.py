"""
    The client side of the peer to peer network
"""

from server_client.constants import *

class Client:
    
    def __init__(self, addr):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.s.connect((addr, PORT))

        self.previous_data = None

        i_thread = threading.Thread(target = self.send_message)
        i_thread.daemon = True
        i_thread.start()

        print("-" * 20 + " Client Running " + "-" * 20)
        print(f"Connected to: {(HOST, PORT)}")

        while True:
            r_thread = threading.Thread(target = self.receive_message)
            r_thread.start()
            r_thread.join()

            data = self.receive_message()

            if not data:
                print("-" * 20 + "  Server Failed " + "-" * 20)
                break

            elif data[0:1] == PEER_BYTE_DIFFERENTIATOR:
                print("Got Peers")
                self.update_peers(data[1:])

    
    """
        Function to receive messages.
    """
    def receive_message(self):
        try:
            print("Receiving" + "."*15)
            data = self.s.recv(BYTE_SIZE)
            print(data.decode(ENCODING))

            print("\nReceived message on the client side is:")
            if self.previous_data != data:
                #get data
                self.previous_data = data
                print(f"debug: {data}")     #debug

            return data

        except KeyboardInterrupt:
            self.send_disconnect_signal()

    
    """
        Function to update peers.
    """
    def update_peers(self, peers):
        print("debug: bruh what's happening")       #debug
        print(f"debug: {nodes.peers}")
        nodes.peers = str(peers, ENCODING).split(",")[:-1]
        print("debug: " + nodes.peers)      #debug

    
    """
        Function to send message.
    """
    def send_message(self):
        try:
            self.s.send(REQUEST_STRING.encode(ENCODING))

        except KeyboardInterrupt as e:
            self.s.send_disconnect_signal()
            return
    

    def send_disconnect_signal(self):
        print("Disconnected from server")
        self.s.send("q".encode(ENCODING))
        sys.exit()


            
    