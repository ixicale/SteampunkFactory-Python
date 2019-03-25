from config.flask import service, run
from util.world import endpoints as world_api
from util.factory import endpoints as factory_api

if __name__ == '__main__':
    world_api(service)
    factory_api(service)
    run()
