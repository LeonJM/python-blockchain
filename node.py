from server_client.constants import *
from server_client.client import Client
from server_client.server import Server

class nodes:
    peers = ['127.0.0.1']


def main():
    
    welcome = "Welcome to CheapCoin".encode(ENCODING)

    while True:
        try:
            print("-" * 20 + " Trying to connect " + "-" * 20)
            time.sleep(SLEEP_TIME)
            flag = 0    #debug
            for peer in nodes.peers:
                print(flag)     #debug
                flag += 1       #debug
                print("debug: line 21 node.py")     #debug
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass

                print("debug: line 29 node.py")     #debug
                try:
                    server = Server(welcome)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass    
            
        except KeyboardInterrupt as e:
            sys.exit(0)


if __name__ == "__main__":
    main()