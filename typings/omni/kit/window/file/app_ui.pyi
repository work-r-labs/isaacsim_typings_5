"""
USD File interaction for Omniverse Kit.

:mod:`omni.kit.window.file` provides util functions to new/open/save/close USD files. It handles file picking dialog and prompt
for unsaved stage.
"""
from __future__ import annotations
import carb as carb
import enum
from enum import Enum
from omni.kit.window.file.prompt_ui import Prompt
from omni.kit.window.file.save_stage_ui import StageSaveDialog
from omni.kit.window.file.style import get_style
from omni.kit.window.file_exporter import get_file_exporter
import omni.kit.window.filepicker.detail_view
from omni.kit.window.filepicker.detail_view import DetailFrameController as ExportOptionsDelegate
from omni.kit.window.filepicker.detail_view import DetailFrameController as ImportOptionsDelegate
from omni import ui
import omni.ui._ui
import os as os
import typing
__all__: list = ['DialogOptions', 'SaveOptionsDelegate', 'OpenOptionsDelegate', 'AppUI']
class AppUI:
    """
     Wrapper class for open/save prompts.
    """
    def __init__(self):
        ...
    def _cancel_save(self, new_root_path, checkpoint_comment = ''):
        ...
    def _dont_save_layers(self, new_root_path, on_save_done = None, checkpoint_comment = ''):
        ...
    def _save_layers(self, new_root_path, dirty_layers, on_save_done = None, create_checkpoint = True, checkpoint_comment = ''):
        ...
    def destroy(self):
        """
        Destructor.
        """
    def save_root_and_sublayers(self, new_root_path: str, dirty_sublayers: typing.List[str], on_save_done: typing.Callable = None, dialog_options: int = ..., save_comment: str = '', allow_skip_sublayers: bool = False):
        """
        
                Save root and sub layers.
        
                Args:
                    new_root_path (str): path to set the root layer.
                    dirty_layers (List[str]): layer identifiers to save.
                Keyword Args:
                    on_save_done (Callable): function to call after saving. Function Signature:
                        on_save_done(result: bool, url: str) -> None
                    dialog_options (:obj:`DialogOptions`): dialog options to prompt or not.
                    save_comment (str): comment on the created checkpoint.
                    allow_skip_sublayers (bool): True to skip sublayers.
                
        """
    def show_open_stage_failed_prompt(self, path):
        """
        
                Show open stage failed prompt with the given path.
                Args:
                    path(str): The path to show the failed prompt with.
                
        """
    def show_save_layers_failed_prompt(self):
        """
         Show save layers failed prompt. 
        """
class DialogOptions(enum.Enum):
    """
    Enum for dialog options.
    """
    FORCE: typing.ClassVar[DialogOptions]  # value = <DialogOptions.FORCE: (1,)>
    HIDE: typing.ClassVar[DialogOptions]  # value = <DialogOptions.HIDE: (2,)>
    NONE: typing.ClassVar[DialogOptions]  # value = <DialogOptions.NONE: (0,)>
class OpenOptionsDelegate(omni.kit.window.filepicker.detail_view.DetailFrameController):
    """
     Delegate class managing open options. 
    """
    def __init__(self):
        ...
    def _build_ui_impl(self):
        ...
    def _destroy_impl(self, _):
        ...
    def should_load_payload(self) -> bool:
        """
        
                Return:
                    bool: Return True if payload should be loaded.
                
        """
class SaveOptionsDelegate(omni.kit.window.filepicker.detail_view.DetailFrameController):
    """
     Delegate class managing save options. 
    """
    def __init__(self):
        ...
    def _build_option_checkbox(self, text, default_value, tooltip, identifier):
        ...
    def _build_options_box(self, server_url: str, checkpoint_enabled: bool):
        ...
    def _build_ui_impl(self):
        ...
    def _destroy_impl(self, _):
        ...
    def _on_begin_edit(self, model):
        ...
    def _on_end_edit(self, model: omni.ui._ui.AbstractValueModel):
        ...
    def get_comment(self) -> str:
        """
        
                Return:
                    str: Return the comment text.
                
        """
    def include_session_layer(self) -> bool:
        """
        
                When doing save-as or save-flattened-as, this option
                can tell if it needs to keep session layers's change or
                flatten session layer's change also.
                Return:
                    bool: Return whether to include session layer or not.
                
        """
    @property
    def show_include_session_layer_option(self):
        """
        Get/set whether to show the include session layer option or not.
        """
    @show_include_session_layer_option.setter
    def show_include_session_layer_option(self, value):
        ...
SHOW_SAVE_OPTIONS: str = '/persistent/app/file/save/showSaveOptionsAutomatically'
have_versioning: bool = False
