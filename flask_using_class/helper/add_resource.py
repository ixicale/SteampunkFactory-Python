
from flask import Flask
def add_endpoint(clase,funcion,metodos=['Get'],flask=Flask(__name__)):
    arr={
        'url_begins':str(clase),
        'url_ends':str(funcion.__name__),
        'methods':metodos,
        'task':funcion,
        'url':str(clase)+str(funcion.__name__),
    }
    print(arr['url'])
    @flask.route(str(arr['url']),endpoint=str(arr['url']), methods=arr['methods'])
    def gen():
        from flask import request
        params = {}
        for value in request.args:
            params[value]=request.args.get(value, default = 1, type = int)
        return arr['task'](params)
