from helper.base_controller import BaseController


class Endpoint1(BaseController):
    """docstring for Endpoint1."""

    def __init__(self):
        super(Endpoint1, self).__init__()

    def get(self):
        return self.entorno
