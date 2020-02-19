from DomainName import DomainName
import socket
import sys


'''

This class will define server functionality: 

will contain list of ServerStructure objects, server socket set up, and will specify what level server is @? (as in is it RS or TS)

If RS --> Need to find way to pass hostname of TS to RS

'''

class Server ():
    '''
        # For now I'll define the serverName
    def __init__(self, serverName):
        self.serverName = serverName

    '''

    domainNameList = []

    #Below function creates a socket for server
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

    #Below function binds socket to port
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

    #Below function accepts connection from client --> SOCKET SHOULD NOT BE ENDED If connection is dropped
    def socketAccept(self):
        conn, address = serverSocket.accept()
        print("Connection has been establish: @ IP: " + str(address[0]) + " | " + "port: " + str(address[1]))
        try:
            while True:
                client_response = str(conn.recv(1024), "utf-8")
                conn.send(Server.searchDNL(self, client_response).encode('utf-8'))
        except:
            print("Connection has a problem!")
            conn.close()


    #searches list for DNL we
    def searchDNL(self, client_response):
            print("in searchDNL")
            for domainInfo in self.domainNameList:
                if (client_response == domainInfo.hostname):
                    print(domainInfo.hostname)
                    output = "{} {} {}".format(domainInfo.hostname, domainInfo.IP, domainInfo.flag)
                    return output


    #Will append the domainInfo into a file
    def appendDNL(self, domainInfo):
        (self.domainNameList).append(domainInfo) #domainInfo is a ServerStructure obj

    #Reads DNSRS or DNSTS from file
    def readDataFromFile(self, fileName):
        File = open(fileName, "r")
        for line in File:
            tokens = line.split() #This splits line into tokens to be put into domain info
            domainInfo = DomainName(tokens[0], tokens[1], tokens[2]) #This is the domain information
            #print("Domain Info:", domainInfo.hostname, domainInfo.IP, domainInfo.flag)
            Server.appendDNL(self, domainInfo)

        File.close()

#First try to create new server, connect with client, and send basic messages back and forth
if __name__ == "__main__":

    newServer = Server() #Not sure why I can't access for input
    newServer.readDataFromFile("PROJI-DNSRS.txt")

    newServer.createSocket(5015) #random port filled
    newServer.socketBind()
    newServer.socketAccept()

#TODO
'''
1) Need to keep server running for as many clients I create --> right now server ends when I create a client
2) be able to search for client queries and send back to client 
3) Root and TS should be connected
'''
