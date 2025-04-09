from __future__ import annotations
import carb as carb
import omni.kit.widget.filebrowser.model
from omni.kit.widget.filebrowser.model import FileBrowserModel
import omni.kit.window.filepicker.detail_view
from omni.kit.window.filepicker.detail_view import DetailFrameController
from omni.kit.window.filepicker.utils import exec_after_redraw
from omni.kit.window.filepicker.widget import FilePickerWidget
from omni import ui
__all__: list = ['FilePickerDialog']
class FilePickerDialog:
    """
    
        A popup window for browsing the filesystem and taking action on a selected file.
        Includes a browser bar for keyboard input with auto-completion for navigation of the tree
        view.  For similar but different options, see also :obj:`FilePickerWidget` and :obj:`FilePickerView`.
    
        Args:
            title (str): Window title. Default None.
    
        Keyword Args:
            width (int): Window width. Default 1000.
            height (int): Window height. Default 600.
            click_apply_handler (Callable): Function that will be called when the user accepts
                the selection. Function signature:
                apply_handler(file_name: str, dir_name: str) -> None.
            click_cancel_handler (Callable): Function that will be called when the user clicks
                the cancel button. Function signature:
                cancel_handler(file_name: str, dir_name: str) -> None.
            other: Additional args listed for :obj:`FilePickerWidget`
    
        
    """
    def __init__(self, title: str, **kwargs):
        ...
    def _build_ui(self, title: str, **kwargs):
        ...
    def _on_key_pressed(self, key, mod, pressed):
        ...
    def add_connections(self, connections: dict):
        """
        
                Adds specified server connections to the browser.
        
                Args:
                    connections (dict): A dictionary of name, path pairs. For example:
                        {"C:": "C:", "ov-content": "omniverse://ov-content"}.  Paths to Omniverse servers
                        should be prefixed with "omniverse://".
        
                
        """
    def add_detail_frame_from_controller(self, name: str, controller: omni.kit.window.filepicker.detail_view.DetailFrameController):
        """
        
                Adds subsection to the detail view, and populate it with a custom built widget.
        
                Args:
                    name (str): Name of the widget sub-section, this name must be unique over all detail sub-sections.
                    controller (:obj:`DetailFrameController`): Controller object that encapsulates all aspects of creating,
                        updating, and deleting a detail frame widget.
        
                Returns:
                    ui.Widget: Handle to created widget.
        
                
        """
    def delete_detail_frame(self, name: str):
        """
        
                Deletes the named detail frame.
        
                Args:
                    name (str): Name of the frame.
        
                
        """
    def destroy(self):
        """
        Destructor.
        """
    def get_current_directory(self) -> str:
        """
        
                Returns the current directory from the browser bar.
        
                Returns:
                    str: The system path, which may be different from the displayed path.
        
                
        """
    def get_current_selections(self, pane: int = 2) -> typing.List[str]:
        """
        
                Returns current selected as list of system path names.
        
                Args:
                    pane (int): Specifies pane to retrieve selections from, one of {TREEVIEW_PANE = 1, LISTVIEW_PANE = 2,
                        BOTH = None}.  Default LISTVIEW_PANE.
                Returns:
                    [str]: List of system paths (which may be different from displayed paths, e.g. bookmarks)
        
                
        """
    def get_file_extension(self) -> str:
        """
        
                Returns:
                    str: Currently selected filename extension.
                
        """
    def get_file_extension_options(self) -> typing.List[typing.Tuple[str, str]]:
        """
        
                Returns:
                    List[str]: List of all extension options strings.
                
        """
    def get_file_postfix(self) -> str:
        """
        
                Returns:
                    str: Currently selected postfix.
                
        """
    def get_file_postfix_options(self) -> typing.List[str]:
        """
        
                Returns:
                    List[str]: List of all postfix strings.
                
        """
    def get_filebar_label_name(self) -> str:
        """
        
                Returns:
                    str: Currently text of name label for file bar.
                
        """
    def get_filename(self) -> str:
        """
        
                Returns:
                    str: Currently selected filename.
                
        """
    def hide(self):
        """
        
                Hides this dialog. Automatically called when "Cancel" buttons is clicked.
        
                
        """
    def navigate_to(self, path: str):
        """
        
                Navigates to a path, i.e. the path's parent directory will be expanded and leaf selected.
        
                Args:
                    path (str): The path to navigate to.
        
                
        """
    def refresh_current_directory(self):
        """
        Refreshes the current directory set in the browser bar.
        """
    def set_click_apply_handler(self, click_apply_handler: typing.Callable[[str, str], NoneType]):
        """
        
                Sets the function to execute upon clicking apply.
        
                Args:
                    click_apply_handler (Callable): Callback with filename being the name of the file, and dirname being the containing directory path with an ending slash.
                        Function Signature is fn(filename: str, dirname: str) -> None
        
                
        """
    def set_current_directory(self, path: str):
        """
        
                Procedurally sets the current directory path.
        
                Args:
                    path (str): The full path name of the folder, e.g. "omniverse://ov-content/Users/me.
        
                Raises:
                    :obj:`RuntimeWarning`: If path doesn't exist or is unreachable.
        
                
        """
    def set_file_extension(self, extension: str):
        """
        Sets the file extension in the file bar.
        """
    def set_file_postfix(self, postfix: str):
        """
        Sets the file postfix in the file bar.
        """
    def set_filebar_label_name(self, name: str):
        """
        
                Sets the text of the name label for filebar, at the bottom of dialog.
        
                Args:
                    name (str): By default, it's "File name" if it's not set. For some senarios that,
                    it only allows to choose folder, it can be configured with this API for better UX.
                
        """
    def set_filename(self, filename: str):
        """
        
                Sets the filename in the file bar, at bottom of the dialog.
        
                Args:
                    filename (str): The filename only (and not the fullpath), e.g. "myfile.usd".
        
                
        """
    def set_item_filter_fn(self, item_filter_fn: typing.Callable[[str], bool]):
        """
        
                Sets the item filter function.
        
                Args:
                    item_filter_fn (Callable): Signature is bool fn(item: FileBrowserItem)
        
                
        """
    def set_search_delegate(self, delegate):
        """
        
                Sets a custom search delegate for the tool bar.
        
                Args:
                    delegate (:obj:`SearchDelegate`): Object that creates the search widget.
        
                
        """
    def set_visibility_changed_listener(self, listener: typing.Callable[[bool], NoneType]):
        """
        
                Call the given handler when window visibility is changed.
        
                Args:
                    listener (Callable): Handler with signature listener[visible: bool).
        
                
        """
    def show(self, path: str = None):
        """
        
                Shows this dialog.  Currently pops up atop all other windows but is not completely
                modal, i.e. does not take over input focus.
        
                Args:
                    path (str): If optional path is specified, then navigates to it upon startup.
        
                
        """
    def show_model(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel):
        """
        
                Displays the given model in the list view, overriding the default model.  For example, this model
                might be the result of a search.
        
                Args:
                    model (:obj:`FileBrowserModel`): Model to display.
        
                
        """
    def toggle_bookmark_from_path(self, name: str, path: str, is_bookmark: bool, is_folder: bool = True):
        """
        
                Adds/deletes the given bookmark with the specified path. If deleting, then the path argument
                is optional.
        
                Args:
                    name (str): Name to call the bookmark or existing name if delete.
                    path (str): Path to the bookmark.
                    is_bookmark (bool): True to add, False to delete.
                    is_folder (bool): Whether the item to be bookmarked is a folder.
        
                
        """
    @property
    def current_filter_option(self):
        """
        int: Index of current filter option, range 0 .. num_filter_options.
        """
