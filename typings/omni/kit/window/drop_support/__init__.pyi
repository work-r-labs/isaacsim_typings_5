"""
This module provides support for handling external drag and drop events in specified application windows, offering functionality to detect events, check mouse coordinates, and expand directories in payloads.
"""
from __future__ import annotations
from omni.kit.window.drop_support.drop_support import ExternalDragDrop
from . import drop_support
__all__ = ['ExternalDragDrop', 'drop_support']
