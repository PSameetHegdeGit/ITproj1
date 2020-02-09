from Server import Server

TS = Server()  # Not sure why I can't access for input
TS.readDataFromFile("PROJI-DNSTS.txt")

TS.createSocket(5015)  # random port filled
TS.socketBind()
TS.socketAccept()
