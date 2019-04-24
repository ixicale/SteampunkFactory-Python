from flask import Flask,request,Response
from helper.add_resource import add_endpoint
from workers.ichigo import sasuke

trabajador = sasuke()
default = Flask(__name__)

# @default.route('/', methods=['GET'])
def exit():
    'Display registered routes'
    rules = []
    for rule in default.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        rules.append((rule.endpoint, methods, str(rule)))
    for endpoint, methods, rule in sorted(rules):
        route = '{:50s} {:25s} {}'.format(endpoint, methods, rule)
        print(route)

    print("\n\n")
    str1 = ' \n<br/>'.join(( endpoint+" => "+methods+"("+rule+")" ) for endpoint, methods, rule in rules)
    return str1

add_endpoint(clase=trabajador,funcion=trabajador.ejemplo_funcion, metodos=['post','get'],flask=default)
add_endpoint(clase=trabajador,funcion=trabajador.ejemplo_funcion2, metodos=['post','get'],flask=default)
default.run(host='0.0.0.0', debug='1', port='9002')
print()
