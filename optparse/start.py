from test_command import run
from flask import Flask, Response

app = Flask(__name__)


if __name__ == '__main__':
    run(app)
