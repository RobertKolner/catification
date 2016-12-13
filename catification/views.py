import logging
import random
from flask import redirect, request, render_template
from . import app, settings
from .reddit import get_posts
from .utils import decode_url_key, encode_url_key, valid_post_links
from .validators import ImgurValidator


logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def cat():
    if 'cat' not in request.args:
        urls = valid_post_links(get_posts(), validators=[ImgurValidator()])
        url = encode_url_key(settings.SECRET_KEY, random.choice([u for u in urls]))
        return redirect('/?cat={}'.format(url))

    encoded = request.args.get('cat')
    url = decode_url_key(settings.SECRET_KEY, encoded)
    logger.info('Returning cat image on "{url}"'.format(url=url))
    context = {
        'image_url': url
    }
    return render_template('index.html', **context)
