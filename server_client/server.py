"""
    The server side of the peer to peer network.
    The file deals with sending data to other peers.
"""

from server_client.constants import *

class Server:

    def __init__(self, msg):
        try:
            self.msg = msg

            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            self.connections = []
            self.peers = []

            self.s.bind((HOST, PORT))
            self.s.listen(CAPACITY)

            print("-" * 20 + " Server Running " + "-" * 20)
            print(f"Binded to: {(HOST, PORT)}")

            self.run()

        except Exception as e:
            sys.exit()


    """
        Handles the connections and sending of data to clients.

    """
    def handler(self, connection, addr):
        try:
            while True:
                data = connection.recv(BYTE_SIZE)
                
                for connection in self.connections:
                    #disconnection
                    if data and data.decode(ENCODING)[0].lower() == 'q':
                        self.disconnect(connection, addr)
                        return
                    
                    elif data and data.decode(ENCODING) == REQUEST_STRING:
                        print("-" * 20 + " Uploading " + "-" * 20)
                        connection.send(self.msg)
        
        except Exception as e:
            sys.exit()


    """
        Disconnecting the node
    """
    def disconnect(self, connection, addr):
        self.connections.remove(connection)
        self.peers.remove(addr)
        connection.close()
        self.send_peers()
        print(f"{addr}, disconnected")
        print("-"*80)


    
    """
        Send a list of peers to all connected peers.
    """
    def send_peers(self):
        peer_list = ""
        for peer in self.peers:
            peer_list += str(peer[0]) + ","

        for connection in self.connections:
            data = PEER_BYTE_DIFFERENTIATOR + bytes(peer_list, ENCODING)
            connection.send(data)


    """
        Send a message to all peers.
    """
    def send_message(self):
        try:
            while True:
                msg = input(f"{self}:")
                for connection in self.connections:
                    print("-" * 20 + " Sending Message " + "-" * 20)
                    connection.send(msg.encode(ENCODING))
        
        except Exception:
            pass


    def run(self):
        while True:
            connection, addr = self.s.accept()
            
            self.peers.append(addr)
            print(f"Peers are: {self.peers}")
            self.send_peers()

            c_thread = threading.Thread(target = self.handler, args = (connection, addr))
            c_thread.daemon = True
            c_thread.start()

            self.connections.append(connection)

            print(f"{addr}, connected")
            print("-"*80)

            s_thread = threading.Thread(target = self.send_message)
            s_thread.daemon = True
            s_thread.start()