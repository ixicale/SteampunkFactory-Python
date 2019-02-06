from flask import (Flask, jsonify, abort, request,
					render_template,make_response,
					copy_current_request_context,
					url_for, redirect,)
import json
from json import dumps
import pandas as pd
import os
#instalar paqeteria sudo pip3 install xlsxwriter

app = Flask(__name__)
PORT = 8052
DEBUG = True

@app.errorhandler(404)
def not_found(error):
	return jsonify( generate_response(404, error = 'Resource not found') )

@app.errorhandler(400)
def bad_request(error):
	return jsonify( generate_response(400, error = 'Bad request') )

@app.errorhandler(422)
def unprocessable_entity(error):
	return jsonify( generate_response(422, error = 'Unprocessable Entity') )

#-------------------------------------------------------------------------------

@app.route('/')
def index():
	os.system('clear')
    html=render_template('ixacale.html')
    print(html)
	return render_template('ixacale.html')


def generate_response(status = 200, data = None, error = None):
	return {'status': status, 'data': data, 'error': error  }

if __name__ == '__main__':
	#initialize()
	app.run(port = PORT, debug = DEBUG)
