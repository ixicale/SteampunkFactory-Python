#!/usr/bin/env python3.6
from flask_restful import Api

# # section begins uncoment just for test
# import sys
# sys.path.append("../..")
# # section ends uncoment just for test

from util.factory.endpoint1 import Component
from util.factory.endpoint2 import Device


"----------------------- Se le asignan rutas a las clases importadas"
def endpoints(flask_api):
    flask_api.add_resource(Component, '/factory/ep1')
    flask_api.add_resource(Device, '/factory/ep2')



# # uncoment just for test
# from config.flask import service, run
# if __name__ == '__main__':
#     endpoints(service)
#     run()
# # section ends uncoment just for test
