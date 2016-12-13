import abc
from typing import Optional


class URLValidator(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __call__(self, url: str) -> Optional[str]:
        pass


class ImgurValidator(URLValidator):
    def __call__(self, url: str) -> Optional[str]:
        if 'imgur.com' in url and '/gallery/' not in url and '/a/' not in url and '?' not in url:
            if 'i.imgur.com' not in url:
                url = url.replace('imgur.com', 'i.imgur.com')
            if url[-4:] == 'gifv':
                url = url[:-1]
            elif '.' not in url[-4:]:
                url += '.gif'
            return url

        return None
