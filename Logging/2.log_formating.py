import logging


"""
This script demonstrates how to configure and use the Python logging module with custom message formatting.
The logging.basicConfig() function is used to set up the logging system with the following parameter:
    - format: Specifies the format of the log messages using format codes.
        - %(asctime)s: Timestamp when the log record was created.
        - %(levelname)s: Text logging level for the message (e.g., INFO, WARNING).
        - %(message)s: The actual log message.
        - %(name)s: Name of the logger used.
        - %(filename)s: Name of the file where the logging call was made.
        - %(lineno)d: Line number in the source file where the logging call was made.
        - %(funcName)s: Name of the function containing the logging call.
        - %(process)d: Process ID (useful in multiprocessing).
        - %(thread)d: Thread ID (useful in multithreading).
Example log output:
    2024-06-10 12:34:56,789 - INFO - this is log message
You can customize the format string to include any combination of these attributes to suit your logging needs.
"""


# Configure logging
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(levelname)s - %(message)s')

# advanced formatting with additional attributes
logging.basicConfig(level=logging.INFO,
                    format='{asctime} - {levelname} - {message} - {name} - {filename} - {lineno} - {funcName} - {process:d} - {thread:d}',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    style='{')

logging.info("this is log message")