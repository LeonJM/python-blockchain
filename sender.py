from constants import *

class Sender(threading.Thread):
 
    def __init__(self):
        threading.Thread.__init__(self, name="messenger_sender")


    def run(self):
        while True:
            message = input("")
            for port in Nodes.neighbours:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((HOST, port))
                s.sendall(message.encode(ENCODING))
                s.shutdown(2)
                s.close()
