# coding: utf-8

from xmlrpc.server import SimpleXMLRPCServer
from consts import port


class MyXMLRPCServer(SimpleXMLRPCServer):
    def process_request(self, request, client_address):
        self.client_address = client_address
        return SimpleXMLRPCServer.process_request(
            self, request, client_address)


# Create server
server = MyXMLRPCServer(("localhost", port))
server.register_introspection_functions()


def update_ip():
    try:
        ip = server.client_address
        print('client ip is: ', ip)
        return True
    except:
        return False


server.register_function(update_ip)

# Run the server's main loop
server.serve_forever()
