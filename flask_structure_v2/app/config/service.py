#!/usr/bin/env python3.6
from app.config.urlApi import *

import requests
import json


class Service(object):
    def __init__(self):
        self.entorno = application.get("DEV", NotFound)

    """
    @param {string} api
    Metodo para obtener la url donde apunta la api

    @return {json}
    """

    def curl(self, api="", extends="", headers={}):
        url = (self.entorno.get(api, NotFound) + extends)
        r = requests.get(url=url, headers=headers)
        return r.json()
