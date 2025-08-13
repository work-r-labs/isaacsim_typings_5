"""
This module provides functionality for creating a 'Create' menu in kit, allowing for registration of actions and menu items related to primitive creation like shapes, lights, audio sources, cameras, and more, with support for toggling options such as 'High Quality' for primitives.
"""
from __future__ import annotations
from omni.kit.menu.create.create import CreateMenuExtension
from omni.kit.menu.create.create import rebuild_menus
from . import create
from . import create_actions
__all__: list = ['CreateMenuExtension', 'rebuild_menus']
