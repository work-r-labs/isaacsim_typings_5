"""
This module extends the edit menu functionality within an application, providing mechanisms to manipulate edit menu actions related to selection, duplication, deletion, and other common editing tasks for prims in a USD stage.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import contextlib as contextlib
from functools import partial
from isaacsim.gui.menu.edit_menu.edit_actions import deregister_actions
from isaacsim.gui.menu.edit_menu.edit_actions import register_actions
from isaacsim.gui.menu.edit_menu.selection import Selection
from isaacsim.gui.menu.edit_menu.selection_window import SelectionSetWindow
import omni as omni
from omni.kit.menu.utils.builder_utils import LayoutSourceSearch
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.layout import MenuLayout
from omni.kit import notification_manager as nm
from omni.kit.usd import layers
from omni import ui
import os as os
from pxr import Kind
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
import sys as sys
__all__: list = ['EditMenuExtension', 'get_extension_path']
class EditMenuExtension:
    @staticmethod
    def _rename_viewport_active_camera(old_prim_name: pxr.Sdf.Path, new_prim_name: pxr.Sdf.Path):
        ...
    @staticmethod
    def can_be_instanced():
        """
        Can selected prims be instanced
        """
    @staticmethod
    def can_delete():
        """
        Can selected prims be deleted (prims do not have no_delete metadata
        """
    @staticmethod
    def can_prims_parent():
        """
        Can selected prims be Parented
        """
    @staticmethod
    def can_prims_unparent():
        """
        Can selected prims be Unparented
        """
    @staticmethod
    def capture_screenshot(on_complete_fn: callable = None):
        """
        Captures a screenshot of the active viewport or the entire application.
        
                Args:
                    on_complete_fn (callable, optional): A callback function that gets called upon completion of the screenshot capture. Defaults to None.
                
        """
    @staticmethod
    def create_xform_to_group() -> bool:
        """
        Groups the selected prims under a new Xform in the USD stage.
        """
    @staticmethod
    def deactivate_prims():
        """
        Deactivates the selected prim(s) in the USD stage.
        """
    @staticmethod
    def delete_prim(destructive):
        """
        Deletes the selected prim(s) from the USD stage.
        
                Args:
                    destructive (bool): If True, deletes the prims destructively.
        """
    @staticmethod
    def duplicate_prim(duplicate_layers, combine_layers):
        """
        Duplicates the selected prim(s) in the USD stage with options for layer handling.
        
                Args:
                    duplicate_layers (bool): If True, duplicates the prims across all layers.
                    combine_layers (bool): If True, duplicates the prims with references flattened.
        """
    @staticmethod
    def focus_prim():
        """
        Focuses the viewport camera on the selected prim(s).
        """
    @staticmethod
    def instance_prim():
        """
        Creates an instance of the selected prim(s) in the USD stage.
        """
    @staticmethod
    def is_in_live_session():
        """
        Is kit in live session
        """
    @staticmethod
    def is_not_in_live_session():
        """
        Is kit not in live session
        """
    @staticmethod
    def is_one_prim_selected():
        """
        Is a single prim selected
        """
    @staticmethod
    def parent_prims():
        """
        Parents the selected prims to the last selected prim in the USD stage.
        """
    @staticmethod
    def post_notification(message: str, info: bool = False, duration: int = 3):
        """
        Posts a notification message to the UI.
        
                Args:
                    message (str): The message to be displayed in the notification.
                    info (bool, optional): If True, displays an info notification; otherwise, a warning. Defaults to False.
                    duration (int, optional): The duration in seconds for which the notification should be visible. Defaults to 3.
                
        """
    @staticmethod
    def prim_selected():
        """
        Is one or more prims selected
        """
    @staticmethod
    def rename_prim(stage, prim, window, field_widget):
        """
        Renames the specified prim in the USD stage.
        
                Args:
                    stage (Usd.Stage): The stage where the prim resides.
                    prim (Usd.Prim): The prim to rename.
                    window (ui.Widget): The UI window associated with the rename operation.
                    field_widget (ui.StringField): The UI string field containing the new name for the prim.
        """
    @staticmethod
    def toggle_global_visibility():
        """
        Toggles the global visualization mode in the viewport.
        """
    @staticmethod
    def toggle_visibillity():
        """
        Toggles the visibility of the selected prim(s) in the viewport.
        """
    @staticmethod
    def ungroup_prims() -> bool:
        """
        Ungroups the selected prims in the USD stage.
        """
    @staticmethod
    def unparent_prims():
        """
        Unparents the selected prims in the USD stage.
        """
    def __del__(self):
        ...
    def __init__(self, ext_id):
        ...
    def _add_to_recent(self, description, selection):
        ...
    def _add_to_selection_set(self, description):
        ...
    def _build_edit_menu(self):
        ...
    def _build_recent_menu(self):
        ...
    def _build_selection_kind_menu(self):
        ...
    def _build_selection_set_menu(self):
        ...
    def _create_selection_set(self):
        ...
    def _on_select_by_kind(self, kind):
        ...
    def _on_select_recent(self, index):
        ...
    def _on_select_selection_set(self, index):
        ...
    def _on_stage_event(self, event):
        ...
    def _plugin_kinds(self):
        ...
    def _register_context_menu(self):
        ...
    def _register_page(self):
        ...
    def _unregister_context_menu(self):
        ...
    def _unregister_page(self):
        ...
    def _usd_kinds(self):
        ...
    def _usd_kinds_display(self):
        ...
    def get_screenshot_path(self, settings):
        """
        Get path to save screenshot.
        
                Args:
                    settings: carb.settings()
                
        """
    def menu_rename_prim_dialog(self):
        ...
def get_extension_path(sub_directory):
    """
    Retrieves the full path to a specified subdirectory within the extension's directory.
    
        Args:
            sub_directory (str): The name of the subdirectory within the extension's directory. If empty, returns the path to the extension's root directory.
    
        Returns:
            str: The normalized full path to the specified subdirectory within the extension's directory.
    """
CAPTURE_FRAME_PATH: str = '/app/captureFrame/path'
KEEP_TRANSFORM_FOR_REPARENTING: str = '/persistent/app/stage/movePrimInPlace'
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
_extension_instance: EditMenuExtension  # value = <isaacsim.gui.menu.edit_menu.edit_menu.EditMenuExtension object>
_extension_path: str = '/home/chris/isaacsim/exts/isaacsim.gui.menu'
