from celery import Celery

app = Celery('tasks',broker='pyamqp://localhost//')

@app.task
def reverse(string):
    return string[::-1]