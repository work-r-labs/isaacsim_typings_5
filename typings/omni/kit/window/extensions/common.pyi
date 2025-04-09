"""
This module provides utilities for managing and interacting with extensions in the omni.kit.window.extensions framework.
"""
from __future__ import annotations
import abc as abc
import asyncio as asyncio
import carb as carb
import enum
from enum import Enum
from functools import lru_cache
import omni as omni
from omni.kit.window.extensions import ext_controller
from omni.kit.window.extensions.utils import get_ext_info_dict
from omni.kit.window.extensions.utils import get_extpath_git_ext
from omni.kit.window.extensions.utils import get_setting
from omni.kit.window.extensions.utils import set_default_and_get_setting
from omni.kit.window.extensions.utils import show_ok_popup
import os as os
from string import Template
import typing
__all__: list = list()
class ExtAuthorGroup(enum.Enum):
    """
    An enumeration.
    """
    COMMUNITY_UNVERIFIED: typing.ClassVar[ExtAuthorGroup]  # value = <ExtAuthorGroup.COMMUNITY_UNVERIFIED: 3>
    COMMUNITY_VERIFIED: typing.ClassVar[ExtAuthorGroup]  # value = <ExtAuthorGroup.COMMUNITY_VERIFIED: 2>
    NVIDIA: typing.ClassVar[ExtAuthorGroup]  # value = <ExtAuthorGroup.NVIDIA: 0>
    PARTNER: typing.ClassVar[ExtAuthorGroup]  # value = <ExtAuthorGroup.PARTNER: 1>
    USER: typing.ClassVar[ExtAuthorGroup]  # value = <ExtAuthorGroup.USER: 4>
class ExtOptions:
    """
    A class for managing extension options within the application.
    
        This class encapsulates various settings and preferences related to the handling and presentation of extensions in the application. It includes options for enabling or disabling the community tab, as well as managing publishing settings. The settings are stored persistently across sessions.
        
    """
    def __init__(self):
        """
        Initializes the ExtOptions with settings for community tab and publishing preferences.
        """
class ExtSource(enum.Enum):
    """
    An enumeration.
    """
    NVIDIA: typing.ClassVar[ExtSource]  # value = <ExtSource.NVIDIA: 0>
    THIRD_PARTY: typing.ClassVar[ExtSource]  # value = <ExtSource.THIRD_PARTY: 1>
class ExtensionCommonInfo:
    """
    A class to store and manage common information about an extension.
    
        This class encapsulates various details about an extension such as its ID, information,
        whether it is local or not, and other metadata. It also contains methods to resolve
        extension dependencies and evaluate whether an extension can be toggled.
    
        Args:
            ext_id (str): The unique identifier for the extension.
            ext_info (dict): A dictionary containing information about the extension.
            is_local (bool): A flag indicating whether the extension is local.
    """
    def __init__(self, ext_id, ext_info, is_local):
        """
        Initializes the common information for an extension.
        """
    def _build_image_resource_path(self, ext_info, key, default_path = None):
        ...
    def solve_extensions(self):
        """
        Solves the extension dependencies to determine non-toggleable dependencies and potential solver errors.
        """
class PageBase:
    """
    
        Interface for any classes adding Tabs to the Extension Manager UI
        
    """
    @staticmethod
    def get_tab_name() -> str:
        """
        Retrieves the name of the tab.
        
                Returns:
                    str: The name of the tab.
        """
    def build_tab(self, ext_info: dict, ext_item: ExtensionCommonInfo) -> None:
        """
        Builds the tab for the given extension information.
        
                Args:
                    ext_info (dict): The extension information.
                    ext_item (:obj:`ExtensionCommonInfo`): The common extension item.
        """
    def destroy(self) -> None:
        """
        Destroys the tab, releasing any resources or subscriptions.
        """
    def sort_index(self):
        ...
class SettingBoolValue:
    """
    A class for managing a boolean setting value.
    
        This class encapsulates a boolean setting, providing methods to get and set the value, while also handling the persistence of the setting.
    
        Args:
            path (str): The setting path in the settings registry.
            default (bool): The default boolean value to use if the setting is not already set.
    """
    def __bool__(self):
        ...
    def __init__(self, path: str, default: bool):
        """
        Initializes the SettingBoolValue with a specific settings path and default value.
        """
    def get(self) -> bool:
        """
        Returns the current boolean value of the setting.
        """
    def set_bool(self, value: bool):
        """
        Sets the boolean value of the setting and updates the application settings.
        
                Args:
                    value (bool): The new boolean value to set for the setting.
        """
def build_doc_urls(ext_item: ExtensionCommonInfo) -> typing.List[str]:
    """
    Produce possible candidates for doc urls
    
        Args:
            ext_item (:obj:`ExtensionCommonInfo`): The extension to generate documentation URLs for.
    
        Returns:
            List[str]: A list of possible documentation URLs.
    """
