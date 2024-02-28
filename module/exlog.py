import logging
import datetime
import os

logging.basicConfig(
    format='[%(asctime)s][%(levelname)s][%(name)s:%(lineno)s] : %(message)s',
    level=logging.DEBUG,
    filename='C:/Users/admin/Desktop/taepyo_tarding/logging/trading.{:%Y%m%d}.log'.format(datetime.datetime.now()),
    datefmt='%m-%d-%Y %I:%M:%S',
)

class ExLogger:
  def __init__(self, name, mode):
    self.logger = logging.getLogger(name)
    if mode == "d" :
      self.logger.setLevel(logging.DEBUG)
    elif mode == "i" :
      self.logger.setLevel(logging.INFO)
    elif mode == "w" :
      self.logger.setLevel(logging.WARNING)
    elif mode == "e" :
      self.logger.setLevel(logging.ERROR)
    elif mode == "c" :
      self.logger.setLevel(logging.CRITICAL)