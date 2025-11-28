
import sys
from src.logger import logging

# ------------------------------
# Custom Exception
# ------------------------------
def error_message_detail(error_message, error_detail:sys):
    """
    Formats the exception with filename and line number,
    and logs it automatically.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message_formatted = (
        f"Error occurred in script: [{file_name}] at line: [{line_number}] | Error: [{error_message}]"
    )

    # Automatically log the error
    logging.error(error_message_formatted)
    
    return error_message_formatted

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        # Create formatted message and log it
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message

# ------------------------------
# Example usage
# ------------------------------

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        raise CustomException(e, sys)