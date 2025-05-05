"""
Program to fetch the latest employee report, fetch the details from file and add the logs to keka
"""

import logging
from persistqueue import Queue
from email_file_fetch import download_attachments
from email_file_fetch_cod import download_attachments_cod

q1 = Queue("everyday_data_queue", autosave=True)

formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')

def setup_logger(name, log_file, level=logging.INFO):
    """
    Will help setup more than one logger
    :param name:
    :param log_file:
    :param level:
    :return:
    """
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


print("Downloading the latest file for both bacancy and cod...")
filename = download_attachments()
print(f"Downloaded: {filename}")
cod_filename = download_attachments_cod()
print(f"Downloaded COD file: {cod_filename}")

if filename:
    from fetch_data_file import fetch_data
    logger1 = setup_logger('hubstaff_logger', 'hubstaff_logs.log')
    fetch_data(logger=logger1, q1=q1, filename=filename)

if cod_filename:
    from fetch_data_file_cod import fetch_data_cod
    logger1 = setup_logger('hubstaff_logger_cod', 'hubstaff_cod_logs.log')
    fetch_data_cod(logger=logger1, q1=q1, filename=cod_filename)

if filename and cod_filename:
    from keka_logs import keka_main
    logger2 = setup_logger('keka_logger', 'keka_logs.log')
    keka_main(logger=logger2,q1=q1)
