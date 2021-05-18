from constants import *

class Checker(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, name="door_to_door_salesperson")


    def find_connections(self):
        for port in range(MIN_PORT, MAX_PORT):
            if port is not Nodes.my_port and port not in Nodes.neighbours:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((HOST, port))
                    request_message = REQUEST + str(Nodes.my_port)
                    s.sendall(request_message.encode(ENCODING))
                    Nodes.neighbours.append(port)
                    print(f"Connected to port {port}")
                    s.shutdown(2)
                    s.close()

                except:
                    pass

        
    def fix_connections(self):
        temp = dict.fromkeys(Nodes.neighbours)
        Nodes.neighbours = list(temp)



    def run(self):
        while True:
            self.find_connections()
            self.fix_connections()