import Pyro4

#ns=Pyro4.locateNS()
#uri = ns.lookup('obj')
#o=Pyro4.Proxy(uri)

class RMIClient:

    def __init__(self, server_uri):
        self.server_uri = server_uri

    def set_server_uri(self):
        self.server_uri = input("Ingrese la URI: ")

    def connect(self):
        remote_object = Pyro4.Proxy(self.server_uri)
        return remote_object
