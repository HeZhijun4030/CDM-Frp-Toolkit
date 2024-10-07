# pyfrpc/logger.py

import logging

def setup_logger(level=logging.INFO, log_file=None):
    """
    设置日志记录器。

    :param level: 日志级别，默认为 INFO。
    :param log_file: 日志文件路径，如果为 None，则输出到控制台。
    :return: 配置好的日志记录器。
    """
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('cdmfrpc')
    logger.setLevel(level)

    if log_file:
        handler = logging.FileHandler(log_file)
    else:
        handler = logging.StreamHandler()

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger