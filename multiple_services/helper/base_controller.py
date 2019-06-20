from flask_restful import Resource
from config.server import Service


class BaseController(Service, Resource):
    """docstring for BaseController."""

    def __init__(self):
        super(BaseController, self).__init__()
        self.extends = ("the controller: " + self.__class__.__name__ ).lower()
        # # test section begins, uncoment just for test
        # 'to see the example for __str__ run this class into executing app'
        # self.builder(__file__)
        # # test section ends, uncoment just for test

    def builder(self,path):
        path_array = (path).split('/')
        folder_name = path_array[-2]
        file_name = path_array[-1].split('.py')[0] #file name without extension '.py'

        self.module =('/'+folder_name+'/'+file_name)

    def __str__(self):
        return(self.module+"/"+self.__class__.__name__+'/').lower()

    def __repr__(self):
        return(self.module+"/"+self.__class__.__name__+'/').lower()
