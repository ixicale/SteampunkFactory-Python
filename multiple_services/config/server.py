from config.url_api import *

import requests
import json


class Service(object):
    """docstring for Service."""

    def __init__(self):
        super(Service, self).__init__()
        self.entorno = entorno.get("DEV", NotFound)
        self.extends = ("testing controller: " +
                        self.__class__.__name__.lower())
    def curl(self, api, endpoint, headers):
        print("\nAPI =>", api, "\nENDPOINT =>", endpoint, "\nHEADERS =>", headers)
        url = self.entorno.get(
            api,
            ""
        ) + endpoint

        r = requests.get(
            url=url,
            headers=headers
        )
        return r.json()
