"""
This module provides functionality for creating a 'Create' menu in kit, allowing for registration of actions and menu items related to primitive creation like shapes, lights, audio sources, cameras, and more, with support for toggling options such as 'High Quality' for primitives.
"""
from __future__ import annotations
import omni as omni
from omni.kit.menu.create.create import CreateMenuExtension
from omni.kit.menu.create.create import rebuild_menus
from . import create
from . import create_actions
__all__: list = ['CreateMenuExtension', 'get_action_name', 'rebuild_menus', 'get_geometry_standard_prim_list', 'get_light_prim_list', 'get_audio_prim_list']
