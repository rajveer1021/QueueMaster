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
        logging.info(f"Task1 started")
        result = x + y
        time.sleep(30)
        logging.info(f"Task1 completed successfully. Result: {result}")
        return result
    except Exception as e:
        logging.error(f"Task failed with error: {e}")
        raise

@shared_task(
    max_retries=3,  # Maximum number of retries
    default_retry_delay=5,  # Wait 5 seconds before retrying
    autoretry_for=(Exception,),  # Exceptions to trigger a retry
)
def time_task():
    try:
        logging.info(f"Task2 started")
        time.sleep(100)
        logging.info(f"Task2 completed successfully.")
    except Exception as e:
        logging.error(f"There is an error: {e}")
        raise
