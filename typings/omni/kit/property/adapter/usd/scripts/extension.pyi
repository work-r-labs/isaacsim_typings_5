from __future__ import annotations
import omni as omni
from omni.kit.property.adapter import core as ac
from omni.kit.property.adapter.usd.scripts.usd_adapter import UsdStageAdapter
__all__ = ['UsdPropertyAdapterExtension', 'UsdStageAdapter', 'ac', 'omni']
class UsdPropertyAdapterExtension(omni.ext._extensions.IExt):
    """
    The entry point for Stage Window
    """
    def __init__(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
