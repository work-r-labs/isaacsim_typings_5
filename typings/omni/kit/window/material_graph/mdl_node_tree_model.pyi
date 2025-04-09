from __future__ import annotations
import asyncio as asyncio
from collections import defaultdict
import enum
from enum import Enum
import json as json
import omni as omni
from omni.kit.window.material_graph import compound_registry
from omni import ui
import pathlib
from pathlib import Path
from pxr import Sdf
from pxr import Sdr
from pxr import Usd
from pxr import UsdShade
from pxr import UsdUI
import sys as sys
import typing
__all__: list = ['CompoundComponentItem', 'MdlFamilyGroupItem', 'MdlNodeItem', 'MdlNodeItem', 'MdlNodeTreeDelegate', 'MdlNodeTreeModel', 'MdlNodeTreeQuickSearchModel', 'MiscellaneousGroupItem', 'MiscellaneousItem']
class CompoundComponentItem(MdlNodeItem):
    def __init__(self, name: str, prim_type: str, info: str):
        ...
class MdlBaseItem(omni.ui._ui.AbstractItem):
    """
    Base item for for all items in the model
    """
    def __init__(self, item_name: str, item_info: str, item_icon: str, item_tooptip: str):
        ...
class MdlFamilyGroupItem(MdlGroupItem):
    """
    Family item of the model
    """
    def __init__(self, family: str, shader_nodes: typing.List):
        ...
    def int_type_filter(self, filter_type: str):
        ...
    def prefilter(self, filter_name_text: str):
        """
        
                Filter the children and display the ones that have the given pattern
                in the identifier.
                
        """
class MdlGroupItem(MdlBaseItem):
    """
    Base item for for all group items in the model
    """
    def __init__(self, item_name: str):
        ...
class MdlNodeItem(MdlBaseItem):
    """
    Base item for for all node items in the model
    """
    def __init__(self, item_name: str, item_info: str, item_icon: str, item_tooptip: str, prim_type, source_asset: str, sub_identifier: str):
        ...
class MdlNodeTreeModel(omni.ui._ui.AbstractItemModel):
    """
    Model that has all the shaders it's possible to create.
    """
    class Column(enum.Enum):
        """
        An enumeration.
        """
        ICON: typing.ClassVar[MdlNodeTreeModel.Column]  # value = <Column.ICON: 2>
        INFO: typing.ClassVar[MdlNodeTreeModel.Column]  # value = <Column.INFO: 1>
        NAME: typing.ClassVar[MdlNodeTreeModel.Column]  # value = <Column.NAME: 0>
        TOOLTIP: typing.ClassVar[MdlNodeTreeModel.Column]  # value = <Column.TOOLTIP: 3>
    def __del__(self):
        ...
    def __init__(self, *args):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...
    def filter_by_text(self, filter_name_text: str):
        """
        Specify the filter string that is used to reduce the model
        """
    def getNodesFromSdr(self):
        ...
    def get_drag_mime_data(self, item):
        """
        Returns data for be able to drop this item somewhere
        """
    def get_item_children(self, item):
        """
        Returns all the children when the widget asks it.
        """
    def get_item_value_model(self, item, column_id):
        """
        
                Return value model.
                It's the object that tracks the specific value.
                In our case we use ui.SimpleStringModel for the first column
                and SimpleFloatModel for the second column.
                
        """
    def get_item_value_model_count(self, item):
        """
        The number of columns
        """
    def refresh(self, nodes = list()):
        ...
    def reload(self):
        ...
class MdlNodeTreeQuickSearchModel(MdlNodeTreeModel):
    """
    
        The MDL Node model that returns children when the MDL Material Graph window
        is active.
        
    """
    def __init__(self, *args):
        ...
    def execute(self, item: typing.Any):
        """
        The user pressed enter
        """
    def filter_by_text(self, filter_name_text: str):
        """
        Specify the filter string that is used to reduce the model
        """
class MdlShaderNodeItem(MdlNodeItem):
    """
    Shader node item of the model
    """
    def __init__(self, node):
        ...
    def __repr__(self):
        ...
class MiscellaneousGroupItem(MdlGroupItem):
    """
    Has backdrop, compound, etc..
    """
    def __init__(self):
        ...
    def int_type_filter(self, filter_type: str):
        ...
    def prefilter(self, filter_name_text: str):
        """
        
                Filter the children and display the ones that have the given pattern
                in the identifier.
                
        """
class MiscellaneousItem(MdlNodeItem):
    def __init__(self, prim_type: str, info: str):
        ...
class SdrFamilyGroupItem(MdlGroupItem):
    """
    Family item of the model
    """
    def __init__(self, family: str, sdr_nodes: typing.List):
        ...
    def int_type_filter(self, filter_type: str):
        ...
    def prefilter(self, filter_name_text: str):
        """
        
                Filter the children and display the ones that have the given pattern
                in the identifier.
                
        """
class SdrNodeItem(MdlBaseItem):
    """
    Base item for for all node items in the model
    """
    def __init__(self, sdr_node):
        ...
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/omni/kit/window/material_graph')
FAMILY_TO_ICON: dict = {'Materials': 'Materials_category_dark.png', 'Materials, modifiers': 'Materials_category_dark.png', 'Texturing, high level': 'Texture_category_dark.png', 'Texturing, basic': 'Texture_category_dark.png', 'Math functions': 'Math_category_dark.png', 'Constants, State and Primvars': 'State_Data_category_dark.png', 'Constructors, conversions and swizzles': 'Conversions_category_dark.png'}
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/icons')
