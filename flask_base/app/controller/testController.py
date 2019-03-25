#!/usr/bin/env python3.6
# Resources
from app.helper.BaseController import BaseController

class TestController(BaseController):
    def __init__(self):
        super(TestController,self).__init__()

    def get(self):
        print(self.extends)
        return(self.extends)
