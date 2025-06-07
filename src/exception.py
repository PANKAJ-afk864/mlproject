import sys
import traceback

def error_message_detail(error, error_detail: sys):
    """
    Returns a detailed error message with file name, line number, and error description.
    """
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script [{file_name}] at line [{line_number}] with error: {str(error)}"
    return error_message


class CustomException(Exception):
    """
    Custom exception class that captures detailed context about an error.
    """
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the CustomException with detailed error information.

        Args:
            error_message (str): The original error message.
            error_detail (sys): The sys module to extract traceback information.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        """
        Returns the string representation of the CustomException.
        """
        return self.error_message
