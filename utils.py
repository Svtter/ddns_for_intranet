# coding: utf-8

"""load json file & update json file
"""

import json
import threading


def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def write_data(filename, obj):
    with open(filename, 'w') as f:
        json.dump(obj, f)


def change_record(name, ip):
    """
    change record in dns_dict
    """

    # lock for what... wait or not run
    lock = threading.Lock()

    dns_dict = load_data('data.json')
    dns_dict[name] = ip
    write_data('data.json', dns_dict)

    lock.release()