def build_ext_info(ext_id, package_id = None) -> typing.Tuple[omni.kit.window.extensions.common.ExtensionCommonInfo, dict]:
    """
    Builds extension information and creates an ExtensionCommonInfo instance.
    
        Args:
            ext_id (str): The unique identifier of the extension.
            package_id (Optional[str]): The package identifier, defaults to ext_id if not provided.
    
        Returns:
            Tuple[ExtensionCommonInfo, dict]: A tuple containing the ExtensionCommonInfo instance and the extension info dictionary.
    
        Raises:
            AssertionError: If the function is called before EXT_ROOT is set.
    """
def check_can_be_toggled(ext_id: str, for_autoload = False):
    """
    Determines if an extension can be toggled.
    
        Args:
            ext_id (str): Unique identifier of the extension.
            for_autoload (bool): If checking for auto-loading on startup.
    
        Returns:
            bool: True if the extension can be toggled, False otherwise.
    """
def get_categories(*args, **kwargs):
    ...
def get_core_exts() -> list:
    """
    Retrieves a list of core extensions from the settings.
    
        Returns:
            The list of core extension identifiers.
        
    """
def get_deprecated_exts() -> list:
    """
    Retrieves a list of deprecated extensions.
    
        Returns:
            list: A list containing the identifiers of deprecated extensions.
    """
def get_example_exts() -> list:
    """
    Retrieves a list of example extensions from the application settings.
    
        Returns:
            list: A list containing the names of example extensions stored in the application settings.
    """
def get_icons_path(*args, **kwargs):
    ...
def get_internal_exts() -> list:
    """
    Retrieves a list of internal extensions.
    
        Returns:
            list: A list of internal extensions that have been marked as such within the application settings.
    """
def get_kit_path(*args, **kwargs):
    ...
def get_omni_documents_path(*args, **kwargs):
    ...
def get_open_example_links(*args, **kwargs):
    ...
def get_options(*args, **kwargs):
    ...
def get_registries():
    """
    Retrieves a generator that yields registry information.
    
        Returns:
            Generator[Tuple[str, str, bool]]: A generator that produces tuples containing the registry name, the URL of the registry,
                and a boolean flag indicating whether the registry is a user registry.
    """
def get_registry_url(*args, **kwargs):
    ...
def get_version_locked_exts() -> list:
    """
    Retrieves a list of version locked extensions.
    
        Returns:
            list: A list containing the identifiers of version locked extensions.
    """
def is_community_tab_always_enabled(*args, **kwargs):
    ...
def is_community_tab_enabled() -> bool:
    """
    Checks if the community tab is enabled in the application.
    
        Returns:
            bool: True if the community tab is enabled, False otherwise.
    """
def is_community_tab_enabled_as_option() -> bool:
    """
    Checks if the community tab is enabled as an option in the application settings.
    
        Returns:
            bool: True if the community tab is enabled as an option, False otherwise.
    """
def is_in_omni_documents(path):
    """
    Checks if the given path is within the Omni Documents directory.
    
        Args:
            path (str): The file system path to check.
    """
def is_version_locked_exts(extension):
    ...
def path_is_parent(parent_path, child_path):
    """
    Checks if the parent_path is a parent of child_path.
    
        Args:
            parent_path (str): The potential parent directory path.
            child_path (str): The path of the potential child.
    """
def pull_extension_async(ext_item: ExtensionCommonInfo, on_pull_started_fn: typing.Callable = None):
    """
    Pulls an extension asynchronously.
    
        Args:
            ext_item (:obj:`ExtensionCommonInfo`): The extension to be pulled.
            on_pull_started_fn (Callable): Optional; function to call when pull starts.
    """
def pull_extension_async_by_name(ext_name: str):
    """
    Pulls the extension with the specified name asynchronously.
    
        Args:
            ext_name (str): The name of the extension to pull.
    """
def toggle_extension(ext_id: str, enable: bool, ui_render: bool = False):
    """
    Toggles the state of an extension.
    
        Args:
            ext_id (str): The unique identifier of the extension to toggle.
            enable (bool): Whether to enable (`True`) or disable (`False`) the extension.
            ui_render (bool): call is from ui_render callback, then async delay to prevent "Container::addChild attempting to add a child during a draw callback" warning/spam.
        
    """
COMMUNITY_TAB_TOGGLE_EVENT: int = 17022095773621968051
EXTENSION_PULL_STARTED_EVENT: int = 8509126198065146478
EXT_ROOT: str = '/home/chris/isaacsim/extscache/omni.kit.window.extensions-1.4.25+d02c707b'
REGISTRIES_CHANGED_EVENT: int = 17790543992418514273
REGISTRIES_SETTING: str = '/exts/omni.kit.registry.nucleus/registries'
REMOTE_IMAGE_SUPPORTED_EXTS: set = {'.png'}
USER_REGISTRIES_SETTING: str = '/persistent/exts/omni.kit.registry.nucleus/userRegistries'
core_exts_list = None
deprecated_exts_list = None
example_exts_list = None
internal_exts_list = None
version_locked_exts_list = None
