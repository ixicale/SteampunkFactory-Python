#!/usr/bin/env python3.6
from flask_restful import Api
from flask import Flask
import sys
sys.path.append("../..")

from util.report.endpoint1 import Endpoint1

# inicia flask y le asigna la ubicación de la carpeta con los templates
app = Flask(__name__, template_folder='../templates')

service = Api(app)


"----------------------- Se le asignan rutas a las clases importadas"
service.add_resource(Endpoint1, '/')




# ejecuta flask del objeto __init__
def main():
    app.run(port=2323, debug=True)


if __name__ == '__main__':
    main()
