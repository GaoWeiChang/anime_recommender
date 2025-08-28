import logging
import os # work with directory
from datetime import datetime

# create directory
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True) # if exist, dont create

# create log file path
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log") # ex. log_2023-10-01.log

# configure logging
logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger