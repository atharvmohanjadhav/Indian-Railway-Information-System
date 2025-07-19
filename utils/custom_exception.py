import sys
import os
import logging
from datetime import datetime

class IrisException(Exception):
    def __init__(self, error_msg, error_details: sys):
        self.error_msg = error_msg

        # Extract traceback info
        _, _, exc_tb = error_details.exc_info()
        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

        # Format the error message
        self.formatted_msg = (
            f"Error occurred in script [{self.filename}] "
            f"at line [{self.lineno}]: {str(self.error_msg)}"
        )

        # Create logs directory if not exists
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # Configure logger
        self.logger = logging.getLogger("IrisLogger")
        self.logger.setLevel(logging.ERROR)

        # Avoid duplicate handlers
        if not self.logger.handlers:
            file_handler = logging.FileHandler(f"{log_dir}/error_log.log")
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

        # Log the error
        self.logger.error(self.formatted_msg)

        super().__init__(self.formatted_msg)

    def __str__(self):
        return self.formatted_msg


if __name__ == "__main__":
    try:
        1 / 0
    except Exception as e:
        raise IrisException(e,sys)
