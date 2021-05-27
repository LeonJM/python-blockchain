from constants import *

class Sender(threading.Thread):
 
    def __init__(self):
        threading.Thread.__init__(self, name="messenger_sender")


    def send(self, message):
        for port in Nodes.neighbours:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, port))
            s.sendall(message.encode(ENCODING))
            s.shutdown(2)
            s.close()


    def run(self):
        print("loading... checking neighbours")
        while True:
            if not Nodes.start:
                print("Welcome to the cheapcoin network, you may now begin using the network")
                print(f"Initial connections are ports {Nodes.neighbours}")
                while True:
                    message = input("")
                    if message == "-list neighbours":
                        print(Nodes.neighbours)

                    elif message == "q":
                        sys.exit("Goodbye, thanks for using the cheapcoin network")
                        
                    else:
                        self.send(message)


@atexit.register
def goodbye():
    for port in Nodes.neighbours:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, port))
        disconnect_message = QUIT + str(Nodes.my_port)
        s.sendall(disconnect_message.encode(ENCODING))
        s.shutdown(2)
        s.close()