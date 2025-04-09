"""
This module provides a widget for binding materials to selected USD prims within NVIDIA Omniverse Kit.
"""
from __future__ import annotations
import carb as carb
import contextlib as contextlib
import copy as copy
from functools import partial
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.material.library.listbox_widget import MaterialListBoxWidget
from omni.kit.material.library.search_widget import SearchWidget
from omni.kit.material.library.thumbnail_loader import ThumbnailLoader
from omni.kit.property.material.scripts.widgets.material_binding.context_menu import show_context_menu
from omni.kit.property.material.scripts.widgets.material_binding.material_utils import Constant
from omni.kit.property.material.scripts.widgets.material_binding.material_utils import get_binding_from_prims
from omni.kit.widget.highlight_label.highlight_label import HighlightLabel
from omni.kit.window.property.templates.simple_property_widget import SimplePropertyWidget
from omni import ui
import os as os
from pxr import Tf
from pxr import Usd
from pxr import UsdShade
import typing
__all__: list = ['MaterialBindingWidget']
class MaterialBindingWidget(omni.kit.window.property.templates.simple_property_widget.SimplePropertyWidget):
    """
    A widget designed to bind materials to selected USD prims.
    
        This widget facilitates the association of materials to prims in USD stages by providing a user interface for selection and assignment. It supports context menus, search functionality, thumbnail previews, and asynchronous material retrieval.
    
        Args:
            extension_path (Optional[str]): The path where the extension is located. Used for loading icons and other resources.
            add_context_menu (bool): Indicates whether to add a context menu to the widget.
            title (str): The title of the widget.
            material_purpose (str): The purpose of the material (e.g., 'allPurpose', 'preview', etc.).
            filter_fn (Optional[callable]): A function used to filter materials.
            get_materials_async_fn (Optional[callable]): An asynchronous function to retrieve materials.
    
        Keyword Args:
            collapsed (bool): Specifies whether the widget is initially collapsed.
            collapsable (bool): Specifies whether the widget is collapsible.
            enable_bound_widget (bool): Enables the display of the bound widget.
            enable_strength_widget (bool): Enables the display of the material strength widget.
    """
    EXTENSION_PATH: typing.ClassVar[str] = '/home/chris/isaacsim/extscache/omni.kit.property.material-1.10.17+d02c707b'
    def __init__(self, extension_path: typing.Optional[str] = None, add_context_menu = False, title = 'Materials on selected models', material_purpose = '', filter_fn = None, get_materials_async_fn = None, **kwargs):
        """
        Initializes a new instance of the MaterialBindingWidget.
        """
    def _build_binding_info(self, inherited: bool, style_name: str, material_list: typing.List[str], material_path: str, strength_value: str, bound_prim_list: typing.Set[str], material_missing: bool, on_material_fn: callable, on_strength_fn: callable, on_goto_fn: callable, on_dragdrop_fn: callable):
        ...
    def _build_combo(self, material_list: typing.List[str], material_index: int, on_fn: callable):
        ...
    def _build_material_popup(self, material_list: typing.List[str], material_index: int, thumbnail_image: omni.ui._ui.Button, bound_prim_list: typing.Set[pxr.Usd.Prim], material_missing: bool, bind_material_fn: callable, on_goto_fn: callable, on_dragdrop_fn: callable):
        ...
    def _get_index(self, items: typing.List[str], value: str, default_value: int = 0):
        ...
    def _get_prim(self, prim_path):
        ...
    def _get_theme_name(self, darkname, lightname):
        ...
    def _get_type_label_and_bounded_prims(self, bound_prim_list: typing.Set[str]):
        ...
    def _materials_changed(self):
        ...
    def _on_usd_changed(self, notice, stage):
        ...
    def _show_material_popup(self, name_field: omni.ui._ui.StringField, material_index: int, bind_material_fn: callable):
        ...
    def bind_material_to_prims(self, bind_material_path, items):
        """
        Binds a material to prims.
        
                Args:
                    bind_material_path (str): Path of the material to bind.
                    items (List[Tuple]): List of items to bind the material to.
        """
    def build_bound_widget(self, type_label, prim_style, bound_prims):
        """
        Builds a widget showing the bound type and prims.
        
                Args:
                    type_label (str): Label indicating the type (Prim or Collection).
                    prim_style (str): Style of the primary label.
                    bound_prims (str): Label showing the bound prims or collections.
        """
    def build_items(self):
        """
        Builds the items for the widget based on the current payload.
        """
    def build_strength_widget(self, strength_value, on_strength_fn):
        """
        Builds a widget for adjusting material binding strength.
        
                Args:
                    strength_value (str): Initial strength value.
                    on_strength_fn (callable): Function to call when strength is changed.
        """
    def build_thumbnail_widget(self, style_name, material_path, index):
        """
        Builds a thumbnail widget.
        
                Args:
                    style_name (str): Style name for the thumbnail widget.
                    material_path (str): Path of the material for the thumbnail.
                    index (int): Index of the thumbnail in the list.
        
                Returns:
                    ui.Button: A UI button with the thumbnail image.
        """
    def clean(self):
        """
        Cleans up the widget's resources.
        """
    def get_on_dragdrop_callback(self):
        """
        Gets a callback for handling drag and drop operations.
        
                Returns:
                    callable: A callback function.
        """
    def get_on_material_changed_callback(self, material_list):
        """
        Gets a callback for when the material selection changes.
        
                Args:
                    material_list (List[str]): List of available materials.
        
                Returns:
                    callable: A callback function.
        """
    def get_on_material_goto_callback(self):
        """
        Gets a callback for navigating to a material.
        
                Returns:
                    callable: A callback function.
        """
    def get_on_strength_changed_callback(self):
        """
        Gets a callback for when the material strength changes.
        
                Returns:
                    callable: A callback function.
        """
    def on_new_payload(self, payload):
        """
        Handles a new payload for the widget.
        
                Args:
                    payload (Dict): The new payload to be handled by the widget.
        
                Returns:
                    bool: True if the payload is valid and handled; False otherwise.
        """
    def reset(self):
        """
        Resets the widget to its initial state.
        """
LABEL_HEIGHT: int = 18
