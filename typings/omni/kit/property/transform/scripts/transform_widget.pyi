"""
Provides a widget for editing transformation attributes of USD prims in the user interface.
"""
from __future__ import annotations
import carb as carb
from collections import defaultdict
from functools import lru_cache
import omni as omni
from omni.kit.property.transform.scripts.transform_builder import TransformWidgets
from omni.kit.property.transform.scripts.xform_op_utils import _add_trs_op
from omni.kit.property.usd.usd_attribute_model import GfVecAttributeSingleChannelModel
from omni.kit.property.usd.usd_property_widget import UsdPropertiesWidget
from omni.kit.property.usd.usd_property_widget import get_group_properties_clipboard
from omni.kit.property.usd.usd_property_widget import set_group_properties_clipboard
from omni.kit.widget.settings.style import get_style
from omni.kit.window.property.templates.header_context_menu import GroupHeaderContextMenu
from omni.kit.window.property.templates.header_context_menu import GroupHeaderContextMenuEvent
from omni import ui
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
from pxr import UsdGeom
import traceback as traceback
__all__ = ['ADDITIONAL_CHANGED_PATH_EVENT_TYPE', 'GfVecAttributeSingleChannelModel', 'GroupHeaderContextMenu', 'GroupHeaderContextMenuEvent', 'Sdf', 'Tf', 'Trace', 'TransformAttributeWidget', 'TransformWidgets', 'Usd', 'UsdGeom', 'UsdPropertiesWidget', 'carb', 'defaultdict', 'get_group_properties_clipboard', 'get_style', 'lru_cache', 'omni', 'set_group_properties_clipboard', 'traceback', 'ui']
class TransformAttributeWidget(omni.kit.property.usd.usd_property_widget.UsdPropertiesWidget):
    """
    A class for managing transformation attributes of USD prims.
    
        This widget is designed to interact with and manipulate transformation attributes of USD prims within a user interface. It extends the UsdPropertiesWidget to provide a specialized interface for handling transformations, including features such as adding new transform operations, copying, pasting, and resetting transformation values, and toggling between different modes like offset mode.
    
            Args:
                title (str): The title of the widget.
                collapsed (bool): A flag indicating whether the widget starts in a collapsed state.
    """
    @staticmethod
    def _on_usd_changed(*args, **kwargs):
        ...
    def __init__(self, title: str, collapsed: bool):
        """
        Initializer for TransformAttributeWidget.
        """
    def _build_frame_header(self, collapsed, text: str, group_id: str = None):
        """
        Custom header for CollapsableFrame
        """
    def _build_header_context_menu(self, group_id: str):
        ...
    def _on_add_transform(self):
        ...
    def _toggle_link_scale(self):
        ...
    def _toggle_offset_mode(self):
        ...
    def build_items(self):
        """
        Builds the items for the transform attribute widget.
        """
    def clean(self):
        """
        Cleans up the widget and its resources.
        """
    def on_new_payload(self, payload):
        """
        Handles a new payload for the widget.
        
                Args:
                    payload (dict): The new payload to be handled by the widget.
        
                Returns:
                    bool: True if the payload is handled successfully, False otherwise.
        """
    def toggle_link_scale(self):
        ...
def _get_plus_glyph(*args, **kwargs):
    ...
ADDITIONAL_CHANGED_PATH_EVENT_TYPE: int = 17954634024720962805
