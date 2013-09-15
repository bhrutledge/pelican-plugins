Image Classes Plugin For Pelican
=================================

This plugin adds a "landscape" or "portrait" class to all `img` tags.

Todo
----

* Setting for limiting the image directories
* Settings-based rules for classes

Installation
------------

To enable, ensure that `img_class.py` is put somewhere that is accessible.
Then use as follows by adding the following to your settings.py:

    PLUGIN_PATH = 'path/to/pelican-plugins'
    PLUGINS = ["img_class"]

`PLUGIN_PATH` can be a path relative to your settings file or an absolute path.

Usage
-----
The plugin will activate upon the `content_object_init` signal of Pelican.
