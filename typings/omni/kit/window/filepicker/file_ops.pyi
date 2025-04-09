from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb import log_warn
from datetime import datetime
from functools import partial
import omni as omni
from omni.kit.notification_manager.notification_info import NotificationStatus
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni.kit.widget.filebrowser.nucleus_model import NucleusConnectionItem
from omni.kit.window.filepicker.about_dialog import AboutDialog
from omni.kit.window.filepicker.bookmark_model import BookmarkItem
from omni.kit.window.filepicker.item_deletion_dialog import ConfirmItemDeletionDialog
from omni.kit.window.filepicker.versioning_helper import VersioningHelper
from omni.kit.window.filepicker.view import FilePickerView
from omni.kit.window.popup_dialog.form_dialog import FormDialog
from omni.kit.window.popup_dialog.input_dialog import InputDialog
from omni.kit.window.popup_dialog.message_dialog import MessageDialog
from omni import ui
import os as os
import subprocess as subprocess
import sys as sys
__all__ = ['AboutDialog', 'BookmarkItem', 'ConfirmItemDeletionDialog', 'FileBrowserItem', 'FileBrowserItemFields', 'FilePickerView', 'FormDialog', 'InputDialog', 'MessageDialog', 'NotificationStatus', 'NucleusConnectionItem', 'VersioningHelper', 'about_connection', 'add_bookmark', 'add_connection', 'asyncio', 'carb', 'checkpoint_items', 'copy_to_clipboard', 'create_folder', 'create_usd_file', 'datetime', 'delete_bookmark', 'delete_items', 'edit_bookmark', 'exec_tasks_async', 'is_item_checkpointable', 'is_usd_supported', 'log_out_from_connection', 'log_warn', 'move_item_async', 'move_items', 'move_items_async', 'obliterate_item_async', 'obliterate_items', 'omni', 'open_in_file_browser', 'os', 'partial', 'refresh_connection', 'refresh_item', 'remove_connection', 'rename_file', 'rename_file_async', 'rename_item', 'restore_item_async', 'restore_items', 'subprocess', 'sys', 'ui']
def _check_paths_exist_async(paths: typing.List[str]) -> typing.List[str]:
    """
    Check if paths already exist.
    """
def _display_notification_message(message: str, status: omni.kit.notification_manager.notification_info.NotificationStatus = 1) -> None:
    """
    
        Display the given notification message to the User, using the given status.
    
        Args:
            message (str): Message to display in the notification.
            status (NotificationStatus): Status of the notification (default: `NotificationStatus.INFO`).
    
        Returns:
            None
    
        
    """
def _prompt_confirm_items_deletion_dialog(dst_paths, apply_callback):
    """
    
        Checks dst_paths existence and prompt user to confirm deletion.
    
        Args:
            dst_paths (List[str]): The file paths to delete.
            apply_callback (Callable): Function to execute upon clicking the "Yes" button. Function signature:
                        void apply_callback(dialog: :obj:`PopupDialog`)
        
    """
def _validate_usd_file_creation(usd_filename: str, absolute_usd_file_path: str) -> bool:
    """
    
        Check if the given absolute file path for a USD file can be created, based on:
            * Whether or not the given file name is empty.
            * Whether or not the given file path already exists.
    
        Args:
            usd_filename (str): The name of the USD file to create, as provided by the User (without extension).
            absolute_usd_file_path (str): The absolute file path of a USD file to create.
    
        Returns:
            bool: `True` if the given absolute file path for a USD file can be created, `False` otherwise.
    
        
    """
def about_connection(item: omni.kit.widget.filebrowser.model.FileBrowserItem):
    """
    
        Show a connection's about info dialog for the connected file browser item.
    
        Args:
            item (:obj:`FileBrowserItem`): The FileBrowserItem own the connection.
        
    """
def add_bookmark(item: omni.kit.widget.filebrowser.model.FileBrowserItem, view: omni.kit.window.filepicker.view.FilePickerView):
    """
    
        Add a bookmark to the file browser item with a dialog.
    
        Args:
            item(:obj:'FileBrowserItem'): The item that was selected.
            view(:obj:'FilePickerView'): The view to add the bookmark to.
        
    """
def add_connection(view: omni.kit.window.filepicker.view.FilePickerView):
    """
    
        Show the connect dialog for the given view
    
        Args:
            view (:obj:`FilePickerView`): The FilePickerView to add the connection.
        
    """
def checkpoint_items(items: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem], checkpoint_widget):
    """
    
        Create checkpoint for a list of items.
    
        Args:
            items(List[:obj:'FileBrowserItem']): List of items to checkpoint.
            checkpoint_widget(:obj:'CheckpointWidget'): Checkpoint widget that is used to list checkpoints.
        
    """
