# Image Classes Plugin For Pelican

This plugin adds "landscape" or "portrait" to the `class` attribute of all `img`
tags.

## Todo

* Setting for limiting the image directories
* Settings-based rules for classes

## Installation

This plugin requires [PIL][1] and [BeautifulSoup][2]:

    pip install PIL
    pip install BeautifulSoup4

To enable the plugin, copy the `img_class` package to your `PLUGIN_PATH`, and 
add `img_class` to the `PLUGINS` setting. See the [Pelican docs][3] for more
info.

[1]: http://www.pythonware.com/products/pil/
[2]: http://www.crummy.com/software/BeautifulSoup/
[3]: http://docs.getpelican.com/en/latest/plugins.html

## Usage

The plugin will activate upon the `content_object_init` signal of Pelican.
