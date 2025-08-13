from __future__ import annotations
from carb import eventdispatcher
import carb.eventdispatcher._eventdispatcher
from carb import log_warn
import omni as omni
from omni.kit.window.filepicker.utils import exec_after_redraw
__all__: list[str] = ['BOOKMARK_ADDED_GLOBAL_EVENT', 'BOOKMARK_DELETED_GLOBAL_EVENT', 'BOOKMARK_RENAMED_GLOBAL_EVENT', 'FilePickerExtension', 'NUCLEUS_SERVER_ADDED_GLOBAL_EVENT', 'NUCLEUS_SERVER_DELETED_GLOBAL_EVENT', 'NUCLEUS_SERVER_RENAMED_GLOBAL_EVENT', 'eventdispatcher', 'exec_after_redraw', 'g_singleton', 'get_instance', 'log_warn', 'omni']
class FilePickerExtension(omni.ext._extensions.IExt):
    """
    
        The filepicker extension is not necessarily integral to using the widget.  However, it is useful for handling
        singleton tasks for the class.
    
        
    """
    def _update_persistent_bookmarks(self, event: carb.eventdispatcher._eventdispatcher.Event):
        """
        When a bookmark is updated or deleted, update persistent settings
        """
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
def get_instance():
    ...
BOOKMARK_ADDED_GLOBAL_EVENT: str = 'omni.kit.window.filepicker.BOOKMARK_ADDED'
BOOKMARK_DELETED_GLOBAL_EVENT: str = 'omni.kit.window.filepicker.BOOKMARK_DELETED'
BOOKMARK_RENAMED_GLOBAL_EVENT: str = 'omni.kit.window.filepicker.BOOKMARK_RENAMED'
NUCLEUS_SERVER_ADDED_GLOBAL_EVENT: str = 'omni.kit.window.filepicker.NUCLEUS_SERVER_ADDED'
NUCLEUS_SERVER_DELETED_GLOBAL_EVENT: str = 'omni.kit.window.filepicker.NUCLEUS_SERVER_DELETED'
NUCLEUS_SERVER_RENAMED_GLOBAL_EVENT: str = 'omni.kit.window.filepicker.NUCLEUS_SERVER_RENAMED'
g_singleton: FilePickerExtension  # value = <omni.kit.window.filepicker.extension.FilePickerExtension object>
