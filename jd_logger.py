import logging
import logging.handlers

'''
日志模块
'''
LOG_FILENAME = './log/jd_seckill.log'
logger = logging.getLogger()


def set_logger():
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - pid-%(process)d - %(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    file_handler = logging.handlers.TimedRotatingFileHandler(
        LOG_FILENAME, when='D', interval=1, backupCount=10, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


set_logger()
