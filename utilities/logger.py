import logging
import datetime

def get_logger():
    logger = logging.getLogger(__name__)
    if not logger.hasHandlers():
        # Create a unique log file name with a timestamp
        log_file = f"logs/test_run_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger