from __future__ import annotations
import asyncio as asyncio
from functools import partial
from functools import wraps
from pxr import Sdf
from pxr import Usd
import re as re
__all__: list = ['wrap', 'aio_open_layer', 'aio_re_find_all', 'aio_replace_all', 'aio_save_layer', 'aio_re_sub_all']
def _layer_save(layer):
    ...
def _open_layer(path):
    ...
def _re_find_all(regex, content):
    ...
def _replace_all(s, old_text, new_text, exact_match = False):
    ...
def _sub_all(s, pattern, replace):
    ...
def wrap(func):
    ...
__warningregistry__: dict = {'version': 4}
aio_open_layer = _open_layer
aio_re_find_all = _re_find_all
aio_re_sub_all = _sub_all
aio_replace_all = _replace_all
aio_save_layer = _layer_save
