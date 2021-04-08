from server import Server
from client import Client
from constants import *

class p2p:
    peers = [HOST]


def main():

    msg = "hello from main"

    while True:
        try:
            print("-" * 30 + "Trying to connect" + "-" * 30)
            # sleep a random time between 1 -5 seconds
            time.sleep(2)
            for peer in p2p.peers:
                try:
                    client = Client(peer)
                except KeyboardInterrupt:
                    sys.exit(0)
                except:
                    pass


                # become the server
                try:
                    server = Server(msg)
                except KeyboardInterrupt:
                    sys.exit()
                except:
                    pass

        except KeyboardInterrupt as e:
            sys.exit(0)

if __name__ == "__main__":
    main()

