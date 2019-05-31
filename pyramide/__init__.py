"""pyramide - pyramide es un simple crawler basado en crawlerino"""

__version__ = '0.0.1'
__author__ = 'manuvaldes <manuvaldes@gmail.com>'
__all__ = []

#TODO añade un import para que crawler sea visible desde el primer nivel
from .pyramide import Crawler
from .handlers import WordCountHandler