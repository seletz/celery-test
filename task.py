import time
from celery.task import task

@task
def add(x, y):
    logger = add.get_logger()
    logger.info("sleeping ...")
    time.sleep(5)
    logger.info("waking up.")
    return x + y

