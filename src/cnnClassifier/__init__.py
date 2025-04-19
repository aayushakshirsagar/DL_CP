import os
import sys
import logging

logging_str="[%(asctime)s: %(levelname)s %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log") #will create one log folder and then a running_logs file 

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #logs stored in the log file as well as displayed in the terminal using Stream Handler
        logging.StreamHandler(sys.stdout)


    ]

)

logger = logging.getLogger("cnnClassifierLogger")

