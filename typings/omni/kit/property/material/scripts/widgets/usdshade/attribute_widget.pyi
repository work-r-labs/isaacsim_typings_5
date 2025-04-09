"""
This module provides a custom widget for displaying UsdShade attributes in the Raw Properties widget, specifically modifying the display metadata to present a flat list of properties.
"""
from __future__ import annotations
import omni.kit.property.usd.usd_property_widget
from omni.kit.property.usd.usd_property_widget import RawUsdPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from pxr import Sdf
from pxr import UsdShade
__all__: list = ['UsdShadeAttributeWidget']
class UsdShadeAttributeWidget(omni.kit.property.usd.usd_property_widget.RawUsdPropertiesWidget):
    """
    A widget that overrides the display of UsdShade attributes in the Raw Properties widget.
    
        This widget modifies the UsdPropertyUiEntry instances to remove the display[Name|Group] metadata, resulting in a flat list presentation of the properties without pagination.
        
    """
    def _customize_props_layout(self, props: typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]) -> typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]:
        """
        
                If prims are UsdShade then remove:
                    1. display name - so the true property name is shown.
                    2. display group - so properties are shown unpaginated.
                
        """
