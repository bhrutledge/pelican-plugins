import os

from pelican import signals

from bs4 import BeautifulSoup
from PIL import Image


def get_static_path(src, instance):   
    try:
        img_path = src.split("/static/")[1]
    except IndexError:
        return None

    return os.path.join(instance.settings['PATH'], *img_path.split('/'))


def content_object_init(instance):

    if instance._content:
        soup = BeautifulSoup(instance._content)

        for img in soup('img'):
            static_path = get_static_path(img['src'], instance)
            if not static_path:
                continue

            im = Image.open(static_path)

            orientation = 'landscape'
            if im.size[0] <= im.size[1]:
                orientation = 'portrait'

            try:
                img['class'].append(orientation)
            except:
                img['class'] = orientation

        instance._content = soup.decode()


def register():
    signals.content_object_init.connect(content_object_init)
