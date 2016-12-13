from catification.utils import decode_url_key, encode_url_key
from unittest import mock
from unittest.mock import MagicMock


def test_encode_url_key():
    url = 'https://google.com'
    enc = encode_url_key('cats', url)

    assert ':' not in enc
    assert '/' not in enc
    assert 'google' not in enc


def test_uncode_decode_url_key():
    url = 'https://google.com'
    enc = encode_url_key('cats', url)
    assert url == decode_url_key('cats', enc)

