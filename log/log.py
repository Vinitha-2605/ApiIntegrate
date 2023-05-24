import logging

def initialize_log():
 logger = logging.getLogger(__name__)

 log_format ='%(asctime)s - %(filename)s - %(funcName)s() - %(levelname)s - %(message)s'
 logger.setLevel(logging.INFO)
 file = logging.FileHandler('app.log')
 format = logging.Formatter(log_format)

 file.setFormatter(format)
 logger.addHandler(file)

 return logger