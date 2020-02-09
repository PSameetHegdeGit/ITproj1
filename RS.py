from Server import Server

RS = Server()  # Not sure why I can't access for input
RS.readDataFromFile("PROJI-DNSRS.txt")

RS.createSocket(5015)  # random port filled
RS.socketBind()
RS.socketAccept()
