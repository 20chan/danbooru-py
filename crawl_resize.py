from danbooru import pages
from PIL import Image
import requests
from io import BytesIO


def get(size=(300, 300)) -> (Image, int):
    ''':returns PIL.Image, 0~2 raiting level. 0 is safe, 1 is questionable, 2 is explicit.'''
    p = pages(limit=100)
    while True:
        post = next(p)
        if 'file_url' in post.keys():
            response = requests.get('https://danbooru.donmai.us{}'.format(post['file_url']))
            img = Image.open(BytesIO(response.content))
            img = img.resize(size, Image.ANTIALIAS)
            yield img, 'sqe'.index(post['rating'])
