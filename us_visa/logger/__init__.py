import os
from datetime import datetime
import sys
import logging
from from_root import from_root

logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir='logs'
log_filepath=os.path.join(from_root(),log_dir,LOG_FILE)
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    format=logging_str,
    level=logging.DEBUG,
    handlers=[logging.FileHandler(log_filepath),logging.StreamHandler(sys.stdout)] 
)

