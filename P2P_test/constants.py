import socket
import threading
import sys
import time

HOST = '127.0.0.1'
PORT = 5050
PRE_PEER_BYTE = b'\x11'