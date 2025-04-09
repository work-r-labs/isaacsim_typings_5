"""
A window extension for browsing filesystem, including Nucleus, content
"""
from __future__ import annotations
from omni.kit.window.content_browser.extension import ContentBrowser
from omni.kit.window.content_browser.extension import get_content_instance
from omni.kit.window.content_browser.extension import get_instance
from omni.kit.window.content_browser.widget import ContentBrowserWidget
from omni.kit.window.content_browser.window import ContentBrowserWindow
from . import api
from . import context_menu
from . import extension
from . import external_drag_drop_helper
from . import file_ops
from . import hotkey
from . import prompt
from . import style
from . import tool_bar
from . import widget
from . import window
__all__: list = ['ContentBrowserExtension', 'get_content_window', 'ContentBrowser']
def get_content_window() -> extension.ContentBrowser:
    """
    Returns the singleton instance of the content browser.
    
        Returns:
            ContentBrowser: The instance of the content browser  that allows browsing
            of the filesystem, including Nucleus content.
    """
FILE_TYPE_IMAGE: int = 2
FILE_TYPE_SOUND: int = 3
FILE_TYPE_TEXT: int = 4
FILE_TYPE_USD: int = 1
FILE_TYPE_VOLUME: int = 5
SETTING_PERSISTENT_CURRENT_DIRECTORY: str = '/persistent/exts/omni.kit.window.content_browser/current_directory'
SETTING_PERSISTENT_ROOT: str = '/persistent/exts/omni.kit.window.content_browser/'
SETTING_ROOT: str = '/exts/omni.kit.window.content_browser/'
