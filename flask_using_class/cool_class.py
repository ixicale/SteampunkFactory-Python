#!/usr/bin/env python3.6
# from main.config.service import Service

class cooler(object):
# class cooler(Service):
    def __init__(self):
        # Multiple herencia de clases
        super(cooler, self).__init__()
        self.extends = (
            "the controller: " +
            self.__class__.__name__
            ).lower()

    def builder(self,path):
        path_array = (path).split('/')
        folder_name = path_array[-2]
        file_name = path_array[-1].split('.py')[0] #file without extension '.py'

        self.module =('/'+folder_name+'/'+file_name)

    def __str__(self):
        return(self.module+"/"+self.__class__.__name__+'/').lower()

    def __repr__(self):
        return(self.module+"/"+self.__class__.__name__+'/').lower()
