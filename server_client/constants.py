"""
    The constants of the program.
"""

import socket
import threading
import sys
import time
from random import randint

CAPACITY = 50
SLEEP_TIME = 1
BYTE_SIZE = 1024
HOST = '127.0.0.1'
PORT = 5000
PEER_BYTE_DIFFERENTIATOR = b'\x11'
REQUEST_STRING = "req"
ENCODING = "utf-8"