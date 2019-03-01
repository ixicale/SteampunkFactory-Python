#!/usr/bin/env python3.6
# Resources
from app.helper.BaseController import BaseController


class PageTestController(BaseController):

    def __init__(self):
        super(PageTestController, self).__init__()

    def get(self):
        data = self.curl(api="productions", extends="/habilidad/", headers={})

        return data
