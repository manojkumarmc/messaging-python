from celery import Celery

results = []
celery = Celery()
celery.config_from_object('celeryconfig')

for x in range(1,100):
    results.append(celery.send_task("tasks.multi",[x,x]))



