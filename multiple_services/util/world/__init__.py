#!/usr/bin/env python3.6

import sys
sys.path.append("../..")

from util.world.endpoint1 import Country
from util.world.endpoint2 import City


"----------------------- Se le asignan rutas a las clases importadas"
def endpoints(flask_api):
    flask_api.add_resource(Country, '/world/ep1')
    flask_api.add_resource(City, '/world/ep2')



# # uncoment just for test
# from config.flask import service, run
# if __name__ == '__main__':
#     endpoints(service)
#     run()
