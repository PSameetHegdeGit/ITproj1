import DomainName
import time
import random

import socket
import sys

'''

This class will define server functionality: 

will contain list of ServerStructure objects, server socket set up, and will specify what level server is @? (as in is it RS or TS)

'''

class Server ():
    '''
        # For now I'll define the serverName
    def __init__(self, serverName):
        self.serverName = serverName

    '''

    domainNameList = []

    def createSocket(self, portno):
        print("Creating a socket\n")
        try:
            global host
            global port
            global serverSocket
            host = ''
            port = portno

            serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        except socket.error as err:
            print('socket could not be opened: {}\n'.format(err))
            exit()

    def socketBind(self):
        try:
            global host
            global port
            global serverSocket
            print("Binding socket to port: " + str(port))

            serverSocket.bind((host, port))
            serverSocket.listen(1)

        except socket.error as err:
            print("Server could not bind: error " + str(err))
            Server.socketBind(self) #trying to include recursion --> idk about syntax

    def socketAccept(self):
        conn, address = serverSocket.accept()
        print("Connection has been establish: @ IP: " + str(address[0]) + " | " + "port: " + str(address[1]))
        Server.commands(self, conn)
        conn.close()


    def commands(self, conn):
        while True:
            client_response = str(conn.recv(1024), "utf-8")
            conn.send(str.encode("Server is working!"))
            print(client_response)

    #Will append the domainInfo into a file
    def appendDNL(self, domainInfo):
        (self.domainNameList).append(domainInfo) #domainInfo is a ServerStructure obj


#First try to create new server, connect with client, and send basic messages back and forth
if __name__ == "__main__":
    newServer = Server() #Not sure why this isn't working
    newServer.createSocket(5009) #random port filled
    newServer.socketBind()
    newServer.socketAccept()


#TODO: Need to keep server running for as many clients I create --> right now server ends when I create a client