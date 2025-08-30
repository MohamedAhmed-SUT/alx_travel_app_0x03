# Celery settings
CELERY_BROKER_URL = "amqp://localhost"   # RabbitMQ broker
CELERY_RESULT_BACKEND = "rpc://"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
