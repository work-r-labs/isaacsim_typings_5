"""
This module provides access to a singleton ToolbarRegistry instance for manipulator toolbars.
"""
from __future__ import annotations
import omni.kit.manipulator.transform.toolbar_registry
from omni.kit.manipulator.transform.toolbar_registry import ToolbarRegistry
__all__ = ['ToolbarRegistry', 'get_toolbar_registry']
def get_toolbar_registry() -> omni.kit.manipulator.transform.toolbar_registry.ToolbarRegistry:
    """
    Returns the singleton instance of the ToolbarRegistry.
    
        Returns:
            :obj:`ToolbarRegistry`: The singleton instance of the ToolbarRegistry.
    """
_toolbar_registry: omni.kit.manipulator.transform.toolbar_registry.ToolbarRegistry  # value = <omni.kit.manipulator.transform.toolbar_registry.ToolbarRegistry object>
