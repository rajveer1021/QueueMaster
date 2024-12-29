from celery import shared_task
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

@shared_task
def add(x, y):
    try:
        result = x + y
        time.sleep(30)
        logging.info(f"Task completed successfully. Result: {result}")
        return result
    except Exception as e:
        logging.error(f"Task failed with error: {e}")
        raise

@shared_task(
    max_retries=3,  # Maximum number of retries
    default_retry_delay=5,  # Wait 5 seconds before retrying
    autoretry_for=(Exception,),  # Exceptions to trigger a retry
)
def time_task(time_period):
    try:
        time.sleep(100)
        logging.info(f"This is a time-consuming task but will start parallelly: {time_period}")
    except Exception as e:
        logging.error(f"There is an error: {e}")
        raise