def copy_to_clipboard(item: omni.kit.widget.filebrowser.model.FileBrowserItem):
    """
    
        Copy a item's path to the clipboard.
    
        Args:
            item(:obj:'FileBrowserItem'): The item to copy
        
    """
def create_folder(item: omni.kit.widget.filebrowser.model.FileBrowserItem):
    """
    
        Creates folder under given item.
    
        Args:
            item (:obj:`FileBrowserItem`): Item under which to create the folder.
    
        
    """
def create_usd_file(item: omni.kit.widget.filebrowser.model.FileBrowserItem):
    """
    
        Action executed upon clicking the "New USD File" contextual menu item.
    
        Args:
            item (FileBrowserItem): Directory item of the File Browser where to create the new USD file.
    
        Returns:
            None
    
        
    """
def delete_bookmark(item: omni.kit.window.filepicker.bookmark_model.BookmarkItem, view: omni.kit.window.filepicker.view.FilePickerView):
    """
    
        Delete a bookmark item with a dialog.
    
        Args:
            item(:obj:'BookmarkItem'): The bookmark item that to be delete.
            view(:obj:'FilePickerView'): The view which own the bookmark.
        
    """
def delete_items(items: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem], view: typing.Optional[omni.kit.window.filepicker.view.FilePickerView] = None):
    """
    
        Deletes given items. Upon success, executes the given callback.
    
        Args:
            items ([:obj:`FileBrowserItem`]): Items to delete.
            view (Optional[:obj:`FilePickerView`]): The FilePickerView own the item.
    
        Raises:
            :obj:`Exception`
        
    """
def edit_bookmark(item: omni.kit.window.filepicker.bookmark_model.BookmarkItem, view: omni.kit.window.filepicker.view.FilePickerView):
    """
    
        Edit a bookmark item with a dialog.
    
        Args:
            item(:obj:'BookmarkItem'): The bookmark item that to be edit.
            view(:obj:'FilePickerView'): The view which own the bookmark.
        
    """
def exec_tasks_async(tasks, callback: typing.Callable = None):
    """
    
        Helper function to execute a given list of tasks concurrently.  When done, invokes the callback with the
        list of results. Results can include an exceptions if appropriate.
    
        Args:
            tasks ([]:obj:`Task`]): List of tasks to execute.
            callback (Callable): Invokes this callback when all tasks are finished. Function signature is
                void callback(results: List[Union[str, Exception]])
    
        
    """
def is_item_checkpointable(context: typing.Dict[str, typing.Any], menu_item: omni.ui._ui.MenuItem):
    """
    
        Checks if an item is checkpointable. Show the correspond menu item when it's true.
    
        Args:
            context(Dict[str, Any]): The context of the menu.
            menu_item(:obj:'ui.MenuItem'): The menu item to be shown on
        
    """
def is_usd_supported() -> bool:
    """
    
        Check if USD is supported.
    
        Returns:
            bool: True if support usd or False.
        
    """
def log_out_from_connection(item: omni.kit.widget.filebrowser.nucleus_model.NucleusConnectionItem, view: omni.kit.window.filepicker.view.FilePickerView):
    """
    
        Log out from the Nucleus server from the given connection item
    
        Args:
            item (:obj:`NucleusConnectionItem`): The NucleusConnectionItem to log out the connection from.
            view (:obj:`FilePickerView`): The FilePickerView own the item.
        
    """
def move_item_async(src_path: str, dst_path: str, timeout: float = 300.0, is_rename: bool = False) -> str:
    """
    
        Async function that moves item (recursively) from one path to another.
        Note: this function simply uses the move function from omni.client and makes no attempt to optimize for
        moving from one Omniverse server to another.
        Example usage:
        await move_item_async("C:/tmp/my_file.usd", "omniverse://ov-content/Users/me/moved.usd")
    
        Args:
            src_root (str): Source path to item being copied.
            dst_root (str): Destination path to move the item.
            timeout (float): Number of seconds to try before erroring out.  Default 10.
    
        Returns:
            str: Destination path name
    
        Raises:
            :obj:`RuntimeWarning`: If error or timeout.
    
        
    """
def move_items(dst_item: omni.kit.widget.filebrowser.model.FileBrowserItem, src_paths: typing.List[str], dst_name: typing.Optional[str] = None, callback: typing.Callable = None):
    """
    
        Moves items. Upon success, executes the given callback.
    
        Args:
            dst_item (:obj: 'FileBrowserItem'): Destination item.
            src_paths (List[str]): Paths of items to move.
            dst_name (Optional[str]): Destination item's name.
            callback (Callable): the callback function when move success.Function signature is void callback().
        
    """
