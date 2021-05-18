from constants import *

class Sharer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, name="door_to_door_gossiper")
        self.number_of_connections = 0
    
    def share_connections(self):
        if (len(Nodes.neighbours) is not self.number_of_connections):
            self.number_of_connections = len(Nodes.neighbours)
            for port in Nodes.neighbours:
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.connect((HOST, port))
                    share_message = SHARE + str(Nodes.neighbours)
                    s.sendall(share_message.encode(ENCODING))
                    s.shutdown(2)
                    s.close()

                except:
                    pass


    def fix_connections(self):
        temp = dict.fromkeys(Nodes.neighbours)
        Nodes.neighbours = list(temp)


    def run(self):
        while True:
            self.fix_connections()
            self.share_connections() 