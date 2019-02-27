#!/usr/bin/env python3.6
from flask_restful import Resource
# Resources
from app.config.service import Service

class BaseController(Resource, Service):
    def __init__(self):
        # Multiple herencia de clases
        super(BaseController, self).__init__()
        self.extends = ("testing controller: "+self.__class__.__name__.lower())
        # self.extends = ("testing controller: "+__class__.__name__)

    def get(self):
        return self.extends

    def post(self):
        return self.extends

    def put(self):
        return self.extends
