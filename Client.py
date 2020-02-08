import threading
import time
import random
import DomainName

import socket

class Client:

    def socketSetUp(self, port):
        try:
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM means "use TCP protocol"
            print("[C]: client socket created")
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit()

        portNo = port #is there a required port for us to use or can we use any port? Also conceptual question: should separate servers have separate ports?
        localhost_addr = socket.gethostbyname(socket.gethostname()) #gethostbyname translates hostname given by socket.gethostname() into IPV4 format

        server_binding = (localhost_addr, portNo)
        clientSocket.connect(server_binding)

    #below function will request hostname from user
    def hostNameRequest(self):
        hostname = input("Enter host name that you would like to find: ")
        return hostname