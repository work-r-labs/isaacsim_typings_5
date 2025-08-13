"""
Module implementing a ContentBrowserOptions class to integrate custom context menus into the content browser for adding file-based references or payloads to a USD stage using selection-based or viewport-based placement.
"""
from __future__ import annotations
import omni as omni
from omni.kit.menu.stage.content_browser_options import ContentBrowserOptions
from omni.kit.menu.stage.stage_menus_extension import StageMenusExtension
from . import content_browser_options
from . import stage_menus_extension
__all__: list = ['ContentBrowserOptions']
