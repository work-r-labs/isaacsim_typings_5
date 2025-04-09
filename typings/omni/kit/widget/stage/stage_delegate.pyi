from __future__ import annotations
import _asyncio
import asyncio as asyncio
from functools import partial
import inspect as inspect
from omni.kit.widget.stage.abstract_stage_column_delegate import AbstractStageColumnDelegate
from omni.kit.widget.stage.abstract_stage_column_delegate import StageColumnItem
from omni.kit.widget.stage.context_menu import ContextMenu
from omni.kit.widget.stage.delegates.name_column_delegate import NameColumnDelegate
from omni.kit.widget.stage.stage_item import StageItem
from omni import ui
import omni.ui._ui
import pxr.Usd
import weakref as weakref
__all__: list = ['StageDelegate']
class AwaitWithFrame:
    """
    
        A future-like object that runs the given future and makes sure it's
        always in the given frame's scope. It allows creating widgets
        asynchronously.
        
    """
    def __await__(self):
        ...
    def __init__(self, frame: omni.ui._ui.Frame, future: _asyncio.Future):
        ...
class ContextMenuEvent:
    """
    The object comatible with ContextMenu
    """
    def __init__(self, stage: pxr.Usd.Stage, path_string, expanded = None):
        ...
class ContextMenuHandler:
    """
    The object that the ContextMenu calls to expand the item
    """
    collapse_fn = ...
    expand_fn = ...
    def __init__(self):
        ...
    def _collapse(self, path):
        ...
    def _expand(self, path):
        ...
    def context_menu_handler(self, cmd, prim_path):
        ...
class StageDelegate(omni.ui._ui.AbstractItemDelegate):
    collapse_fn = ...
    expand_fn = ...
    model = ...
    def _StageDelegate__on_header_hovered(self, hovered):
        ...
    def _StageDelegate__on_stage_items_destroyed(self, items: typing.List[omni.kit.widget.stage.stage_item.StageItem]):
        ...
    def __init__(self, **kwargs):
        ...
    def build_branch(self, model, item, column_id, level, expanded):
        """
        Create a branch widget that opens or closes subtree
        """
    def build_header(self, column_id):
        ...
    def build_widget(self, model, item, column_id, level, expanded):
        """
        Create a widget per item
        """
    def destroy(self):
        ...
    def get_name_column_delegate(self):
        ...
    def on_mouse_pressed(self, button, stage: pxr.Usd.Stage, item, expanded):
        """
        Called when the user press the mouse button on the item
        """
    def set_column_delegates(self, delegates):
        """
        Add custom columns
        """
    def set_highlighting(self, enable: bool = None, text: str = None):
        """
        
                Specify if the widgets should consider highlighting. Also set the text that should be highlighted in flat mode.
                
        """
