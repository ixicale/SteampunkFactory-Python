#!/usr/bin/env python3.6
from flask_restful import Api

# Import all Resources from each class
from app.controller.aController import PageTestController
from app.controller.testController import TestController

"""
Clase donde se declaran los controladores y las rutas que apunta cada controlador
"""


class flask_api(object):

    """
    Se inicializa api para que recupere todas rutas de request
    """

    def __init__(self, flask):
        super(flask_api, self).__init__()
        self.api = self.endpoints(Api(flask))

    """
    Se asignan endpoints a las clases importadas que simulan Get, Post, Put
    """

    def endpoints(self, r):
        r.add_resource(PageTestController, '/pagetestcontroller/<string:name>')
        r.add_resource(TestController, '/')

        return r
