#!/usr/bin/env python3.6
from flask import Flask
from flask_restful import Api

__all__ = ["run", "service"]

app = Flask(__name__, template_folder='../templates')

# inicia flask y le asigna la ubicación de la carpeta con los templates
service = Api(app)


from optparse import OptionParser


def run(host=None, debug=None, port=None):

    parser = OptionParser(usage='usage: %prog [options] ')

    parser.add_option("-H",  "--host",
        default="127.0.0.1" if host is None else host,
        type="str",
        dest="host"
    )

    parser.add_option("-D",  "--debug",
        default=True if debug is None else debug,
        dest="debug"
    )

    parser.add_option("-P",  "--port",
        type="int",
        default=9000 if port is None else port,
        dest="port"
    )

    (options, args) = parser.parse_args()
    # print(options)

    app.run(
        debug=options.debug,
        host=options.host,
        port=int(options.port)
    )
