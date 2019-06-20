from helper.base_controller import BaseController


class Component(BaseController):
    """docstring for Component from api 2 flask."""

    def __init__(self):
        super(Component, self).__init__()

    def get(self):
        return self.extends
