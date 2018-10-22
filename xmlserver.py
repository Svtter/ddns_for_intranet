# coding: utf-8

from xmlrpc.server import SimpleXMLRPCServer
from consts import port

ip_dict = {}


class MyXMLRPCServer(SimpleXMLRPCServer):
    def process_request(self, request, client_address):
        self.client_address = client_address
        return SimpleXMLRPCServer.process_request(
            self, request, client_address)


# Create server
server = MyXMLRPCServer(("localhost", port))
server.register_introspection_functions()


def update_ip(name):
    try:
        ip = server.client_address
        ip_dict[name] = ip
        print('client ip is: ', ip)
        return True
    except BaseException as e:
        print(e)
        return False


def query_ip(name):
    try:
        print('query ip {name}'.format(name=name))
        ip = ip_dict[name]
        return ip
    except BaseException as e:
        print(e)
        return "0.0.0.0", 80


server.register_function(update_ip)
server.register_function(query_ip)

# Run the server's main loop
server.serve_forever()
