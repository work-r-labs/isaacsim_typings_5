"""

This extension provides util functions to new/open/save/close USD files. It handles file picking dialog and prompt for unsaved stage.
"""
from __future__ import annotations
from omni.kit.window.file.app_ui import DialogOptions
from omni.kit.window.file.file_window import FileUtils
from omni.kit.window.file.file_window import FileWindowExtension
from omni.kit.window.file.file_window import add_reference
from omni.kit.window.file.file_window import close
from omni.kit.window.file.file_window import get_file_utils_instance
from omni.kit.window.file.file_window import new
from omni.kit.window.file.file_window import open
from omni.kit.window.file.file_window import open_stage
from omni.kit.window.file.file_window import open_with_new_edit_layer
from omni.kit.window.file.file_window import prompt_if_unsaved_stage
from omni.kit.window.file.file_window import register_open_stage_addon
from omni.kit.window.file.file_window import register_open_stage_complete
from omni.kit.window.file.file_window import reopen
from omni.kit.window.file.file_window import save
from omni.kit.window.file.file_window import save_as
from omni.kit.window.file.file_window import save_layers
from omni.kit.window.file.prompt_ui import Prompt
from omni.kit.window.file.read_only_options_window import ReadOnlyOptionsWindow
from omni.kit.window.file.save_stage_ui import StageSaveDialog
from . import app_ui
from . import file_actions
from . import file_window
from . import prompt_ui
from . import read_only_options_window
from . import save_stage_ui
from . import style
__all__: list = ['FileWindowExtension', 'DialogOptions', 'get_instance', 'new', 'open', 'open_stage', 'open_with_new_edit_layer', 'reopen', 'save', 'save_as', 'close', 'save_layers', 'prompt_if_unsaved_stage', 'add_reference', 'register_open_stage_addon', 'register_open_stage_complete', 'ReadOnlyOptionsWindow', 'Prompt', 'StageSaveDialog']
