"""
This module provides the UsdUIBackdropWidget class, which is a specialized USD properties widget for interacting with USD UI Backdrop elements within a properties panel.
"""
from __future__ import annotations
import carb as carb
from omni.kit.property.material.scripts.widgets.usdshade.utils import property_name_to_display_name
import omni.kit.property.usd.prim_selection_payload
from omni.kit.property.usd.prim_selection_payload import PrimSelectionPayload
import omni.kit.property.usd.usd_property_widget
from omni.kit.property.usd.usd_property_widget import UsdPropertiesWidget
from omni.kit.property.usd.usd_property_widget import UsdPropertyUiEntry
from pxr import UsdUI
import typing
__all__ = ['PrimSelectionPayload', 'UsdPropertiesWidget', 'UsdPropertyUiEntry', 'UsdUI', 'UsdUIBackdropWidget', 'carb', 'property_name_to_display_name']
class UsdUIBackdropWidget(omni.kit.property.usd.usd_property_widget.UsdPropertiesWidget):
    """
    A widget representing a USD UI Backdrop within a properties panel.
    
        This widget extends the UsdPropertiesWidget to specifically handle the display and
        interaction with USD UI Backdrop elements. It provides a custom property layout
        and integrates with the material adapter settings. The widget is initialized
        with a title and configures itself based on the application settings.
    
        Args:
            title (str): The title of the backdrop widget. Defaults to 'Backdrop'.
    """
    MATERIAL_ADAPTER_SETTING_PATH: typing.ClassVar[str] = '/ext/omni.kit.property.material/enableAdapter'
    def __init__(self, title: str = 'Backdrop'):
        """
        Initializes the backdrop widget with optional title.
        """
    def _customize_props_layout(self, props: typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]) -> typing.List[omni.kit.property.usd.usd_property_widget.UsdPropertyUiEntry]:
        ...
    def on_new_payload(self, payload: omni.kit.property.usd.prim_selection_payload.PrimSelectionPayload) -> bool:
        """
        Handles a new payload for the widget.
        
                Args:
                    payload (:obj:`PrimSelectionPayload`): The new payload to be handled by the widget.
        
                Returns:
                    bool: True if the payload is processed successfully, otherwise False.
        """
