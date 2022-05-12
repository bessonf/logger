import os, logging
from datetime import datetime

cwd = os.path.dirname(os.path.realpath(__file__))
now_fname = f'{datetime.now().strftime("%m-%d-%Y_%H%M%S")}.txt'


# HANDLE PATHS FOR ERROR FILES
err_path = os.path.join(cwd, '_err')

if not os.path.exists(err_path):
    os.makedirs(err_path)

err_fname = os.path.join(err_path, now_fname)


# HANDLE PATHS FOR LOG FILES
log_path = os.path.join(cwd, '_log')

if not os.path.exists(log_path):
    os.makedirs(log_path)

log_fname = os.path.join(log_path, now_fname)


# DEFINE FORMATTER
formatter = logging.Formatter(
    '%(asctime)s | %(name)s |  %(levelname)s: %(message)s')


# DEFIN FILTER
class MyFilter(object):
    def __init__(self, level):
        self.__level = level

    def filter(self, logRecord):
        return logRecord.levelno <= self.__level


# DFFINE HANDLER FOR INFO LEVEL
handler_log = logging.FileHandler(
    filename=log_fname,
    mode='w',
    delay=True
)
handler_log.setFormatter(formatter)
handler_log.setLevel(logging.INFO)
handler_log.addFilter(MyFilter(logging.INFO))


# DFFINE HANDLER FOR ERROR LEVEL
handler_err = logging.FileHandler(
    filename=err_fname,
    mode='w',
    delay=True
)
handler_err.setFormatter(formatter)
handler_err.setLevel(logging.ERROR)
handler_err.addFilter(MyFilter(logging.ERROR))


# DFFINE LOGGER
logging.basicConfig(
	handlers=[
		# logging.StreamHandler(),
        handler_log,
        handler_err
	], 
	level='INFO',
    format='%(levelname)s %(asctime)s %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S'
)

logger = logging.getLogger('my_logger')


if __name__ == "__main__":
    logger.info('test log')
    logger.error('test err')
