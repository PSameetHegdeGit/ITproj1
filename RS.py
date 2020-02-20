from Server import Server

if __name__ == "__main__":

    RS = Server()  # Not sure why I can't access for input
    RS.readDataFromFile("PROJI-DNSRS.txt")

    RS.createSocket(5017)  # random port filled
    RS.socketBind()
    RS.socketAccept()
