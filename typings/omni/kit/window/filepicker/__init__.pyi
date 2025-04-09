"""

This Kit extension provides both a popup dialog as well as an embeddable widget that
you can add to your code for browsing the filesystem. Incorporates
:obj:`BrowserBarWidget` and :obj:`FileBrowserWidget` into a general-purpose utility.
The filesystem can either be from your local machine or the Omniverse server.

Example:

    With just a few lines of code, you can create a ready-made dialog window. Then,
    customize it by setting any number of attributes.

        filepicker = FilePickerDialog(
            "my-filepicker",
            apply_button_label="Open",
            click_apply_handler=on_click_open,
            click_cancel_handler=on_click_cancel )

        filepicker.show()

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html

"""
from __future__ import annotations
import carb as carb
from omni.kit.window.filepicker.api import FilePickerAPI
from omni.kit.window.filepicker.collection_data import CollectionData
from omni.kit.window.filepicker.context_menu import BaseContextMenu
from omni.kit.window.filepicker.context_menu import BookmarkContextMenu
from omni.kit.window.filepicker.context_menu import CollectionContextMenu
from omni.kit.window.filepicker.context_menu import ConnectionContextMenu
from omni.kit.window.filepicker.context_menu import ContextMenu
from omni.kit.window.filepicker.context_menu import LocalContextMenu
from omni.kit.window.filepicker.context_menu import UdimContextMenu
from omni.kit.window.filepicker.detail_view import DetailFrameController
from omni.kit.window.filepicker.detail_view import DetailView
from omni.kit.window.filepicker.dialog import FilePickerDialog
from omni.kit.window.filepicker.extension import FilePickerExtension
from omni.kit.window.filepicker.file_ops import delete_items
from omni.kit.window.filepicker.file_ops import move_items
from omni.kit.window.filepicker.file_ops import rename_item
from omni.kit.window.filepicker.item_deletion_dialog import ConfirmItemDeletionDialog
from omni.kit.window.filepicker.model import FilePickerModel
from omni.kit.window.filepicker.timestamp import TimestampWidget
from omni.kit.window.filepicker.tool_bar import ToolBar
from omni.kit.window.filepicker.utils import get_user_folders_dict
from omni.kit.window.filepicker.view import FilePickerView
from omni.kit.window.filepicker.widget import FilePickerWidget
from . import about_dialog
from . import api
from . import bookmark_model
from . import collection_data
from . import config_button
from . import context_menu
from . import datetime
from . import detail_view
from . import dialog
from . import disk_partitions
from . import extension
from . import file_bar
from . import file_ops
from . import item_deletion_dialog
from . import item_deletion_model
from . import model
from . import option_box
from . import style
from . import timestamp
from . import tool_bar
from . import utils
from . import versioning_helper
from . import view
from . import widget
__all__: list = ['UI_READY_EVENT', 'SETTING_PERSISTENT_SHOW_GRID_VIEW', 'SETTING_PERSISTENT_GRID_VIEW_SCALE', 'CollectionData', 'FilePickerDialog', 'FilePickerWidget', 'FilePickerView', 'FilePickerModel', 'FilePickerAPI', 'BaseContextMenu', 'ContextMenu', 'CollectionContextMenu', 'ConnectionContextMenu', 'BookmarkContextMenu', 'UdimContextMenu', 'LocalContextMenu', 'DetailView', 'DetailFrameController', 'ToolBar', 'TimestampWidget', 'SearchDelegate', 'SearchResultsModel', 'SearchResultsItem', 'delete_items', 'move_items', 'rename_item', 'ConfirmItemDeletionDialog', 'get_user_folders_dict']
SETTING_PERSISTENT_GRID_VIEW_SCALE: str = '/persistent/exts/omni.kit.window.filepicker/grid_view_scale'
SETTING_PERSISTENT_ROOT: str = '/persistent/exts/omni.kit.window.filepicker/'
SETTING_PERSISTENT_SHOW_GRID_VIEW: str = '/persistent/exts/omni.kit.window.filepicker/show_grid_view'
SETTING_ROOT: str = '/exts/omni.kit.window.filepicker/'
UI_READY_EVENT: int = 284649323482245942
