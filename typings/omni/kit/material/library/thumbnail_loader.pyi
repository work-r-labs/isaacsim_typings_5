"""
Material thumbnail loader class.
"""
from __future__ import annotations
import asyncio as asyncio
import copy as copy
import omni as omni
from omni import ui
import pxr.Usd
from pxr import Usd
__all__: list = ['ThumbnailLoader']
class ThumbnailLoader:
    """
    Material thumbnail loader class.
    """
    def __init__(self):
        ...
    def load(self, material_prim: pxr.Usd.Prim, thumbnail_image: omni.ui._ui.Image):
        ...
    def purge(self):
        ...
    def set_material_thumbnail_url(self, thumbnail_image: omni.ui._ui.Image, thumbnail_url: str):
        ...
