import logging

"""
This script demonstrates how to configure Python's logging module to write log messages to a file.
Features:
- Logs messages to a file named 'mylog'.
- Uses 'filemode="w"' to overwrite the log file each time the script runs, instead of appending to it.
Parameters:
- filemode: Specifies the mode to open the log file. 'w' means write mode, which overwrites the file on each run. Use 'a' to append to the file instead.
"""


# Configure logging
logging.basicConfig(level=logging.INFO,
                    filename='mylog', filemode='w')

logging.info("this is log message")