import os


# Secret key used for a myriad of stuff
SECRET_KEY = os.getenv('SECRET_KEY', 'cats')


# Python logging configuration
LOGGING = {
    "version": 1,
    "formatters": {
        "simple": {
            'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": 'DEBUG',
            "stream": "ext://sys.stdout",
        }
    },
    "root": {
        "handlers": ["console"],
        "level": 'DEBUG',
    }
}


# Reddit-Praw settings
REDDIT = {
    'subreddits': [
        'babybigcatgifs', 'BadAtCat', 'cats', 'CatGifs', 'Catloaf', 'StartledCats',
        'catpranks', 'CatSlaps', 'catsonglass', 'CatsStandingUp', 'catsvstechnology',
        'kittengifs', 'LazyCats', 'StartledCats',
    ],
    'post_limit': 50,
    'client_id': os.getenv('REDDIT_CLIENT_ID'),
    'client_secret': os.getenv('REDDIT_CLIENT_SECRET'),
    'username': os.getenv('REDDIT_USERNAME'),
    'password': os.getenv('REDDIT_PASSWORD'),
    'user_agent': os.getenv('REDDIT_USER_AGENT', 'CatCrawler'),
}


# Local overrides
try:
    from .local_settings import *  # noqa
except ImportError:
    pass  # all good


for key in ('client_id', 'client_secret', 'username', 'password', 'user_agent'):
    if not REDDIT[key]:
        raise ValueError("Setting `{key}` must be set!".format(key=key))
