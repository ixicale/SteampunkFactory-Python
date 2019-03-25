#!/usr/bin/env python3.6
# Resources
from app.helper import BaseController


class PageTestController(BaseController):

    def __init__(self):
        super(PageTestController, self).__init__()

    def get(self, name):
        data = self.curl(api=name)
        return data
