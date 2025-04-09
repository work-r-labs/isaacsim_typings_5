"""
USD File interaction for Omniverse Kit.

:mod:`omni.kit.window.file` provides util functions to new/open/save/close USD files. It handles file picking dialog and prompt for unsaved stage.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.kit.helper import file_utils
from omni.kit.helper.file_utils import asset_types
from omni.kit.window.file.app_ui import AppUI
from omni.kit.window.file.app_ui import DialogOptions
from omni.kit.window.file.app_ui import OpenOptionsDelegate
from omni.kit.window.file.app_ui import SaveOptionsDelegate
from omni.kit.window.file.file_actions import deregister_actions
from omni.kit.window.file.file_actions import register_actions
from omni.kit.window.file.prompt_ui import Prompt
from omni.kit.window.file.read_only_options_window import ReadOnlyOptionsWindow
from omni.kit.window.file_exporter import get_file_exporter
from omni.kit.window.file_importer import get_file_importer
import os as os
from pxr import Sdf
from pxr import Tf
from pxr import Usd
from pxr import UsdGeom
from pxr import UsdUtils
import time as time
import traceback as traceback
__all__: list = ['FileWindowExtension', 'FileUtils', 'get_file_utils_instance', 'get_instance', 'new', 'open', 'open_stage', 'open_with_new_edit_layer', 'reopen', 'save', 'save_as', 'close', 'save_layers', 'prompt_if_unsaved_stage', 'add_reference', 'register_open_stage_addon', 'register_open_stage_complete']
class FileUtils:
    """
     File utils class to provide file relate function. 
    """
    @staticmethod
    def _exclusive_task_wrapper(job: typing.Awaitable, *args):
        ...
    @staticmethod
    def post_notification(message: str, info: bool = False, duration: int = 3):
        """
        
                Post a notification message.
        
                Args:
                    message (str): message text.
                    info (bool): If True, post the message as info or otherwise warning.
                    duration (int): Duration of notification, in seconds.
                
        """
    def _on_stage_event(self, event):
        ...
    def _show_file_existed_prompt(self, path, on_confirm_fn, on_cancel_fn = None):
        ...
    def _show_readonly_usd_prompt(self, ok_fn, middle_fn):
        ...
    def add_reference(self, is_payload = False):
        """
        
                Prompt for the file to add reference or payload to.
        
                Keyword Args:
                    is_payload (bool): True to add payload instead of reference.
                
        """
    def close(self, on_closed: typing.Callable[[], NoneType], fast_shutdown = False):
        """
        
                Check if current stage is dirty. If it's dirty, it will ask if to save the file, then close stage.
        
                Args:
                    on_closed (Callable): function to call after closing, Function Signature:
                        on_closed() -> None
        
                Keyword Args:
                    fast_shutdown (bool): clear pending edits immediately to shutdown faster.
                
        """
    def create_stage(self, edit_layer_path: str, file_path: str, callback: typing.Callable = None):
        """
        
                Create a stage with edit layer from paths.
        
                Args:
                    edit_layer_path (str): path to create the edit layer.
                    file_path (str): path to create the stage.
                Keyword Args:
                    callback: (Callable): callback to call after creating stage. Function Signature:
                        callback() -> None
                
        """
    def new(self, template = None):
        """
        
                Create a new USD stage. If currently opened stage is dirty, a prompt will show to let you save it.
        
                Keyword Args:
                    template (Optional[str]): the template to use.
                
        """
    def on_shutdown(self):
        """
         Cleanup the extension. 
        """
    def on_startup(self):
        """
        
                Initialize the FileUtils.
                
        """
    def open(self, open_loadset = ...):
        """
        
                Bring up a file picker to choose a USD file to open. If currently opened stage is dirty, a prompt will show to let you save it.
        
                Keyword Args:
                    open_loadset (:obj:`omni.usd.UsdContextInitialLoadSet`): initial load set enum, LOAD_ALL or LOAD_NONE.
                
        """
    def open_stage(self, path: str, open_loadset = ..., open_options: omni.kit.window.file.app_ui.OpenOptionsDelegate = None):
        """
        
                Open stage. If the current stage is dirty, a prompt will show to let you save it.
        
                Args:
                    path(str): the path to the stage file to open.
                Keyword Args:
                    open_loadset(:obj:`omni.usd.UsdContextInitialLoadSet`): initial load set enum, LOAD_ALL or LOAD_NONE.
                    open_options(:obj:`OpenOptionsDelegate`): if set, use the open_loadset setting from options.
                
        """
    def open_with_new_edit_layer(self, path: str, open_loadset: int = ..., callback: typing.Callable[[], NoneType] = None):
        """
        
                Open stage and create a new edit layer.
        
                Args:
                    path (str): path to open the stage.
                Keyword Args:
                    open_loadset (:obj:`omni.usd.UsdContextInitialLoadSet`): initial load set enum, LOAD_ALL or LOAD_NONE.
                    callback: (Callable): callback to call after creating stage. Function Signature:
                        callback() -> None
                
        """
    def prompt_if_unsaved_stage(self, callback: typing.Callable[[], NoneType]):
        """
        
                Check if current stage is dirty. If it's dirty, ask to save the file, then execute callback. Otherwise runs callback directly.
        
        
                Args:
                    callback (Callable): function to call upon saving. Function Signature:
                        callback() -> None
                
        """
    def register_open_stage_addon(self, callback: typing.Callable[[], NoneType]):
        """
        
                Register callback to call when opening a stage.
        
                Args:
                    callback (Callable): function to call. Function Signature:
                        callback() -> None
                Return:
                    :obj:`_CallbackRegistrySubscription`: The callback subscription.
                
        """
    def register_open_stage_complete(self, callback: typing.Callable[[], NoneType]):
        """
        
                Register callback to call when finish opening a stage.
        
                Args:
                    callback (Callable): function to call. Function Signature:
                        callback() -> None
                Return:
                    :obj:`_CallbackRegistrySubscription`: The callback subscription.
                
        """
    def reopen(self):
        """
        Reopen currently opened stage. If the stage is dirty, a prompt will show to let you save it.
        """
    def save(self, callback: typing.Callable[[bool, str], NoneType], allow_skip_sublayers: bool = False, dialog_options = ...):
        """
        
                Save currently opened stage to file. Will call Save As for a newly created stage.
        
                Keyword Args:
                    callback (Callable): function to call after saving. Function Signature:
                        callback(result: bool, url: str) -> None
                    allow_skip_sublayers (bool): True to skip sublayers.
                    dialog_options (:obj:`DialogOptions`): options for opening the dialog.
                
        """
    def save_as(self, flatten: bool, callback: typing.Callable[[bool, str], NoneType], allow_skip_sublayers: bool = False):
        """
        
                Bring up a file picker to choose a file to save current stage to.
        
                Args:
                    flatten (bool): Whether to flatten the stage or not.
        
                Keyword Args:
                    callback (Callable): function to call after saving. Function Signature:
                        callback(result: bool, url: str) -> None
                    allow_skip_sublayers (bool): True to skip sublayers.
                
        """
    def save_layers(self, new_root_path: str, dirty_layers: typing.List[str], on_save_done: typing.Callable[[bool, str], NoneType], create_checkpoint = True, checkpoint_comment = ''):
        """
        
                Save current layers.
        
                Args:
                    new_root_path (str): path to set the root layer.
                    dirty_layers (List[str]): layer identifiers to save.
                    on_save_done (Callable): function to call after saving. Function Signature:
                        on_save_done(result: bool, url: str) -> None
        
                Keyword Args:
                    create_checkpoint (bool): true to create checkpoints.
                    checkpoint_comments (str): comment on the created checkpoint.
                
        """
    def save_stage(self, path: str, callback: typing.Callable[[bool, str], NoneType] = None, flatten: bool = False, save_options: omni.kit.window.file.app_ui.SaveOptionsDelegate = None, allow_skip_sublayers: bool = False):
        """
        
                Save current stage to the given path, if the path exists bring up the filepicker to choose a potential new path.
        
                Args:
                    path (str): path to save the file.
        
                Keyword Args:
                    callback (Callable): function to call after saving. Function Signature:
                        callback(result: bool, url: str) -> None
                    flatten (bool): whether to flatten the stage or not.
                    save_options (:obj:`SaveOptionsDelegate`): if set, load save settings from it.
                    allow_skip_sublayers (bool): True to skip sublayers.
                
        """
    def stop_timeline(self):
        """
         Stop the timeline. 
        """
class FileWindowExtension(omni.ext._extensions.IExt):
    """
     File window extension interface. 
    """
    @staticmethod
    def add_reference(*args, **kwargs):
        """
        
                Prompt for the file to add reference or payload to.
        
                Keyword Args:
                    is_payload (bool): True to add payload instead of reference.
                
        """
    @staticmethod
    def close(*args, **kwargs):
        """
        
                Check if current stage is dirty. If it's dirty, it will ask if to save the file, then close stage.
        
                Args:
                    on_closed (Callable): function to call after closing, Function Signature:
                        on_closed() -> None
        
                Keyword Args:
                    fast_shutdown (bool): clear pending edits immediately to shutdown faster.
                
        """
    @staticmethod
    def create_stage(*args, **kwargs):
        """
        
                Create a stage with edit layer from paths.
        
                Args:
                    edit_layer_path (str): path to create the edit layer.
                    file_path (str): path to create the stage.
                Keyword Args:
                    callback: (Callable): callback to call after creating stage. Function Signature:
                        callback() -> None
                
        """
    @staticmethod
    def new(*args, **kwargs):
        """
        
                Create a new USD stage. If currently opened stage is dirty, a prompt will show to let you save it.
        
                Keyword Args:
                    template (Optional[str]): the template to use.
                
        """
    @staticmethod
    def open(*args, **kwargs):
        """
        
                Bring up a file picker to choose a USD file to open. If currently opened stage is dirty, a prompt will show to let you save it.
        
                Keyword Args:
                    open_loadset (:obj:`omni.usd.UsdContextInitialLoadSet`): initial load set enum, LOAD_ALL or LOAD_NONE.
                
        """
    @staticmethod
    def open_stage(*args, **kwargs):
        """
        
                Open stage. If the current stage is dirty, a prompt will show to let you save it.
        
                Args:
                    path(str): the path to the stage file to open.
                Keyword Args:
                    open_loadset(:obj:`omni.usd.UsdContextInitialLoadSet`): initial load set enum, LOAD_ALL or LOAD_NONE.
                    open_options(:obj:`OpenOptionsDelegate`): if set, use the open_loadset setting from options.
                
        """
    @staticmethod
    def open_with_new_edit_layer(*args, **kwargs):
        """
        
                Open stage and create a new edit layer.
        
                Args:
                    path (str): path to open the stage.
                Keyword Args:
                    open_loadset (:obj:`omni.usd.UsdContextInitialLoadSet`): initial load set enum, LOAD_ALL or LOAD_NONE.
                    callback: (Callable): callback to call after creating stage. Function Signature:
                        callback() -> None
                
        """
    @staticmethod
    def post_notification(*args, **kwargs):
        """
        
                Post a notification message.
        
                Args:
                    message (str): message text.
                    info (bool): If True, post the message as info or otherwise warning.
                    duration (int): Duration of notification, in seconds.
                
        """
    @staticmethod
    def prompt_if_unsaved_stage(*args, **kwargs):
        """
        
                Check if current stage is dirty. If it's dirty, ask to save the file, then execute callback. Otherwise runs callback directly.
        
        
                Args:
                    callback (Callable): function to call upon saving. Function Signature:
                        callback() -> None
                
        """
    @staticmethod
    def register_open_stage_addon(*args, **kwargs):
        """
        
                Register callback to call when opening a stage.
        
                Args:
                    callback (Callable): function to call. Function Signature:
                        callback() -> None
                Return:
                    :obj:`_CallbackRegistrySubscription`: The callback subscription.
                
        """
    @staticmethod
    def register_open_stage_complete(*args, **kwargs):
        """
        
                Register callback to call when finish opening a stage.
        
                Args:
                    callback (Callable): function to call. Function Signature:
                        callback() -> None
                Return:
                    :obj:`_CallbackRegistrySubscription`: The callback subscription.
                
        """
    @staticmethod
    def reopen(*args, **kwargs):
        """
        Reopen currently opened stage. If the stage is dirty, a prompt will show to let you save it.
        """
    @staticmethod
    def save(*args, **kwargs):
        """
        
                Save currently opened stage to file. Will call Save As for a newly created stage.
        
                Keyword Args:
                    callback (Callable): function to call after saving. Function Signature:
                        callback(result: bool, url: str) -> None
                    allow_skip_sublayers (bool): True to skip sublayers.
                    dialog_options (:obj:`DialogOptions`): options for opening the dialog.
                
        """
    @staticmethod
    def save_as(*args, **kwargs):
        """
        
                Bring up a file picker to choose a file to save current stage to.
        
                Args:
                    flatten (bool): Whether to flatten the stage or not.
        
                Keyword Args:
                    callback (Callable): function to call after saving. Function Signature:
                        callback(result: bool, url: str) -> None
                    allow_skip_sublayers (bool): True to skip sublayers.
                
        """
    @staticmethod
    def save_layers(*args, **kwargs):
        """
        
                Save current layers.
        
                Args:
                    new_root_path (str): path to set the root layer.
                    dirty_layers (List[str]): layer identifiers to save.
                    on_save_done (Callable): function to call after saving. Function Signature:
                        on_save_done(result: bool, url: str) -> None
        
                Keyword Args:
                    create_checkpoint (bool): true to create checkpoints.
                    checkpoint_comments (str): comment on the created checkpoint.
                
        """
    @staticmethod
    def save_stage(*args, **kwargs):
        """
        
                Save current stage to the given path, if the path exists bring up the filepicker to choose a potential new path.
        
                Args:
                    path (str): path to save the file.
        
                Keyword Args:
                    callback (Callable): function to call after saving. Function Signature:
                        callback(result: bool, url: str) -> None
                    flatten (bool): whether to flatten the stage or not.
                    save_options (:obj:`SaveOptionsDelegate`): if set, load save settings from it.
                    allow_skip_sublayers (bool): True to skip sublayers.
                
        """
    @staticmethod
    def stop_timeline(*args, **kwargs):
        """
         Stop the timeline. 
        """
    def on_shutdown(self):
        """
         Cleanup the extension. 
        """
    def on_startup(self, ext_id):
        """
        
                Initialize the extension.
                Args:
                    ext_id(str): Extension identifier.
                
        """
class _CallbackRegistrySubscription:
    """
    
        Simple subscription.
    
        _Event has callback while this object exists.
        
    """
    def __del__(self):
        """
        Called by GC.
        """
    def __init__(self, callback_list: typing.List, callback: typing.Callable):
        """
        
                Save the callback in the given list.
                
        """
class _CheckpointCommentContext:
    def __enter__(self):
        ...
    def __exit__(self, type, value, trace):
        ...
    def __init__(self, comment: str):
        ...
def add_reference(is_payload = False):
    """
    
        Prompt for the file to add reference or payload to.
    
        Keyword Args:
            is_payload (bool): True to add payload instead of reference.
        
    """
def close(on_closed: typing.Optional[typing.Callable[[], NoneType]] = None):
    """
    
        Check if current stage is dirty. If it's dirty, it will ask if to save the file, then close stage.
    
        Keyword Args:
            on_closed (Callable): function to call after closing, Function Signature:
                on_closed() -> None
        
    """
def create_stage(self, edit_layer_path: str, file_path: str, callback: typing.Callable = None):
    """
    
        Create a stage with edit layer from paths.
    
        Args:
            edit_layer_path (str): path to create the edit layer.
            file_path (str): path to create the stage.
        Keyword Args:
            callback: (Callable): callback to call after creating stage. Function Signature:
                callback() -> None
        
    """
def get_file_utils_instance():
    """
    Get the file utils instance.
    """
def new(template = None):
    """
    
        Create a new USD stage. If currently opened stage is dirty, a prompt will show to let you save it.
    
        Keyword Args:
            template (Optional[str]): the template to use.
        
    """
def open(open_loadset = ...):
    """
    
        Bring up a file picker to choose a USD file to open. If currently opened stage is dirty, a prompt will show to let you save it.
    
        Keyword Args:
            open_loadset (:obj:`omni.usd.UsdContextInitialLoadSet`): initial load set enum, LOAD_ALL or LOAD_NONE.
        
    """
def open_stage(path: str, open_loadset = ...):
    """
    
        Open stage. If the current stage is dirty, a prompt will show to let you save it.
    
        Args:
            path (str): path to open the stage.
        Keyword Args:
            open_loadset (:obj:`omni.usd.UsdContextInitialLoadSet`): initial load set enum, LOAD_ALL or LOAD_NONE.
        
    """
def open_with_new_edit_layer(path: str, open_loadset = ..., callback: typing.Callable[[], NoneType] = None):
    """
    
        Open stage and create a new edit layer.
    
        Args:
            path (str): path to open the stage.
        Keyword Args:
            open_loadset (:obj:`omni.usd.UsdContextInitialLoadSet`): initial load set enum, LOAD_ALL or LOAD_NONE.
            callback: (Callable): callback to call after creating stage. Function Signature:
                callback() -> None
        
    """
def prompt_if_unsaved_stage(job: typing.Callable[[], NoneType]):
    """
    
        Check if current stage is dirty. If it's dirty, ask to save the file, then execute callback. Otherwise runs callback directly.
    
        Args:
            job (Callable): function to call upon saving. Function Signature:
                job() -> None
        
    """
def register_open_stage_addon(callback):
    """
    
        Register callback to call when opening a stage.
    
        Args:
            callback (Callable): function to call. Function Signature:
                callback() -> None
        Return:
            :obj:`_CallbackRegistrySubscription`: The callback subscription.
        
    """
def register_open_stage_complete(callback):
    """
    
        Register callback to call when finish opening a stage.
    
        Args:
            callback (Callable): function to call. Function Signature:
                callback() -> None
        Return:
            :obj:`_CallbackRegistrySubscription`: The callback subscription.
        
    """
def reopen():
    """
    Reopen currently opened stage. If the stage is dirty, a prompt will show to let you save it.
    """
def save(on_save_done: typing.Optional[typing.Callable[[bool, str], NoneType]] = None, exit = False, dialog_options = ...):
    """
    
        Save currently opened stage to file. Will call Save As for a newly created stage.
    
        Keyword Args:
            on_save_done (Callable): function to call after saving. Function Signature:
                on_save_done(result: bool, url: str) -> None
            exit(bool): Unused parameter.
            dialog_options (:obj:`DialogOptions`): options for opening the dialog.
        
    """
def save_as(flatten, on_save_done: typing.Optional[typing.Callable[[bool, str], NoneType]] = None):
    """
    
        Bring up a file picker to choose a file to save current stage to.
    
        Args:
            flatten (bool): Whether to flatten the stage or not.
    
        Keyword Args:
            on_save_done (Callable): function to call after saving. Function Signature:
                on_save_done(result: bool, url: str) -> None
        
    """
def save_layers(new_root_path, dirty_layers, on_save_done, create_checkpoint = True, checkpoint_comment = ''):
    """
    
        Save current layers.
    
        Args:
            new_root_path (str): path to set the root layer.
            dirty_layers (List[str]): layer identifiers to save.
            on_save_done (Callable): function to call after saving. Function Signature:
                on_save_done(result: bool, url: str) -> None
    
        Keyword Args:
            create_checkpoint (bool): true to create checkpoints.
            checkpoint_comments (str): comment on the created checkpoint.
        
    """
IGNORE_UNSAVED_ON_EXIT_PATH: str = '/app/file/ignoreUnsavedOnExit'
IGNORE_UNSAVED_STAGE: str = '/app/file/ignoreUnsavedStage'
SHOW_UNSAVED_LAYERS_DIALOG: str = '/persistent/app/file/save/showUnsavedLayersDialog'
_file_util_instance: FileUtils  # value = <omni.kit.window.file.file_window.FileUtils object>
have_nucleus: bool = True
