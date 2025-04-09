"""

The basic UI widget and set of supporting classes for navigating the filesystem through a tree or grid view.
The filesystem can either be from your local machine or the Omniverse server.

Example:

.. code-block:: python

    With just a few lines of code, you can create a powerful, flexible tree view widget that you
    can embed into your view.

        filebrowser = FileBrowserWidget(
            "Omniverse",
            layout=SPLIT_PANES,
            mouse_pressed_fn=on_mouse_pressed,
            selection_changed_fn=on_selection_changed,
            drop_fn=drop_handler,
            filter_fn=item_filter_fn,
        )

Module Constants:

    layout: {LAYOUT_SINGLE_PANE_SLIM, LAYOUT_SINGLE_PANE_WIDE, LAYOUT_SPLIT_PANES, LAYOUT_DEFAULT}

"""
from __future__ import annotations
import carb as carb
from omni.kit.widget.filebrowser.abstract_column_delegate import AbstractColumnDelegate
from omni.kit.widget.filebrowser.abstract_column_delegate import ColumnItem
from omni.kit.widget.filebrowser.card import FileBrowserItemCard
from omni.kit.widget.filebrowser.clipboard import clear_clipboard
from omni.kit.widget.filebrowser.clipboard import get_clipboard_items
from omni.kit.widget.filebrowser.clipboard import is_clipboard_cut
from omni.kit.widget.filebrowser.clipboard import is_path_cut
from omni.kit.widget.filebrowser.clipboard import save_items_to_clipboard
from omni.kit.widget.filebrowser.filesystem_model import FileSystemItem
from omni.kit.widget.filebrowser.filesystem_model import FileSystemModel
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFactory
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni.kit.widget.filebrowser.model import FileBrowserModel
from omni.kit.widget.filebrowser.model import FileBrowserUdimItem
from omni.kit.widget.filebrowser.nucleus_model import NucleusConnectionItem
from omni.kit.widget.filebrowser.nucleus_model import NucleusItem
from omni.kit.widget.filebrowser.nucleus_model import NucleusModel
from omni.kit.widget.filebrowser.thumbnails import find_thumbnails_for_files_async
from omni.kit.widget.filebrowser.thumbnails import list_thumbnails_for_folder_async
from omni.kit.widget.filebrowser.widget import FileBrowserWidget
from . import abstract_column_delegate
from . import card
from . import clipboard
from . import column_delegate_registry
from . import date_format_menu
from . import filesystem_model
from . import grid_view
from . import model
from . import nucleus_model
from . import singleton
from . import style
from . import thumbnails
from . import tree_view
from . import view
from . import widget
from . import zoom_bar
__all__: list = ['FileBrowserWidget', 'FileBrowserItemCard', 'FileBrowserModel', 'FileBrowserItem', 'FileBrowserUdimItem', 'FileBrowserItemFactory', 'FileBrowserItemFields', 'FileSystemModel', 'FileSystemItem', 'NucleusModel', 'NucleusItem', 'NucleusConnectionItem', 'ColumnDelegateRegistry', 'ColumnItem', 'AbstractColumnDelegate', 'find_thumbnails_for_files_async', 'list_thumbnails_for_folder_async', 'save_items_to_clipboard', 'get_clipboard_items', 'is_clipboard_cut', 'is_path_cut', 'clear_clipboard', 'CONNECTION_ERROR_EVENT', 'MISSING_IMAGE_THUMBNAILS_EVENT', 'THUMBNAILS_GENERATED_EVENT', 'ALERT_INFO', 'ALERT_WARNING', 'ALERT_ERROR', 'LAYOUT_SINGLE_PANE_SLIM', 'LAYOUT_SINGLE_PANE_WIDE', 'LAYOUT_SPLIT_PANES', 'LAYOUT_SINGLE_PANE_LIST', 'LAYOUT_DEFAULT', 'TREEVIEW_PANE', 'LISTVIEW_PANE']
ALERT_ERROR: int = 3
ALERT_INFO: int = 1
ALERT_WARNING: int = 2
CONNECTION_ERROR_EVENT: int = 1730322306128580327
LAYOUT_DEFAULT: int = 3
LAYOUT_SINGLE_PANE_LIST: int = 4
LAYOUT_SINGLE_PANE_SLIM: int = 1
LAYOUT_SINGLE_PANE_WIDE: int = 2
LAYOUT_SPLIT_PANES: int = 3
LISTVIEW_PANE: int = 2
MISSING_IMAGE_THUMBNAILS_EVENT: int = 1346573191877322751
THUMBNAILS_GENERATED_EVENT: int = 4677668926123661862
TREEVIEW_PANE: int = 1
