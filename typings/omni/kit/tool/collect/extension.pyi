"""
This module provides classes and functions to facilitate the USD asset collection workflow within Omniverse Kit by offering UI components and logic to collect USD files and their dependencies into a single directory.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit import notification_manager as nm
from omni.kit.tool.collect.actions import ActionManager
from omni.kit.tool.collect.folder_collect_helper import FolderCollectHelper
from omni.kit.tool.collect.main_window import CollectMainWindow
from omni.kit.tool.collect.progress_popup import ProgressPopup
from omni.kit.usd.collect.collector import Collector
from omni.kit.usd.collect.collector import DefaultPrimOnlyOptions
from omni.kit.usd.collect.collector import FlatCollectionTextureOptions
from omni.kit.widget.prompt.prompt import PromptButtonInfo
from omni.kit.widget.prompt.prompt import PromptManager
import os as os
import pathlib
from pathlib import Path
from pxr import Sdf
import toml as toml
from urllib.parse import unquote
import weakref as weakref
__all__ = ['ACTION_COLLECT_STAGE', 'ActionManager', 'CollectMainWindow', 'Collector', 'DefaultPrimOnlyOptions', 'FlatCollectionTextureOptions', 'FolderCollectHelper', 'ICON_PATH', 'MenuItemDescription', 'Path', 'ProgressPopup', 'PromptButtonInfo', 'PromptManager', 'PublicExtension', 'Sdf', 'asyncio', 'carb', 'g_singleton', 'get_instance', 'nm', 'omni', 'os', 'toml', 'unquote', 'weakref']
class PublicExtension(omni.ext._extensions.IExt):
    """
    A class to handle USD asset collection in Omniverse.
    
        This class provides methods to collect USD files and their dependencies into a single directory, handling individual USDs, multiple USDs, and USDs within folders. It integrates with Omniverse Kit extensions to enhance the user experience with context menus and progress popups, offering a seamless asset collection workflow within the content browser. The class ensures that only writable USD file types can be collected and provides informative popups for unsupported files or other user feedback.
        
    """
    def _get_collection_dir(self, folder, usd_file_name):
        ...
    def _get_multi_files_progress_popup(self):
        ...
    def _is_folder(self, path):
        ...
    def _on_checkpoint_menu_click(self, menu, value):
        ...
    def _on_context_menu_click(self, menu, value):
        ...
    def _refresh_current_directory(self):
        ...
    def _register_menus(self):
        ...
    def _show_file_not_supported_popup(self):
        ...
    def _show_folder_exist_popup(self, usd_path, collect_dir, usd_only, flat_collection, material_only, texture_option, finish_callback: typing.Callable[[], NoneType] = None, default_prim_only = False, default_prim_option = ..., usda_to_usdc = False):
        ...
    def _show_folder_exist_popup_for_multi_files(self, current_index, total, path_provider, collect_dir, usd_only, flat_collection, material_only, texture_option, finish_callback, default_prim_only, default_prim_option = ..., usda_to_usdc = False):
        ...
    def _show_main_multi_files_window(self, usd_paths, folder_name, target_folder, finish_callback: typing.Callable[[], NoneType] = None):
        ...
    def _show_main_window(self, usd_path, finish_callback: typing.Callable[[], NoneType] = None):
        ...
    def _show_progress_popup(self):
        ...
    def _start_collecting(self, usd_path, collect_folder, usd_only, flat_collection, material_only, texture_option, finish_callback: typing.Callable[[], NoneType] = None, default_prim_only = False, default_prim_option = ..., usda_to_usdc = False):
        ...
    def _start_collecting_multi_files(self, current_index, total, path_provider, collect_dir, usd_only, flat_collection, material_only, texture_option, finish_callback, default_prim_only, default_prim_option = ..., usda_to_usdc = False):
        ...
    def collect(self, filepath: str, finish_callback: typing.Callable[[], NoneType] = None) -> None:
        """
        
                Collect a usd file.
                Args:
                    filepath: Path to usd file to be collected.
                
        """
    def collect_multiple(self, filepaths: str, folder_name: str, target_folder: str = '', finish_callback: typing.Callable[[], NoneType] = None) -> None:
        """
        
                Collect usd files.
                Args:
                    filepaths: Paths to usd file to be collected.
                    folder_name: Target folder name to save collect files.
                    target_folder: Target folder to save collect folder.
                
        """
    def collect_multiple_in_folder(self, folder: str, target_name: str = '', target_folder: str = '', finish_get_files_callback: typing.Callable[[], NoneType] = None, finish_collect_callback: typing.Callable[[], NoneType] = None) -> None:
        """
        
                Collect all usd files in a folder.
                Args:
                    folder: Paths to contain usd files to be collected.
                    target_name: Target folder name to save collect files.
                    target_folder: Target folder to save collect folder.
                    finish_get_files_callback: Will called when finish get all files in folder.
                    finish_collect_callback: Will called when finish collect all files in folder.
                
        """
    def get_content_folder(self):
        """
        
                Retrieves the content folder path that in ov launcher's settings.
        
                Returns:
                    str: The content folder path.
                
        """
    def get_content_window(self):
        """
        
                Retrieves the content window instance.
        
                Returns:
                    :'obj': The content window instance.
                
        """
    def on_shutdown(self):
        """
        Clean up the menus and destroy the collect window on extension shutdown.
        """
    def on_startup(self):
        """
        Initializes the menus and action on extension startup.
        """
def _exists_sync(path):
    ...
def get_instance():
    """
    Returns the singleton instance of the collect extension.
    
        Returns:
            The singleton instance of the collect extension.
    """
ACTION_COLLECT_STAGE: str = 'collect_stage'
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.tool.collect-2.2.16+d02c707b/icons')
g_singleton: PublicExtension  # value = <omni.kit.tool.collect.extension.PublicExtension object>
