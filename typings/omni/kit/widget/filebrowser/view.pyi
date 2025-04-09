"""

An abstract View class, subclassed by TreeView and GridView.
"""
from __future__ import annotations
from abc import abstractmethod
import omni as omni
from omni.kit import async_engine
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserModel
import threading as threading
__all__: list = ['FileBrowserView']
class FileBrowserView:
    """
    
        Base class for :obj:`FileBrowserGridView` and :obj:`FileBrowserTreeView`.
    
        Args:
            model (:obj:`FileBrowserModel`): the model to use.
        
    """
    def __init__(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel):
        ...
    def _on_item_changed(self, model, item):
        """
        Called by the model when something is changed
        """
    def _on_model_changed(self, model):
        """
        Called by the model when something is changed
        """
    def _on_selection_changed(self, selections: [omni.kit.widget.filebrowser.model.FileBrowserItem]):
        ...
    def _throttled_refresh_ui(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem = None, callback: typing.Callable = None, throttle_frames: int = 1):
        """
        
                Refresh the view. Delays the redraw to a later frame so that multiple calls to this function
                are queued up and handled in one go. For example, when multiple files are copied to the current
                directory, it will trigger a refresh for each file. If there are many of them, it could swamp
                the render queue with unnecessary redraws. By queueing up these tasks, we can limit the redraws
                to once per frame.
                
        """
    def _throttled_refresh_ui_async(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, callback: typing.Callable, throttle_frames: int = 1):
        ...
    def build_ui(self):
        """
         Build the UI. 
        """
    def destroy(self):
        """
         Destructor. 
        """
    def refresh_ui(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem = None):
        """
        
                Update the UI.
        
                Args:
                    item (:obj:`FileBrowserItem`): The item to refresh.
                
        """
    def select_and_center(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        """
        
                Select and center the view on the given item.
                Args:
                    item (:obj:`FileBrowserItem`): the item to set the new selection to.
                
        """
    def set_root(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        """
         Set the root item. 
        """
    @property
    def model(self):
        """
         Return the model of the view. 
        """
    @model.setter
    def model(self, model):
        ...
    @property
    def visible(self):
        """
         Return visiblity of the view. 
        """
    @visible.setter
    def visible(self, visible: bool):
        ...
