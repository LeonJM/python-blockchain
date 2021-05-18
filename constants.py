import socket
import threading
import sys
import time

MIN_PORT = 1
MAX_PORT = 5
BYTE_SIZE = 1024
ENCODING = "utf-8"
CAPACITY = 50
HOST = '127.0.0.1'      #to be changed to the network host later
REQUEST = "req"

class Nodes:
    my_port = -1
    neighbours = []

