import calendar
import logging
import time


class LogGen:
    @staticmethod
    def loggen():
        ts = calendar.timegm(time.gmtime())
        logging.basicConfig(filename="./Logs/autotest.log",
                            format='%(time)s: %(levels)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
