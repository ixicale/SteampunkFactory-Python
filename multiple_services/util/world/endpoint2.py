from helper.base_controller import BaseController


class City(BaseController):
    """docstring for City from api 1."""

    def __init__(self):
        super(City, self).__init__()

    def get(self):
        return self.extends
