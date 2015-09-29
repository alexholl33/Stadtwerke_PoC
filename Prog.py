__author__ = 'AHolland'
from celery import Celery

app = Celery('Prog', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

