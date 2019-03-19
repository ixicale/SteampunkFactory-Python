from test_command import run
from flask import Flask, Response

app = Flask(__name__)
run(app)
