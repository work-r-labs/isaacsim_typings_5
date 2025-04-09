"""
This module defines UsdShadePropertyUiEntry, a subclass of UsdPropertyUiEntry, which overrides the metadata comparison function.
"""
from __future__ import annotations
import omni.kit.property.usd.usd_property_widget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from pxr import Sdf
from pxr import Sdr
__all__: list = ['UsdShadePropertyUiEntry']
class UsdShadePropertyUiEntry(omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry):
    """
    Subclass of :obj:`UsdPropertyUiEntry` that overrides the metadata comparison function.
    """
    def _compare_metadata(self, meta1: dict, meta2: dict) -> bool:
        ...