def move_items_async(src_paths: typing.List[str], dst_path: str, callback: typing.Callable = None):
    """
    
        Moves items. Upon success, executes the given callback.
    
        Args:
            src_paths ([str]): Paths of items to move.
            dst_path (str): Destination folder.
            callback (func): Callback to execute upon success.  Function signature is void callback([str]).
    
        Raises:
            :obj:`Exception`
        
    """
def obliterate_item_async(path: str, timeout: float = 10.0) -> str:
    """
    
        Async function.  obliterates the item at the given path name.
    
        Args:
            path (str): The full path name of a file or folder, e.g. "omniverse://ov-content/Users/me".
            timeout (float): Number of seconds to try before erroring out.  Default 10.
    
        Returns:
            str: obliterated path name
    
        Raises:
            :obj:`RuntimeWarning`: If error or timeout.
    
        
    """
def obliterate_items(items: [omni.kit.widget.filebrowser.model.FileBrowserItem], view: omni.kit.window.filepicker.view.FilePickerView):
    """
    
        Obliterate given items. Upon success, executes the given callback.
    
        Args:
            items ([:obj:`FileBrowserItem`]): Items to obliterate.
            callback (Callable): Callback to execute upon success.  Function signature is void callback([str]).
    
        Raises:
            :obj:`Exception`
    
        
    """
def open_in_file_browser(item: omni.kit.widget.filebrowser.model.FileBrowserItem):
    """
    
        Open the given file item in the OS's native file browser.
    
        Args:
            item (FileBrowserItem): Selected item of the Content Browser.
    
        Returns:
            None
    
        
    """
def refresh_connection(item: omni.kit.widget.filebrowser.model.FileBrowserItem, view: omni.kit.window.filepicker.view.FilePickerView):
    """
    
        Reconnect current server for the given view
    
        Args:
            item (:obj:`FileBrowserItem`): The FileBrowserItem to refresh the connection from.
            view (:obj:`FilePickerView`): The FilePickerView own the item.
        
    """
def refresh_item(item: omni.kit.widget.filebrowser.model.FileBrowserItem, view: omni.kit.window.filepicker.view.FilePickerView):
    """
    
        Refresh the UI for the item.
    
        Args:
            item(:obj:'FileBrowserItem'): The item to refresh the UI for.
            view(:obj:'FilePickerView'): The view that is own the item.
        
    """
def remove_connection(item: omni.kit.widget.filebrowser.model.FileBrowserItem, view: omni.kit.window.filepicker.view.FilePickerView):
    """
    
        Remove a connection for the file browser item with a confirm dialog.
    
        Args:
            item (:obj:`FileBrowserItem`): The FileBrowserItem to remove the connection from.
            view (:obj:`FilePickerView`): The FilePickerView own the item.
        
    """
def rename_file(item: omni.kit.widget.filebrowser.model.FileBrowserItem, view: omni.kit.window.filepicker.view.FilePickerView, new_name: str):
    """
    
        Rename the item with a new name.
    
        Args:
            item(:obj:'FileBrowserItem'): The item to rename .
            view(:obj:'FilePickerView'): The view that is own the item.
            new_name(str): The new name for the item.
        
    """
def rename_file_async(src_path: str, dst_path: str, callback: typing.Callable = None):
    """
    
        Rename item. Upon success, executes the given callback.
    
        Args:
            src_path (str): Path of item to rename.
            dst_path (str): Destination path to rename to.
            callback (func): Callback to execute upon success.  Function signature is void callback([str]).
    
        Raises:
            :obj:`Exception`
        
    """
def rename_item(item: omni.kit.widget.filebrowser.model.FileBrowserItem, view: omni.kit.window.filepicker.view.FilePickerView):
    """
    
        Rename the item with a dialog.
    
        Args:
            item(:obj:'FileBrowserItem'): The item to rename .
            view(:obj:'FilePickerView'): The view that is own the item.
        
    """
def restore_item_async(path: str, timeout: float = 10.0) -> str:
    """
    
        Async function.  restore the item at the given path name.
    
        Args:
            path (str): The full path name of a file or folder, e.g. "omniverse://ov-content/Users/me".
            timeout (float): Number of seconds to try before erroring out.  Default 10.
    
        Returns:
            str: restore path name
    
        Raises:
            :obj:`RuntimeWarning`: If error or timeout.
    
        
    """
def restore_items(items: [omni.kit.widget.filebrowser.model.FileBrowserItem], view: omni.kit.window.filepicker.view.FilePickerView):
    """
    
        Restore given items. Upon success, executes the given callback.
    
        Args:
            items ([:obj:`FileBrowserItem`]): Items to restore.
            callback (Callable): Callback to execute upon success.  Function signature is void callback([str]).
    
        Raises:
            :obj:`Exception`
    
        
    """
