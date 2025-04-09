from __future__ import annotations
from carb import events
import carb.events._events
from carb import log_warn
import omni as omni
from omni.kit.window.filepicker.utils import exec_after_redraw
__all__ = ['BOOKMARK_ADDED_EVENT', 'BOOKMARK_DELETED_EVENT', 'BOOKMARK_RENAMED_EVENT', 'FilePickerExtension', 'NUCLEUS_SERVER_ADDED_EVENT', 'NUCLEUS_SERVER_DELETED_EVENT', 'NUCLEUS_SERVER_RENAMED_EVENT', 'events', 'exec_after_redraw', 'g_singleton', 'get_instance', 'log_warn', 'omni']
class FilePickerExtension(omni.ext._extensions.IExt):
    """
    
        The filepicker extension is not necessarily integral to using the widget.  However, it is useful for handling
        singleton tasks for the class.
    
        
    """
    def _update_persistent_bookmarks(self, event: carb.events._events.IEvent):
        """
        When a bookmark is updated or deleted, update persistent settings
        """
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
def get_instance():
    ...
BOOKMARK_ADDED_EVENT: int = 14293204382964729133
BOOKMARK_DELETED_EVENT: int = 12591526458620793410
BOOKMARK_RENAMED_EVENT: int = 2010616043326768797
NUCLEUS_SERVER_ADDED_EVENT: int = 2703271046647040724
NUCLEUS_SERVER_DELETED_EVENT: int = 7113468990364096071
NUCLEUS_SERVER_RENAMED_EVENT: int = 8294859433106236004
g_singleton: FilePickerExtension  # value = <omni.kit.window.filepicker.extension.FilePickerExtension object>
