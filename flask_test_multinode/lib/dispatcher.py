# Clases importadas
from lib.controller.url1 import Test1
from lib.controller.url2 import Test2


from flask import Flask
from flask_restful import Api

# inicia flask y le asigna la ubicación de la carpeta con los templates
app = Flask(__name__, template_folder='../templates')
# se inicializa api para que recupere todas las clases que pueden usar flask
api = Api(app)

# se le asignan rutas a las clases importadas
# Controlador con metodos que simulan Get, Post, Put, Del
api.add_resource(Test1, '/t1/<string:name>')
api.add_resource(Test2, '/t2/<string:name>')  # Route_2
