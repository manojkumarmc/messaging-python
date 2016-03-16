CELERY_IGNORE_RESULTS = True
BROKER_HOST="0.0.0.0"
BROKER_PORT=5672
BROKER_URL="amqp://"
CELERY_RESULT_BACKEND="amqp"
CELERY_IMPORTS=("tasks",)

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    'every-minute' : {
        'task' : 'tasks.multi',
        'schedule' : crontab(),
        'args' : (1,2)
    }
}
