from flask_restful import Resource
from config.server import Service


class BaseController(Service, Resource):
    """docstring for BaseController."""

    def __init__(self):
        super(BaseController, self).__init__()
