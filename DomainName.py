class DomainName:

    #Below are the instance variables to classes --> have object lvl scope (can be used in all below functions)
    def __init__(self, hostname, IP, flag):
        self.hostname = hostname
        self.IP = IP
        self.flag = flag

    #IDK why I added the below stuff, felt like this class was a bit empty
    def lookupHostname(self):
        return self.hostname

    def lookupIP(self):
        return self.IP

    def lookupFlag(self):
        return self.lookupFlag