# Clases importadas
from app.controller.aController import PageTestController
from app.controller.testController import TestController


from flask import Flask
from flask_restful import Api

# inicia flask y le asigna la ubicación de la carpeta con los templates
app = Flask(__name__, template_folder='../templates')
# se inicializa api para que recupere todas las clases que pueden usar flask
api = Api(app)

# se le asignan rutas a las clases importadas
# Controlador con metodos que simulan Get, Post, Put, Del
api.add_resource(PageTestController, '/pagetestcontroller')
api.add_resource(TestController, '/')
