#!/usr/bin/env python3.6
from flask_restful import Resource
# Sin template


class Test1(Resource):
    def get(self, name):
        x = "test1 " + name
        return x
