import sys
import os
sys.path.insert(0, os.getcwd())

BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"
BROKER_VHOST = ""

CELERY_RESULT_BACKEND = "amqp"

CELERY_IMPORTS = ("task", )

