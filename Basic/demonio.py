#!/usr/bin/python3
""" Demonstrating Flask, using APScheduler. """

from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

'Convertir fechas y operaciones con fechas'
from datetime import datetime
from datetime import timedelta


def sensor():
    """ Function for test purposes. """
    print('Hello Job! The time is changed on: ', datetime.now())

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',seconds=2, minutes = 1, hours = 0)
sched.start()

app = Flask(__name__)

@app.route("/home")
def home():
    """ Function for test purposes. """
    return "Welcome Home :) !"

if __name__ == "__main__":
    app.run()