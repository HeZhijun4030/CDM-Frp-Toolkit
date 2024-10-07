# pyfrpc/logger.py

import logging

def setup_logger(level, log_file=None):
    """
    设置日志记录器。

    :param level: 日志级别，默认为 INFO。
    :param log_file: 日志文件路径，如果为 None，则输出到控制台。
    :return: 配置好的日志记录器。
    """
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger('cdmfrpc')
    if level=='debug' or level=='DEBUG':
        level = logging.DEBUG
    elif level=='info' or level=='INFO':
        level = logging.INFO
    elif level=='warning' or level=='WARNING':
        level = logging.WARNING
    elif level=='error' or level=='ERROR':
        level = logging.ERROR
    elif level=='critical'  or level=='CRITICAL':
        level = logging.CRITICAL
    logger.setLevel(level)

    if log_file:
        handler = logging.FileHandler(log_file)
    else:
        handler = logging.StreamHandler()

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger