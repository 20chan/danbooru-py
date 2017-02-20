import json
import urllib.request
from typing import Generator
import os.path
from PIL import Image
import requests
from io import BytesIO
import argparse


def pages(limit: int = 10, page: int = 1) -> Generator:
    cur = page
    while True:
        url = 'https://gelbooru.com/index.php?page=dapi&s=post&q=index&limit={}&pid={}&json=1'.format(limit, cur)
        res = json.loads(urllib.request.urlopen(url).read().decode('utf-8'))
        for post in res:
            yield post
        cur += 1

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--pid', type=int, default=1)
    parser.add_argument('--limit', type=int, default=100)

    args = parser.parse_args()
    p = pages(limit=args.limit, page=args.pid)
    while True:
        post = next(p)
        if 'file_url' in post.keys():
            try:
                loc = os.path.join('Download', str('sqe'.index(post['rating'])), str(post['id']) + '.png')
                response = requests.get('https:{}'.format(post['file_url']))
                print('downloading {} in {}...'.format(post['id'], loc))
                img = Image.open(BytesIO(response.content))
                img = img.resize((300, 300), Image.ANTIALIAS)
                img.save(loc)
            except Exception:
                print('Exception raised..')
                continue
