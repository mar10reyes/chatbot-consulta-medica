import Pyro4
import Pyro4.naming


class Server:

    def __init__(self, remote_object):
        self.daemon = Pyro4.Daemon()
        self.uri = self.daemon.register(remote_object)
        ns = Pyro4.locateNS()
        ns.register('remote_object', self.uri)

    def start(self):
        print("running")
        self.daemon.requestLoop()

#ns = Pyro4.locateNS()
# ns.register('obj',uri)

# print(uri)

# daemon.requestLoop()
