"""
This module provides a widget for displaying detailed information about extensions in the Extension Manager UI, including overview, changelog, dependencies, and available packages.
"""
from __future__ import annotations
import asyncio as asyncio
import contextlib as contextlib
from datetime import datetime
from datetime import timezone
import omni as omni
from omni.kit.window.extensions.common import ExtensionCommonInfo
from omni.kit.window.extensions.common import PageBase
from omni.kit.window.extensions.common import build_ext_info
from omni.kit.window.extensions.common import check_can_be_toggled
from omni.kit.window.extensions.common import get_categories
from omni.kit.window.extensions.common import get_icons_path
from omni.kit.window.extensions.common import get_options
from omni.kit.window.extensions.common import pull_extension_async
from omni.kit.window.extensions.common import toggle_extension
from omni.kit.window.extensions.ext_components import ExtensionToggle
from omni.kit.window.extensions.ext_components import SimpleCheckBox
from omni.kit.window.extensions.ext_components import add_doc_link_button
from omni.kit.window.extensions import ext_controller
from omni.kit.window.extensions.ext_data_fetcher import get_ext_data_fetcher
from omni.kit.window.extensions.ext_export_import import export_ext
from omni.kit.window.extensions.exts_dependency_window import ExtsDependencyWidget
from omni.kit.window.extensions.exts_list_widget import ExtensionCardWidget
from omni.kit.window.extensions.markdown_renderer import MarkdownText
from omni.kit.window.extensions.utils import clip_text
from omni.kit.window.extensions.utils import is_vscode_installed
from omni.kit.window.extensions.utils import open_in_vscode_if_enabled
from omni.kit.window.extensions.utils import version_to_str
from omni import ui
import os as os
import typing
import weakref as weakref
__all__: list = ['PageBase', 'OverviewPage', 'ChangelogPage', 'DependenciesPage', 'PackagesPage', 'ExtInfoWidget']
class ChangelogPage(omni.kit.window.extensions.common.PageBase):
    """
    A tab page within the Extension Manager UI that displays the changelog of an extension.
    
        The ChangelogPage allows users to view the list of changes, updates, bug fixes, and other modifications made to an extension over time. It presents this information in a formatted text area, often leveraging markdown for better readability.
    
        The changelog content is dynamically retrieved based on the extension's information, either from a local dictionary or from the registry's extra data. If no changelog is present, a default message indicating the absence of a changelog is shown to the user.
    
        This class inherits from the PageBase interface, adhering to its contract for building and destroying tab content within the Extension Manager UI.
        
    """
    @staticmethod
    def get_tab_name():
        """
        Retrieves the name to be used for the changelog tab in the UI.
        
                Returns:
                    str: The name of the tab.
        """
    def build_tab(self, ext_info, ext_item: omni.kit.window.extensions.common.ExtensionCommonInfo):
        """
        Builds the changelog tab with extension information.
        
                Args:
                    ext_info (dict): The extension info dictionary containing extension details.
                    ext_item (:obj:`ExtensionCommonInfo`): The common info object for the extension.
        """
    def destroy(self):
        """
        Destroys the changelog tab and performs any necessary cleanup.
        """
    def sort_index(self):
        ...
class DependenciesPage(omni.kit.window.extensions.common.PageBase):
    """
    A tab page within the Extension Manager UI that displays dependencies information for an extension.
    
        This page shows the dependencies required by the selected extension, including their versions and whether they are optional. It lists the extensions that would be enabled as a result of enabling the selected extension, along with any errors that would prevent enabling.
        
    """
    @staticmethod
    def get_tab_name():
        """
        Returns the name of the tab.
        """
    def __init__(self):
        """
        Initialize the DependenciesPage.
        """
    def build_tab(self, ext_info, ext_item: omni.kit.window.extensions.common.ExtensionCommonInfo):
        """
        Builds the dependencies tab for the given extension.
        
                Args:
                    ext_info (dict): Information about the extension.
                    ext_item (:obj:`ExtensionCommonInfo`): The extension item to build dependencies for.
        """
    def destroy(self):
        """
        Cleans up any resources or subscriptions.
        """
    def sort_index(self):
        ...
class DeveloperPage(omni.kit.window.extensions.common.PageBase):
    """
    
        Build a class with same interface and add it to ExtInfoWidget.pages
        below to have it show up as a tab
        
    """
    @staticmethod
    def get_tab_name():
        """
        Retrieves the name to be used for the changelog tab in the UI.
        
                Returns:
                    str: The name of the tab.
        """
    def __init__(self):
        ...
    def build_tab(self, ext_info, ext_item: omni.kit.window.extensions.common.ExtensionCommonInfo):
        """
        Builds the content for the developer tab.
        
                Args:
                    ext_info (dict): The dictionary containing extension information.
                    ext_item (:obj:`ExtensionCommonInfo`): The common info about the extension.
        """
    def destroy(self):
        """
        Cleans up resources and UI elements associated with the overview tab.
        """
    def sort_index(self):
        ...
