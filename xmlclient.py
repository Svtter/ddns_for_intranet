# coding: utf-8

import xmlrpc.client
from consts import port

s = xmlrpc.client.ServerProxy('http://0.0.0.0:{p}/'.format(p=port))
print(s.update_ip())
