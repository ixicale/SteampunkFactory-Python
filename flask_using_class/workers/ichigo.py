from cool_class import cooler

class sasuke(cooler):
    """docstring for sasuke."""
    def __init__(self):
        super(sasuke, self).__init__()
        self.builder(__file__)

    def ejemplo_funcion(self,params={}):
        return ("hola")

    def ejemplo_funcion2(self,params={}):
        return ("hola2")
