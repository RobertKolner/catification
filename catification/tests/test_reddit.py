import praw
from catification import settings
from catification.reddit import get_posts, get_client, get_subreddit
from unittest import mock
from unittest.mock import MagicMock


def test_get_client():
    client = get_client(
        client_id=settings.REDDIT['client_id'],
        client_secret=settings.REDDIT['client_secret'],
        password=settings.REDDIT['password'],
        user_agent=settings.REDDIT['user_agent'],
        username=settings.REDDIT['username'],
    )
    assert client is not None
    assert isinstance(client, praw.Reddit)


def test_get_client_with_defaults():
    client = get_client()
    assert client is not None
    assert isinstance(client, praw.Reddit)


def test_get_subreddit_choses_from_available_list():
    sr = ['cats']

    client = get_client()
    with mock.patch.object(client, 'subreddit', MagicMock(return_value=sr[0])) as method:
        subreddit = get_subreddit(client=client, subreddit_list=sr)
        method.assert_called_once_with(sr[0])
        assert subreddit == sr[0]
