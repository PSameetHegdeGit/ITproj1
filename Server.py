import DomainName
import time
import random

import socket


'''

This class will define server functionality: 

will contain list of ServerStructure objects, server socket set up, and will specify what level server is @? (as in is it RS or TS)

'''

class Server ():

    # For now I'll define the serverName
    def __init__(self, serverName):
        self.serverName = serverName

    domainNameList = []

    def socketSetUp(self, port):
        print("This function creates a socket for server")
        try:
            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as err:
            print('socket could not be opened: {}\n'.format(err))
            exit()

        server_binding = ('', port)
        serverSocket.bind(server_binding)

        serverSocket.listen(1)
        host = socket.gethostname()
        localhost_ip = socket.gethostbyname(host)

        csockid, addr = serverSocket.accept() #csockid = new socket obj that can be used to send and receive data; addr = address of socket on other end of connection (i.e. client); thus return val of accept() is (conn, address)


    #Will append the domainInfo into a file
    def appendDNL(self, domainInfo):
        (self.domainNameList).append(domainInfo) #domainInfo is a ServerStructure obj


#First try to create new server, connect with client, and send basic messages back and forth
if __name__ == "__main__":
    newServer = Server(input("Enter Server Name:"))
    newServer.socketSetUp()
