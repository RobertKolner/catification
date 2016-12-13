import logging.config
from . import settings
from flask import Flask


logging.config.dictConfig(settings.LOGGING)
app = Flask(__name__)


if True:  # I don't like Pycharm warnings
    import catification.views
