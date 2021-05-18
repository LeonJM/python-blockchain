from constants import *
from receiver import *
from sender import *
from checker import *


def main():
    Nodes.my_port = int(input("My Port: "))
    
    receiver = Receiver()
    checker = Checker()
    sender = Sender()   #also acts as a user interface

    threads = [
        receiver.start(),
        checker.start(),
        sender.start()
    ]


if __name__ == '__main__':
    main()