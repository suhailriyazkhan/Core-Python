import logging

logging.basicConfig(filename="mylog", level=logging.ERROR)
logging.critical("critical")
logging.error("Error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")

