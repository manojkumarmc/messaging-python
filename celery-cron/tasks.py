from celery.task import task

@task
def multi(x,y):
    mult = x * y
    return "The result is " + str(mult)
