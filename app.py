# coding: utf-8

from flask import Flask, request, abort, jsonify
from utils import change_record

app = Flask(__name__)


@app.route('/update_ip', methods=['POST'])
def update_ip():
    if request.methods == 'POST':
        name = request.json['name']
        ip = request.remote_addr

        change_record(name, ip)

        return jsonify({'name': name,
                        'ip': ip})

    abort(400)


if __name__ == '__main__':
    app.run()
