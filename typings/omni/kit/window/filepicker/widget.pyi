from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb import log_warn
from functools import partial
import omni as omni
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserUdimItem
from omni.kit.window.filepicker.api import FilePickerAPI
from omni.kit.window.filepicker.context_menu import BookmarkContextMenu
from omni.kit.window.filepicker.context_menu import CollectionContextMenu
from omni.kit.window.filepicker.context_menu import ConnectionContextMenu
from omni.kit.window.filepicker.context_menu import ContextMenu
from omni.kit.window.filepicker.context_menu import LocalContextMenu
from omni.kit.window.filepicker.context_menu import UdimContextMenu
from omni.kit.window.filepicker.detail_view import DetailView
from omni.kit.window.filepicker.file_bar import FileBar
from omni.kit.window.filepicker.model import FilePickerModel
from omni.kit.window.filepicker.option_box import OptionBox
from omni.kit.window.filepicker.style import get_style
from omni.kit.window.filepicker.timestamp import TimestampWidget
from omni.kit.window.filepicker.tool_bar import ToolBar
from omni.kit.window.filepicker.utils import SingletonTask
from omni.kit.window.filepicker.utils import exec_after_redraw
from omni.kit.window.filepicker.utils import get_user_folders_dict
from omni.kit.window.filepicker.view import FilePickerView
from omni import ui
import os as os
import pathlib
__all__: list = ['FilePickerWidget']
class FilePickerWidget:
    """
    
        An embeddable UI widget for browsing the filesystem and taking action on a selected file.
        Includes a browser bar for keyboard input with auto-completion for navigation of the tree
        view.  For similar but different options, see also :obj:`FilePickerDialog` and :obj:`FilePickerView`.
    
        Args:
            title (str): Widget title. Default None.
    
        Keyword Args:
            layout (int): The overall layout of the window, one of: {LAYOUT_SPLIT_PANES, LAYOUT_SINGLE_PANE_SLIM,
                LAYOUT_SINGLE_PANE_WIDE, LAYOUT_DEFAULT}. Default LAYOUT_SPLIT_PANES.
            current_directory (str): View is set to display this directory. Default None.
            current_filename (str): Filename is set to this value. Default None.
            splitter_offset (int): Position of vertical splitter bar. Default 300.
            show_grid_view (bool): Displays grid view in the intial layout. Default True.
            grid_view_scale (int): Scales grid view, ranges from 0-5. Default 2.
            show_only_collections (List[str]): List of collections to display, any combination of ["bookmarks",
                "omniverse", "my-computer"]. If None, then all are displayed. Default None.
            allow_multi_selection (bool): Allows multiple selections. Default False.
            click_apply_handler (Callable): Function that will be called when the user accepts
                the selection. Function signature:
                void apply_handler(file_name: str, dir_name: str).
            click_cancel_handler (Callable): Function that will be called when the user clicks
                the cancel button. Function signature:
                void cancel_handler(file_name: str, dir_name: str).
            apply_button_label (str): Alternative label for the apply button. Default "Okay".
            cancel_button_label (str): Alternative label for the cancel button. Default "Cancel".
            enable_file_bar (bool): Enables/disables file bar.  Default True.
            enable_filename_input (bool): Enables/disables filename input. Default True.
            file_postfix_options (List[str]): A list of filename postfix options.  Default [].
            file_extension_options (List[Tuple[str, str]]): A list of filename extension options.  Each list
                element is an (extension name, description) pair, e.g. (".usdc", "Binary format").  Default [].
            item_filter_options (List[str]): OBSOLETE. Use file_postfix_options & file_extension_options instead.
                A list of filter options to determine which files should be listed.  For example: ['usd', 'wav']. Default None.
            item_filter_fn (Callable): This user function should return True if the given tree view
                item is visible, False otherwise. To base the decision on which filter option is
                currently chosen, use the attribute filepicker.current_filter_option.  Function
                signature: bool item_filter_fn(item: :obj:`FileBrowserItem`)
            error_handler (Callable): OBSOLETE. This function is called with error messages when appropriate.
                It provides the calling app a way to display errors on top of writing them to the
                console window. Function signature: void error_handler(message: str).
            show_detail_view (bool): Display the details pane.
            enable_versioning_pane (bool): OBSOLETE. Use enable_checkpoints instead.
            enable_checkpoints (bool): Whether the checkpoints, a.k.a. versioning pane should be displayed. Default False.
            enable_timestamp (bool): Whether the show timestamp panel. need show with checkpoint, Default False.
            options_pane_build_fn (Callable[[List[FileBrowserItem]], bool]): OBSOLETE, add options in a detail frame instead.
            options_pane_width (Union[int, omni.ui.Percent]): OBSOLETE.
            selection_changed_fn (Callable[[List[FileBrowserItem]]]): Selections has changed.
            treeview_identifier (str): widget identifier for treeview, only used by tests.
            enable_tool_bar (bool): Enables/disables tool bar.  Default True.
            enable_zoombar (bool): Enables/disables filename input. Default True.
            save_grid_view (bool): Save grid view mode if toggled. Default True.
            apply_path_handler (Callable): Function that will be called when the user entered
                in the path field. Function Signature:
                void apply_path_handler(url: str)
        
    """
    def __init__(self, title: str, **kwargs):
        ...
    def _apply_config_options(self):
        ...
    def _build_checkpoint_widget(self):
        ...
    def _build_context_menus(self):
        ...
    def _build_detail_view(self):
        ...
    def _build_file_bar(self):
        ...
    def _build_filepicker_view(self):
        ...
    def _build_tool_bar(self):
        ...
    def _build_ui(self):
        ...
    def _cancel_initial_navigation(self):
        ...
    def _get_mounted_servers(self) -> typing.Dict:
        """
        returns mounted server dict from settings
        """
    def _init_view(self, current_directory: str, current_filename: str):
        """
        Initialize the view, runs after the view is ready.
        """
    def _initial_navigation_async(self, current_directory: str, current_filename: str):
        ...
    def _item_filter_handler(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> bool:
        """
        
                Item filter handler, wrapper for the custom handler if specified. Returns True if the item is visible.
        
                Args:
                    item (:obj:`FileBrowseritem`): Item in question.
        
                Returns:
                    bool
        
                
        """
    def _on_begin_edit(self):
        ...
    def _on_detail_splitter_dragged(self, position_x: int):
        ...
    def _on_filename_changed(self, filename: str):
        ...
    def _on_mouse_double_clicked(self, pane: int, button: int, key_mod: int, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        ...
    def _on_mouse_pressed(self, pane: int, button: int, key_mod: int, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        ...
    def _on_scale_grid_view(self, scale_level):
        ...
    def _on_search(self, search_model):
        ...
    def _on_selection_changed(self, pane: int, selected: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem] = list()):
        ...
    def _on_toggle_grid_view(self, show_grid_view):
        ...
    def _on_ui_ready(self, event):
        ...
    def _on_window_width_changed(self, new_width: int):
        ...
    def _refresh_ui(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem = None):
        ...
    def destroy(self):
        """
        Destructor.
        """
    def get_selected_filename_and_directory(self) -> typing.Tuple[str, str]:
        """
         Get the current directory and filename that has been selected or entered into the filename field
        """
    def set_click_apply_handler(self, click_apply_handler: typing.Callable[[str, str], NoneType]):
        """
        
                Sets the function to execute upon clicking apply.
        
                Args:
                    click_apply_handler (Callable): Callback with filename being the name of the file, and dirname being the containing directory path with an ending slash.
                        Signature is fn(filename: str, dirname: str) -> None
        
                
        """
    def set_item_filter_fn(self, item_filter_fn: typing.Callable[[str], bool]):
        """
        
                Sets the item filter function.
        
                Args:
                    item_filter_fn (Callable): Signature is bool fn(item: FileBrowserItem)
        
                
        """
    @property
    def api(self) -> omni.kit.window.filepicker.api.FilePickerAPI:
        """
        :obj:`FilePickerAPI`: Provides API methods to this widget.
        """
    @property
    def current_filter_option(self) -> int:
        """
        OBSOLETE int: Index of current filter option, range 0 .. num_filter_options.
        """
    @property
    def file_bar(self) -> omni.kit.window.filepicker.file_bar.FileBar:
        """
        :obj:`FileBar`: Returns the file bar widget.
        """
    @property
    def model(self):
        """
         Returns the model of this widget.
        """
DETAIL_WIDTH_INIT: str = '/exts/omni.kit.window.filepicker/detail_width_init'
DETAIL_WIDTH_MAX: str = '/exts/omni.kit.window.filepicker/detail_width_max'
DETAIL_WIDTH_MIN: str = '/exts/omni.kit.window.filepicker/detail_width_min'
ICON_COMMON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.filepicker-2.11.7+d02c707b/icons/common')
LAYOUT_SPLIT_PANES: int = 3
LISTVIEW_PANE: int = 2
SETTING_ROOT: str = '/exts/omni.kit.window.filepicker/'
SHOW_ONLY_COLLECTIONS: str = '/exts/omni.kit.window.filepicker/show_only_collections'
TREEVIEW_PANE: int = 1
UI_READY_EVENT: int = 284649323482245942
have_versioning: bool = False
