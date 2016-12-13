import logging.config
from . import settings
from flask import Flask


logging.config.dictConfig(settings.LOGGING)
app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY
app.debug = settings.DEBUG


if True:  # I don't like Pycharm warnings
    import catification.views
