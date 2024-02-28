from module import exlog
from time import sleep

logger = exlog.ExLogger(__name__, 'd').logger

while True:
  logger.debug('asd')