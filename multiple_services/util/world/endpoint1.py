from helper.base_controller import BaseController


class Country(BaseController):
    """docstring for Country from api 1."""

    def __init__(self):
        super(Country, self).__init__()

    def get(self):
        return self.extends
