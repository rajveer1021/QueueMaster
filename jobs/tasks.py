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
        time.sleep(10)
        logging.info(f"Task completed successfully. Result: {result}")
        return result
    except Exception as e:
        logging.error(f"Task failed with error: {e}")
        raise