class ExtInfoWidget:
    """
    A widget for displaying detailed information about extensions in the Extension Manager UI.
    
        This widget provides a comprehensive view of an extension's overview, changelog, dependencies, and available packages. It allows users to select different versions of the extension, install or update it, and view additional metadata and documentation. The widget also offers functionality to copy extension IDs, open extension folders, and export extensions.
    
        The widget is designed to be dynamically updated based on the selected extension and provides tabs for navigating between different sections of extension information. It is also responsible for handling extension-related actions such as installation, updating, enabling autoload, and other management tasks.
        
    """
    current_page: typing.ClassVar[int] = 0
    pages: typing.ClassVar[list] = [OverviewPage, ChangelogPage, DependenciesPage, PackagesPage, DeveloperPage]
    def __init__(self):
        """
        Initializes the ExtInfoWidget instance with default values and subscriptions.
        """
    def _refresh(self):
        ...
    def _refresh_once_next_frame(self):
        ...
    def _show_dependencies(self, ext_id):
        ...
    def destroy(self):
        """
        Cleans up resources and subscriptions.
        """
    def select_ext(self, ext_summary):
        """
        Select extension to display info about. Can be None
        
                Args:
                    ext_summary (:obj:`ExtensionCommonInfo`): The summary of the extension to display.
        """
    def set_show_dependencies_fn(self, fn: typing.Callable):
        """
        Assigns a function to be called to show the extension dependencies.
        
                Args:
                    fn (:obj:`Callable`): The function to call.
        """
    def set_visible(self, visible):
        """
        Sets the visibility of the ExtInfoWidget.
        
                Args:
                    visible (bool): Whether the widget should be visible.
        """
    def update_tabs(self):
        """
        Updates the tabs in the ExtInfoWidget based on the current pages.
        """
class OverviewPage(omni.kit.window.extensions.common.PageBase):
    """
    
        Build a class with same interface and add it to ExtInfoWidget.pages
        below to have it show up as a tab
        
    """
    @staticmethod
    def get_tab_name():
        """
        Get the name used for the tab name in the UI
        
                Returns:
                    str: The name of the tab.
        """
    def __init__(self):
        ...
    def build_tab(self, ext_info, ext_item: omni.kit.window.extensions.common.ExtensionCommonInfo):
        """
        Builds the content for the overview tab.
        
                Args:
                    ext_info (dict): The dictionary containing extension information.
                    ext_item (:obj:`ExtensionCommonInfo`): The common info about the extension.
        """
    def destroy(self):
        """
        Cleans up resources and UI elements associated with the overview tab.
        """
    def sort_index(self):
        ...
class PackagesPage(omni.kit.window.extensions.common.PageBase):
    """
    A UI component representing a tabbed page in the Extension Manager that displays a list of all available packages for a specific version of an extension.
    
        This class is responsible for querying the extension manager for available packages related to a particular extension version and presenting them in a structured format within the Extension Manager UI. It allows users to view detailed information about each package, including its dependencies and other metadata.
    
        The build_tab method is used to construct the user interface elements and populate them with the retrieved package data. The destroy method ensures proper cleanup of resources when the PackagesPage is no longer needed.
        
    """
    @staticmethod
    def get_tab_name():
        """
        Retrieves the name of the tab.
        
                Returns:
                    str: The name of the tab.
        """
    def build_tab(self, ext_info, ext_item: omni.kit.window.extensions.common.ExtensionCommonInfo):
        """
        Builds the tab content for the given extension.
        
                Args:
                    ext_info (dict): The dictionary containing extension metadata.
                    ext_item (:obj:`ExtensionCommonInfo`): The common info object for the extension.
        """
    def destroy(self):
        """
        Destroys the tab and cleans up resources.
        """
    def sort_index(self):
        ...
def build_package_info(ext_info, ext_item):
    """
    Generates a dictionary with detailed package information.
    
        Args:
            ext_info (dict): Extension information to extract package info from.
            ext_item (:obj:`ExtensionCommonInfo`): The common extension item.
    """
def get_ext_text_content(key: str, ext_info, ext_item: omni.kit.window.extensions.common.ExtensionCommonInfo):
    """
    Get extension readme/changelog from either local dict or registry extra data
    
        Args:
            key (str): The key to access the content ('readme' or 'changelog').
            ext_info: The dictionary containing extension info.
            ext_item (:obj:`ExtensionCommonInfo`): The common extension item information.
    
        Returns:
            The extension's readme or changelog content as a string.
    """
CATEGORY_ICON_SIZE: tuple = (70, 70)
CATEGORY_ZONE_WIDTH: int = 120
EXT_ICON_SIZE_LARGE: tuple = (100, 100)
ICON_ZONE_WIDTH: int = 120
