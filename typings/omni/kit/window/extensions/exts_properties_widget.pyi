"""
This module provides a widget for managing and displaying properties of extensions in an application, including UI components for extension paths, registries, and cache, as well as options for exporting extension data.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.window.extensions.common import SettingBoolValue
from omni.kit.window.extensions.common import get_options
from omni.kit.window.extensions.exts_list_widget import ExtSummaryItem
from omni.kit.window.extensions.exts_properties_paths import ExtsPathsWidget
from omni.kit.window.extensions.exts_properties_registries import ExtsRegistriesWidget
from omni.kit.window.extensions.styles import get_style
from omni.kit.window.extensions.utils import cleanup_folder
from omni.kit.window.extensions.utils import copy_text
from omni.kit.window.extensions.utils import ext_id_to_name_version
from omni.kit.window.extensions.utils import get_setting
from omni.kit.window.extensions.utils import version_to_str
from omni import ui
__all__: list = ['ExtsPropertiesWidget']
class ExtsPropertiesWidget:
    """
    A widget class used within an application to manage and display properties of extensions.
    
        This class provides functionality to manage extension properties, such as search paths and registries, and to clean and export extension data. It includes a user interface composed of various collapsable frames that allow users to interact with extension settings, view extension summaries, and perform actions such as opening extension paths or clearing extension caches.
    
        The widget is designed to be integrated into applications that support extension management and requires an extension manager to function. It subscribes to extension change events to refresh its contents dynamically.
        
    """
    def __init__(self):
        """
        Initialize the extension properties widget.
        """
    def _clean_widgets(self):
        ...
    def _refresh(self):
        ...
    def destroy(self):
        """
        Cleans up the widget and its subscriptions.
        """
    def export_all_exts(self, ext_summaries):
        """
        Export all exts in CSV format with some of config params. print and copy result.
        
                Args:
                    ext_summaries (list): A list of extension summaries to export.
        """
    def export_enabled_exts_as_kit_file(self, only_top_level = True):
        """
        Export all topmost exts in .kit format. print and copy result.
        
                Args:
                    only_top_level (bool): Whether to export only top-level extensions.
        """
    def set_visible(self, visible):
        """
        Sets the visibility of the widget.
        
                Args:
                    visible (bool): Whether the widget should be visible.
        """
COMMUNITY_TAB_TOGGLE_EVENT: int = 17022095773621968051
