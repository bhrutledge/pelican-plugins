import os

from pelican import signals

from bs4 import BeautifulSoup
from PIL import Image


def get_orientation(im):
    if im.size[0] <= im.size[1]:
        return 'portrait'

    return 'landscape'


def get_static_path(src, instance):
    # TODO: Refer to better_figures_and_images
    # TODO: Use Pelican to find static files
    try:
        img_path = src.split('{filename}')[1]
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
            orientation = get_orientation(im)

            try:
                img['class'].append(orientation)
            except:
                img['class'] = orientation

        instance._content = soup.decode()


def register():
    signals.content_object_init.connect(content_object_init)

