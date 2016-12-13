import random
from catification import settings
from praw.models import Submission, Subreddit, SubredditHelper
from praw import Reddit
from typing import Iterable, Optional


def get_client(
    client_id=None, client_secret=None, password=None, user_agent=None, username=None
):
    client_id = client_id or settings.REDDIT['client_id']
    client_secret = client_secret or settings.REDDIT['client_secret']
    password = password or settings.REDDIT['password']
    user_agent = user_agent or settings.REDDIT['user_agent']
    username = username or settings.REDDIT['username']
    return Reddit(
        client_id=client_id,
        client_secret=client_secret,
        password=password,
        user_agent=user_agent,
        username=username,
    )


def get_subreddit(client: Optional[Reddit]=None, subreddit_list=None) -> SubredditHelper:
    if client is None:
        client = get_client()
    if subreddit_list is None:
        subreddit_list = settings.REDDIT['subreddits']
    return client.subreddit(random.choice(subreddit_list))


def get_posts(subreddit: Optional[Subreddit]=None) -> Iterable[Submission]:
    if not subreddit:
        subreddit = get_subreddit()
    return subreddit.hot(limit=50)
