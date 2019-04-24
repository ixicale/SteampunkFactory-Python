from flask import Flask,request,Response
from helper.add_resource import add_endpoint
from workers.ichigo import sasuke

trabajador = sasuke()



default = Flask(__name__)
add_endpoint(clase=trabajador,funcion=trabajador.ejemplo_funcion, metodos=['post','get'],flask=default)
add_endpoint(clase=trabajador,funcion=trabajador.ejemplo_funcion2, metodos=['post','get'],flask=default)
default.run(host='0.0.0.0', debug='1', port='9002')
