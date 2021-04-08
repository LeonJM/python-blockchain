from constants import *

class Server:

    def __init__(self, msg):
        try:
            self.msg = msg

            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            self.connections = []
            self.peers = []

            self.s.bind((HOST, PORT))
            self.s.listen(1)

            print("-"*20 + "Server Running" + "-"*20)
            self.run()
        
        except Exception as e:
            print("Exception: " + e)
            self.exit()

        
        def handler(self, connection, addr):
            while True:
                connection, addr = self.s.accept()

                self.peers.append(addr)
                print("Peers: {}".format(self.peers))

                self.send_peers()

                c_thread = threading.Thread(target=self.handler, args=(connection, addr))
                c_thread.daemon = True
                c_thread.start()

                self.connections.append(connection)
                print("Connections: {}".format(addr))

                print("-"*100)


        def send_peers(self):
            peer_list = ""

            for peer in self.peers:
                peer_list = peer_list + str(peer[0]) + ","

            for connection in self.connections:
                connection.send(PRE_PEER_BYTE + bytes(oeer_list, 'utf-8'))