from helper.base_controller import BaseController

"""
    This class support default functions like get, post, put, etc.
    Check documentation of flask_restful for more details!
    https://flask-restful.readthedocs.io/en/latest/
"""
class City(BaseController):
    """docstring for City from api 1."""

    def __init__(self):
        super(City, self).__init__()

    def get(self):
        return self.extends
