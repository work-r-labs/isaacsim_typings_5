"""
This module provides a user interface for managing and interacting with extensions in the application, including features for controlling extension activation, viewing detailed information, and managing settings.
"""
from __future__ import annotations
from omni.kit.window.extensions.common import ExtSource
from omni.kit.window.extensions.common import PageBase
from omni.kit.window.extensions.common import get_open_example_links
from omni.kit.window.extensions.ext_commands import ToggleExtension
from omni.kit.window.extensions.ext_components import SimpleCheckBox
from omni.kit.window.extensions.ext_controller import toggle_autoload
from omni.kit.window.extensions.ext_export_import import _ask_user_for_path
from omni.kit.window.extensions.ext_info_widget import ExtInfoWidget
from omni.kit.window.extensions.extension import ExtsWindowExtension
from omni.kit.window.extensions.extension import get_instance
from omni.kit.window.extensions.exts_list_widget import ExtsListWidget
from omni.kit.window.extensions.utils import ext_id_to_fullname
from omni.kit.window.extensions.utils import open_in_vscode_if_enabled
from omni.kit.window.extensions.utils import show_ok_popup
from omni.kit.window.extensions.utils import show_user_input_popup
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
__all__: list = ['ToggleExtension', 'get_instance', 'ExtsWindowExtension', 'SimpleCheckBox', 'ext_id_to_fullname', 'open_in_vscode_if_enabled', 'show_ok_popup', 'show_user_input_popup', 'PageBase', 'ExtInfoWidget', 'get_open_example_links', 'ExtSource', 'ExtsListWidget', '_ask_user_for_path', 'toggle_autoload']
