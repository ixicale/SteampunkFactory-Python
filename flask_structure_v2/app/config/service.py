#!/usr/bin/env python3.6
from app.config.urlApi import *

class Service(object):
    def __init__(self):
        # Multiple herencia de clases
        super(Service, self).__init__()
        self.entorno = application.get("DEV",NotFound)

    """
        @param {string} api
        Metodo para obtener la url donde apunta la api
        
        @return {string}
    """
    def curl(self, api):
        return self.entorno.get(api, NotFound)
