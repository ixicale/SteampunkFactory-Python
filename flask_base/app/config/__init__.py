# Llama todas las clases(recursos) importadas en el __init__ de la carpeta controller
from app.controller import flask_api as my_resources


from flask import Flask

# inicia flask y le asigna la ubicación de la carpeta con los templates
servicio = Flask(__name__, template_folder='../templates')

my_resources(servicio)
