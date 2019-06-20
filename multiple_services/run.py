from config.flask import service, run
'importing all endpoints from each api'
'you can deploy just one or a lot from here'
from util.world import endpoints as world_api
from util.factory import endpoints as factory_api

if __name__ == '__main__':
    'call all endpoints from each __init__.py file'
    world_api(service)
    factory_api(service)

    'run() execute all app with possible tags (like -h for help)'
    run()
# from helper.base_controller import BaseController
# x = BaseController()
# print(x)
