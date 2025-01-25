import logging

def setup_logging(name, path):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    return logging.getLogger()


# logger = logging.getLogger()
# logger.setLevel(logging.INFO)
# file_handler = logging.FileHandler(log_utils_file, mode='w',  encoding="utf-8")
# file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
# file_handler.setFormatter(file_formater)
# logger.addHandler(file_handler)