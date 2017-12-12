from celery import Celery
import time

app = Celery('tasks',broker='pyamqp://localhost//',backend='db+mysql://prettypr_task:prettyprinted@155.254.18.68/prettypr_tasks')

@app.task
def reverse(string):
    time.sleep(10)
    return string[::-1]