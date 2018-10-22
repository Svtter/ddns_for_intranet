# coding: utf-8

import xmlrpc.client
from consts import port
from utils import filter_name


s = xmlrpc.client.ServerProxy('http://0.0.0.0:{p}/'.format(p=port))


def update_ip(name):
    print('update ip....')
    print(s.update_ip(name))


def query_ip(name):
    print('query ip "{name}" ...'.format(name=name))
    ip, port = s.query_ip(name)
    if ip == "":
        ip = '127.0.0.1'
    print('query ip res: ', ip)
    return ip


if __name__ == '__main__':
    test_name = filter_name('server.test')

    # inter-query
    query_ip(test_name)
    update_ip(test_name)
    query_ip(test_name)
