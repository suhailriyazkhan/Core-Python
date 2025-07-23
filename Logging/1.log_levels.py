import logging


"""
This script demonstrates the different log levels available in Python's logging module.

Log Levels:
- DEBUG: Detailed information, typically of interest only when diagnosing problems.
- INFO: Confirmation that things are working as expected.
- WARNING: An indication that something unexpected happened, or indicative of some problem in the near future.
- ERROR: Due to a more serious problem, the software has not been able to perform some function.
- CRITICAL: A very serious error, indicating that the program itself may be unable to continue running.

The script sets the logging level to INFO, so INFO and higher level messages (WARNING, ERROR, CRITICAL) are displayed.
DEBUG messages are ignored.
"""

# Configure logging
logging.basicConfig(level=logging.INFO)

# logging level: DEBUG (10)
logging.debug("debug") # level is set to INFO (20), so this won't be logged

# logging level: INFO (20)
logging.info("info") # level is set to INFO (20), so this will be logged

# logging level: WARNING (30)
logging.warning("warning") # level is set to INFO (20), so this will be logged

# logging level: ERROR (40)
logging.error("Error") # level is set to INFO (20), so this will be logged

# logging level: CRITICAL (50)
logging.critical("critical") # level is set to INFO (20), so this will be logged