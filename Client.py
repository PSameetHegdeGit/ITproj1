import threading
import time
import random
import DomainName

import socket

class Client:

    def createClientSocket(self, port):
        try:
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM means "use TCP protocol"
            print("[C]: client socket created")
        except socket.error as err:
            print('socket open error: {}\n'.format(err))
            exit()

        portNo = port #is there a required port for us to use or can we use any port? Also conceptual question: should separate servers have separate ports?
        localhost_addr = socket.gethostbyname(socket.gethostname()) #gethostbyname translates hostname given by socket.gethostname() into IPV4 format

        try:
            clientSocket.connect((localhost_addr, portNo)) #since both client and server r on same host, localhost_addr should be fine
            print("Client has successfully connected!")
            Client.client_requests(self, clientSocket)
        except:
            print("connection could not be established or has terminated")

        clientSocket.close()
        exit()

    #below function will request hostname from user
    def hostNameRequest(self, clientSocket):
        hostname = input("Enter host name that you would like to find: ")
        return hostname

    def client_requests(self, clientSocket):
        while True:
            request = input("What would you like to request: ")
            if request == "quit":
                return

            clientSocket.send(request.encode('utf-8'))
            server_response = str(clientSocket.recv(1024), "utf-8")
            print(server_response)



if __name__ == "__main__":
    newClient = Client()
    newClient.createClientSocket(int(input("Enter port number of server:")))