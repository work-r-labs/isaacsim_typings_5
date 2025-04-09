"""
MaterialListItem, MaterialListModel & MaterialListDelegate classes, used by MaterialListBoxWidget.
"""
from __future__ import annotations
import asyncio as asyncio
import copy as copy
import omni as omni
from omni.kit.material.library.material_utils import UpdateState
from omni.kit.material.library.thumbnail_loader import ThumbnailLoader
from omni import ui
from pxr import Sdf
import typing
import weakref as weakref
__all__: list = ['MaterialListItem', 'MaterialListModel', 'MaterialListDelegate']
class Constant:
    """
    Constant class, used by MaterialListModel & MaterialListDelegate.
    """
    SDF_PATH_INVALID: typing.ClassVar[str] = '$NONE$'
    def __setattr__(self, name, value):
        ...
class MaterialListDelegate(omni.ui._ui.AbstractItemDelegate):
    """
    
        Delegate is the representation layer. TreeView calls the methods
        of the delegate to create custom widgets for each item. Used by MaterialListBoxWidget.
        
    """
    def __init__(self, flat = False):
        ...
    def _get_prim(self, prim_path):
        ...
    def build_branch(self, model, item, column_id, level, expanded):
        """
        Create a branch widget that opens or closes subtree
        """
    def build_widget(self, model, item, column_id, level, expanded):
        ...
    def clean(self):
        ...
class MaterialListItem(omni.ui._ui.AbstractItem):
    """
    Single item model class, used by MaterialListModel.
    """
    def __init__(self, text):
        ...
    def __repr__(self):
        ...
    def prefilter(self, filter_name_text: str):
        ...
class MaterialListModel(omni.ui._ui.AbstractItemModel):
    """
    List model class, used by MaterialListBoxWidget.
    """
    _instance = None
    @staticmethod
    def update_children(new_list: list, percent: int, state: omni.kit.material.library.material_utils.UpdateState):
        ...
    def __init__(self, placeholder_fn = None, update_list_model_fn = None, filter_fn = None, get_materials_async_fn = None):
        ...
    def clean(self):
        ...
    def execute(self, item):
        """
         here we bind the material into the Scene
        """
    def filter_by_text(self, filter_name_text: str):
        """
        Specify the filter string that is used to reduce the model
        """
    def get_drag_mime_data(self, item):
        """
        Returns Multipurpose Internet Mail Extensions (MIME) data for be able to drop this item somewhere
        """
    def get_item_children(self, item):
        """
        Returns all the children when the widget asks it.
        """
    def get_item_value_model(self, item, column_id):
        ...
    def get_item_value_model_count(self, item):
        """
        The number of columns
        """
