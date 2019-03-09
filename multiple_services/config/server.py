from config.url_api import *

import requests
import json


class Service(object):
    """docstring for Service."""

    def __init__(self):
        super(Service, self).__init__()
        self.entorno = entorno.get("DEV", NotFound)

    def curl(self, api, endpoint):
        print(api, endpoint)
        url = self.entorno.get(
            api,
            ""
        ) + endpoint

        r = requests.get(
            url=url,
            headers=headers
        )
        return r.json()
