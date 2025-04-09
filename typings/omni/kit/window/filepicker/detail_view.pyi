from __future__ import annotations
import asyncio as asyncio
from carb import log_warn
from collections import OrderedDict
from collections import namedtuple
from datetime import datetime
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.helper.file_utils import asset_types
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.window.filepicker.style import get_style
from omni import ui
import os as os
import pathlib
import typing
__all__: list = ['DetailFrameController', 'ExtendedFileInfo', 'DetailView']
class DetailFrameController:
    def __init__(self, glyph: str = None, build_fn: typing.Callable[[], NoneType] = None, selection_changed_fn: typing.Callable[[typing.List[str]], NoneType] = None, filename_changed_fn: typing.Callable[[str], NoneType] = None, destroy_fn: typing.Callable[[], NoneType] = None, **kwargs):
        """
        
                Initialize the Detail Frame. 
                
                Keyword Args:
                    glyph (Optional[str]): The name of the glyph to use for the widget.
                    build_fn (Callable): A function that will be called when build the detail frame.
                                            Function signature:void build_fn()
                    selection_changed_fn (Callable): A function that will be called when the selection changes.
                                            Function signature:void selection_changed_fn(list[str])
                    filename_changed_fn (Callable): A function that will be called when the filename of current item changes.
                                            Function signature:void filename_changed_fn(str)
                    destroy_fn (Callable): A function that will be called when the widget is destroyed.
                                            Function signature:void destroy_fn()
                
        """
    def build_header(self, collapsed: bool, title: str):
        """
        
                Builds the header. It is used to show the header of the DetailFrame.
                Args:
                    collapsed (bool): True if the header is collapsed.
                    title (str): title of the header to be shown.
                
        """
    def build_ui(self, frame: omni.ui._ui.Frame):
        """
        
                Builds the UI. 
                Args:
                    frame (ui.Frame): The frame that will be used to build the UI.
                
        """
    def destroy(self):
        """
         Destructor 
        """
    def on_filename_changed(self, filename: str):
        """
        
                Called when the filename has changed.It will rebuild the detail frame.
                
                Args:
                    filename (str): The filename that has changed. 
                
        """
    def on_selection_changed(self, selected: typing.List[str] = list()):
        """
        
                 Called when the selection changes. It will rebuild the detail frame.
                 
                 Keywords Args:
                      selected(List[str]): List of selected items's path.
                
        """
class DetailView:
    """
     Detail view that contains all detail frames
    """
    def __init__(self, **kwargs):
        ...
    def _build_detail_frames(self):
        ...
    def _build_ui(self):
        ...
    def add_detail_frame(self, name: str, glyph: str, build_fn: typing.Callable[[], omni.ui._ui.Widget], selection_changed_fn: typing.Callable[[typing.List[str]], NoneType] = None, filename_changed_fn: typing.Callable[[str], NoneType] = None, destroy_fn: typing.Callable[[omni.ui._ui.Widget], NoneType] = None):
        """
        
                Adds sub-frame to the detail view, and populates it with a custom built widget.
        
                Args:
                    name (str): Name of the widget sub-section, this name must be unique over all detail sub-sections.
                    glyph (str): Associated glyph to display for this subj-section
                    build_fn (Callable): This callback function builds the widget.
        
                Keyword Args:
                    selection_changed_fn (Callable): This callback is invoked to handle selection changes.
                    filename_changed_fn (Callable): This callback is invoked when filename is changed.
                    destroy_fn (Callable): Cleanup function called when destroyed.
        
                
        """
    def add_detail_frame_from_controller(self, name: str, detail_frame: DetailFrameController = None):
        """
        
                Adds sub-frame to the detail view, and populates it with a custom built widget.
        
                Args:
                    name (str): Name of the widget sub-section, this name must be unique over all detail sub-sections.
                    controller (:obj:`DetailFrameController`): Controller object that encapsulates all aspects of creating,
                        updating, and deleting a detail frame widget.
        
                
        """
    def delete_detail_frame(self, name: str):
        """
        
                Deletes the specified detail frame.
        
                Args:
                    name (str): Name of the detail frame.
        
                
        """
    def destroy(self):
        """
         Destructor 
        """
    def get_detail_frame(self, name: str) -> DetailFrameController:
        """
        
                Get the detail frame by given name. This method is thread safe. Use with caution
                
                Args:
                    name: Name of the detail frame
                
                Returns: 
                    :obj:'DetailFrameController' with given name or None if not found
                
        """
    def on_filename_changed(self, filename: str = ''):
        """
        
                When the user edits the filename, invokes the callbacks for the detail frames.
        
                Args:
                    filename (str): Current filename.
        
                
        """
    def on_selection_changed(self, selected: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem] = list()):
        """
        
                When the user changes their filebrowser selection(s), invokes the callbacks for the detail frames.
        
                Args:
                    selected (:obj:`FileBrowserItem`): List of new selections.
        
                
        """
class ExtendedFileInfo(DetailFrameController):
    """
     Extended file info show in detail view
    """
    class MockListEntry(tuple):
        """
        MockListEntry(relative_path, modified_time, created_by, modified_by, size)
        """
        __match_args__: typing.ClassVar[tuple] = ('relative_path', 'modified_time', 'created_by', 'modified_by', 'size')
        __slots__: typing.ClassVar[tuple] = tuple()
        _field_defaults: typing.ClassVar[dict] = {}
        _fields: typing.ClassVar[tuple] = ('relative_path', 'modified_time', 'created_by', 'modified_by', 'size')
        @staticmethod
        def __new__(_cls, relative_path, modified_time, created_by, modified_by, size):
            """
            Create new instance of MockListEntry(relative_path, modified_time, created_by, modified_by, size)
            """
        @classmethod
        def _make(cls, iterable):
            """
            Make a new MockListEntry object from a sequence or iterable
            """
        def __getnewargs__(self):
            """
            Return self as a plain tuple.  Used by copy and pickle.
            """
        def __repr__(self):
            """
            Return a nicely formatted representation string
            """
        def _asdict(self):
            """
            Return a new dict which maps field names to their values.
            """
        def _replace(self, **kwds):
            """
            Return a new MockListEntry object replacing specified fields with new values
            """
    _empty_list_entry: typing.ClassVar[MockListEntry]  # value = MockListEntry(relative_path='File info', modified_time=datetime.datetime(2025, 4, 9, 16, 52, 43, 524721), created_by='', modified_by='', size=0)
    def __init__(self):
        ...
    def _build_ui_async(self, selected: typing.List[str] = list()):
        ...
    def _build_ui_impl(self, selected: typing.List[str] = list()):
        ...
    def _destroy_impl(self, _):
        ...
    def _on_file_change_event(self, result: omni.client.impl._omniclient.Result, entry: omni.client.impl._omniclient.ListEntry):
        ...
    def _on_selection_changed_impl(self, selected: typing.List[str] = list()):
        ...
    def build_header(self, collapsed: bool, title: str):
        """
        
                Builds the header. It is used to show the header of the file info.
                Args:
                    collapsed (bool): True if the header is collapsed.
                    title (str): title of the header to be shown.
                
        """
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.filepicker-2.11.7+d02c707b/icons/NvidiaDark')
