from helper.base_controller import BaseController


class Device(BaseController):
    """docstring for Device from api 2 flask."""

    def __init__(self):
        super(Device, self).__init__()

    def get(self):
        return self.extends
