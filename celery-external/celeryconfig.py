CELERY_IGNORE_RESULTS = True
BROKER_HOST="0.0.0.0"
BROKER_PORT=5672
BROKER_URL="amqp://"
CELERY_RESULT_BACKEND="amqp"
CELERY_IMPORTS=("tasks",)
