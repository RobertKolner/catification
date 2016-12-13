import base64
import logging
from praw.models import Submission
from typing import Iterable, List
from .validators import URLValidator


logger = logging.getLogger(__name__)


def encode_url_key(key: str, clear: str) -> str:
    enc = []
    for i, c in enumerate(clear):
        key_c = key[i % len(key)]
        enc_c = chr((ord(c) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


def decode_url_key(key: str, enc: str) -> str:
    dec = []
    enc = base64.urlsafe_b64decode(enc.encode()).decode()
    for i, c in enumerate(enc):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(c) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)


def valid_post_links(posts: Iterable[Submission], validators: List[URLValidator]) -> Iterable[str]:
    for post in posts:
        for validator in validators:
            validated = validator(post.url)
            if validated:
                yield validated
                break
        logger.debug("Post with url `{}` rejected.".format(post.url))