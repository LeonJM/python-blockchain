from constants import *

class Receiver(threading.Thread):
 
    def __init__(self):
        threading.Thread.__init__(self, name="messenger_receiver")
        self.daemon = True


    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, Nodes.my_port))
        sock.listen(CAPACITY)

        while True:
            connection, client_address = sock.accept()

            try:
                full_message = ""

                while True:
                    data = connection.recv(BUFF_SIZE)
                    full_message = full_message + data.decode(ENCODING)

                    if data:
                        if full_message[:3] == REQUEST:
                            port = int(full_message[3:])
                            Nodes.neighbours.append(port)
                            print(f"Connection received from port {port}")
                            break
                        
                        if full_message[:1] == QUIT:
                            port = int(full_message[1:])
                            if port in Nodes.neighbours:
                                Nodes.neighbours.remove(port)
                            print(f"Disconnected from port {port}")   
                            break                         
                        
                        elif data:
                            print("{}: {}".format(client_address, full_message.strip()))
                            break

            finally:
                connection.shutdown(2)
                connection.close()


    def run(self):
        self.listen()
 



          

