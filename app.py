import time
import celery

app = celery.Celery("app")
app.conf.update(BROKER_HOST="localhost")

@app.task
def add(x, y):
    logger = add.get_logger()
    logger.info("sleeping ...")
    time.sleep(5)
    logger.info("waking up.")
    return x + y
 

if __name__ == '__main__':
    app.worker_main()
