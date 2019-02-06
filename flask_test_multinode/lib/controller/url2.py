
from flask_restful import Resource
from flask import render_template
# Con template


class Test2(Resource):
    def get(self, name):
        titulo = "GeekyFlask"
        usuario = {'nombre': name}
        print(usuario)
        return render_template('index.html',
                               titulo=titulo, usuario=usuario)
