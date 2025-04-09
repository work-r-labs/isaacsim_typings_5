"""
Registration for items that want to be added to all viewports
"""
from __future__ import annotations
from omni.kit.viewport.registry.registry import _make_registry
from . import registry
__all__: list = ['RegisterScene', 'RegisterViewportLayer']
