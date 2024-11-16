import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup", "data_load")
class BaseClass:
    def get_logger(self):
        # https://docs.python.org/3.13/library/inspect.html#inspect.FrameInfo
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # file handler object
        logger.setLevel(logging.DEBUG)  # You will see logs starting from level in this argument

        return logger
