"""
This module provides a user interface for managing and interacting with extensions in the application, including features for controlling extension activation, viewing detailed information, and managing settings.
"""
from __future__ import annotations
from omni.kit.window.extensions.ext_commands import ToggleExtension
from omni.kit.window.extensions.ext_components import SimpleCheckBox
from omni.kit.window.extensions.extension import ExtsWindowExtension
from omni.kit.window.extensions.extension import get_instance
from . import common
from . import ext_commands
from . import ext_components
from . import ext_controller
from . import ext_data_fetcher
from . import ext_export_import
from . import ext_info_widget
from . import ext_status_bar
from . import extension
from . import exts_dependency_window
from . import exts_list_widget
from . import exts_properties_paths
from . import exts_properties_registries
from . import exts_properties_widget
from . import markdown_renderer
from . import styles
from . import utils
from . import window
__all__: list = ['ToggleExtension', 'get_instance', 'ExtsWindowExtension']
