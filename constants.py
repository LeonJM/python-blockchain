import socket
import threading
import sys
import time

MIN_PORT = 1
MAX_PORT = 10
BUFF_SIZE = 1024
ENCODING = "utf-8"
CAPACITY = 50
HOST = socket.gethostbyname(socket.gethostname())
REQUEST = "req"
SHARE = "shr"

class Nodes:
    my_port = -1
    neighbours = []


