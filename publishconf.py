# Configuración de producción (para GitHub Pages)
# =================================================
import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa

SITEURL = "https://gabohndz.github.io"
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

# Feeds completos en producción
FEED_ALL_ATOM = "feeds/todos.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
