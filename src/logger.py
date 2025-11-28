import logging
import os
from datetime import datetime

# Folder to store logs
LOG_FOLDER = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_FOLDER, exist_ok=True)

# Create a timestamped log file
LOG_FILE = f"app_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
LOG_FILE_PATH = os.path.join(LOG_FOLDER, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
 
if __name__ == "__main__":
    logging.info("Logger initialized.")