from __future__ import annotations
import asyncio as asyncio
import carb as carb
from collections import defaultdict
import functools as functools
import omni as omni
from omni.kit.widget.graph.graph_model import GraphModel
from omni.kit.widget.material_preview.material_preview_producer import MaterialPreviewProducer
from omni.kit.window.material_graph.export_utils import copy_input_metadata
from omni.kit.window.material_graph.utils import can_connect
from omni.usd.commands.stage_helper import UsdStageHelper
import os as os
import pathlib
from pathlib import Path
from pxr import Sdf
from pxr import Tf
from pxr import Trace
from pxr import Usd
import pxr.Usd
from pxr import UsdShade
from pxr import UsdUI
import tempfile as tempfile
import traceback as traceback
import typing
__all__: list = ['UsdShadeGraphModel']
class PrimNotSupportedError(Exception):
    """
    Wrong prim is passed to the model.
    """
class UsdShadeGraphModel(omni.kit.widget.graph.graph_model.GraphModel):
    """
    The model to watch the UsdShade shading network
    """
    class AttributeGroup(omni.usd.commands.stage_helper.UsdStageHelper):
        def __init__(self, stage: pxr.Usd.Stage, name: str, child_paths: typing.Optional[typing.List[pxr.Sdf.Path]] = None):
            ...
        def __repr__(self):
            ...
    DISPLAY_NAME: typing.ClassVar[str] = 'UsdShade'
    pause = ...
    @staticmethod
    def _UsdShadeGraphModel__delayed_prim_changed(*args, **kwargs):
        """
        Called to pump changes at the next frame after the changes received
        """
    @staticmethod
    def _on_objects_changed(*args, **kwargs):
        """
        Called by Usd.Notice.ObjectsChanged
        """
    @staticmethod
    def has_nodes(obj):
        """
        Returns true if the model can currently build the graph network using the provided object
        """
    @staticmethod
    def is_compound(obj):
        ...
    def _UsdShadeGraphModel__get_stage(self):
        ...
    def _UsdShadeGraphModel__remove_connections(self, prim_path, connection_to_path):
        """
        
                Scans prim_path and removes all the connections to
                connection_to_path.
                
        """
    def __init__(self, prims: typing.List[pxr.Usd.Prim]):
        ...
    def _get_connected_source(self, input):
        ...
    def _is_prim_hidden(self, prim):
        ...
    def _on_kit_selection_changed(self):
        """
        The selection in kit is changed
        """
    def _on_stage_event(self, event):
        """
        Called with omni.usd.context when stage event
        """
    def _update_dirty(self):
        """
        
                Create/remove dirty items that was collected from TfNotice. Can be
                called any time to pump changes.
                
        """
    def create_node(self, parent_item, prim_type, sub_identifier, source_asset, position = None, attributes_to_set = None):
        """
        Create a new shading node with the given identifier at the given MDL asset
        """
    def destroy(self):
        ...
    def position_begin_edit(self, item):
        ...
    def position_end_edit(self, item):
        ...
    def set_material_preview_producer(self, material_preview_producer: omni.kit.widget.material_preview.material_preview_producer.MaterialPreviewProducer):
        ...
    def set_selected_nodes_state(self, state: omni.kit.widget.graph.graph_model.GraphModel.ExpansionState):
        """
         change the state of all the selected nodes 
        """
    def size_begin_edit(self, item):
        ...
    def size_end_edit(self, item):
        ...
    @property
    def description(self, item):
        ...
    @description.setter
    def description(self, value, item = None):
        ...
    @property
    def display_color(self, item):
        ...
    @display_color.setter
    def display_color(self, value, item = None):
        ...
    @property
    def expansion_state(self, item = None):
        ...
    @expansion_state.setter
    def expansion_state(self, value: omni.kit.widget.graph.graph_model.GraphModel.ExpansionState, item: typing.Any = None):
        ...
    @property
    def icon(self, item):
        """
        Return icon of the image
        """
    @icon.setter
    def icon(self, value, item = None):
        ...
    @property
    def inputs(self, item):
        ...
    @inputs.setter
    def inputs(self, value, item = None):
        ...
    @property
    def name(self, item = None):
        ...
    @name.setter
    def name(self, value, item = None):
        ...
    @property
    def nodes(self, item: pxr.Usd.Prim = None) -> typing.Optional[typing.List[pxr.Usd.Prim]]:
        """
        
                The list of sub-nodes. When item is None, return the list of nodes in
                the model.
                
        """
    @property
    def outputs(self, item):
        ...
    @outputs.setter
    def outputs(self, value, item = None):
        ...
    @property
    def ports(self, item = None):
        """
        
                The list of sub-ports. `item` can be a node or a port.
                
        """
    @ports.setter
    def ports(self, value, item = None):
        ...
    @property
    def position(self, item = None):
        ...
    @position.setter
    def position(self, value, item = None):
        ...
    @property
    def preview(self, item):
        """
        Return the preview of the image
        """
    @preview.setter
    def preview(self, value, item = None):
        ...
    @property
    def preview_state(self, item) -> omni.kit.widget.graph.graph_model.GraphModel.PreviewState:
        ...
    @preview_state.setter
    def preview_state(self, value: omni.kit.widget.graph.graph_model.GraphModel.PreviewState, item = None):
        ...
    @property
    def selection(self) -> typing.List[pxr.Usd.Prim]:
        ...
    @selection.setter
    def selection(self, value: list):
        ...
    @property
    def size(self, item):
        ...
    @size.setter
    def size(self, value, item = None):
        ...
    @property
    def stacking_order(self, item):
        ...
    @property
    def type(self, item = None):
        ...
def handle_exception(func):
    """
    
        Decorator to print exception in async functions
        
    """
ATTRIBUTE_EMBEDDED_ICON: str = 'ui:nodegraph:node:embeddedIcon'
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/omni/kit/window/material_graph')
ICONS_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/icons')
