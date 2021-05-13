import socket
import threading
import time
import datetime
import sys

ENCODING = "utf-8"
MIN_PORT = 2000
MAX_PORT = 2005
NODE_CAPACITY = 50
#HOST = socket.gethostbyname(socket.gethostname())
HOST = '127.0.0.1'
SOCKS = []


class Receiver(threading.Thread):

    def __init__(self, my_port):
        threading.Thread.__init__(self, name="receiver")
        self.my_port = my_port


    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, self.my_port))
        sock.listen(NODE_CAPACITY)

        while True:
            time.sleep(1)
            print("receiver says hello")
            # conn, addr = sock.accept()
            # message = ""
            # try: 
            #     while True:
            #         data = conn.recv(16)
            #         message += data.decode(ENCODING)
            #         if not data:
            #             print(f"{addr}: {message.strip()}")
            #             break
            # finally:
            #     conn.shutdown(2)
            #     conn.close()


class Sender(threading.Thread):

    def __init(self):
        threading.Thread.__init__(self, name="sender")


    def run(self):
        while True:
            time.sleep(1)
            print("sender saying sup")
            # message = input("")
            # if message == "quit":
            #     sys.exit(1)
            # if message: 
            #     for sock in SOCKS:
            #         sock.sendall(message.encode(ENCODING))


class Helper(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self, name="helper")

    
    def create_socket(self, port_number):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.connect((HOST, port_number))
        return sock


    def run(self):
        while True:
            for port_number in range(MIN_PORT, MAX_PORT):
                try:
                    SOCKS.append(self.create_socket(port_number))
                    print("-"*30+"NEW CONNECTION"+"-"*30)
                    print(port_number)
                except Exception:
                    pass


def main():
    my_port = 2000 + int(input("Enter port: "))
    receiver = Receiver(my_port)
    sender = Sender()
    helper = Helper()

    print(f"Welcome to fakecoin, you are on port {my_port}")

    thread = [
        receiver.start(),
        sender.start(),
        helper.start()
    ]
    

if __name__ == "__main__":
    main()

    

    
