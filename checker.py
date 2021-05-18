from constants import *

class Checker(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, name="door_to_door_salesperson")

    def run(self):
        while True:
            for port in range(MIN_PORT, MAX_PORT):
                if port is not Nodes.my_port and port not in Nodes.neighbours:
                    try:
                        print(f"Checking port {port}")
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((HOST, port))
                        print(f"Succesfully connected to (HOST,{port})")
                        Nodes.neighbours.append(port)
                        s.shutdown(2)
                        s.close()

                    except:
                        pass
                        
            print(f"Neighbouring ports: {Nodes.neighbours}")