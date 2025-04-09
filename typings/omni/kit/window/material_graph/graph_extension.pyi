from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import omni as omni
from omni.kit.widget.graph.graph_model import GraphModel
from omni.kit.window.material_graph import compound_registry
from omni.kit.window.material_graph.graph_actions import deregister_actions
from omni.kit.window.material_graph.graph_actions import register_actions
from omni.kit.window.material_graph.graph_hotkeys import deregister_hotkeys
from omni.kit.window.material_graph.graph_hotkeys import register_hotkeys
from omni.kit.window.material_graph.graph_window import GraphWindow
from omni.kit.window.material_graph.mdl_node_tree_delegate import MdlNodeTreeDelegate
from omni.kit.window.material_graph.mdl_node_tree_model import MdlNodeTreeQuickSearchModel
from omni.kit.window.material_graph.usdshade_graph_model import UsdShadeGraphModel
from omni import ui
import pathlib
from pathlib import Path
import pxr.Sdf
from pxr import Sdf
from pxr import Usd
from pxr import UsdShade
import typing
__all__: list = ['GraphExtension']
class GraphExtension(omni.ext._extensions.IExt):
    """
    The entry point for MDL Material Graph
    """
    MENU_PATH: typing.ClassVar[str] = 'Window/MDL Material Graph'
    WINDOW_NAME: typing.ClassVar[str] = 'Material Graph'
    @staticmethod
    def add_node(mime_data: str):
        """
        Adds a node to the current Material Graph window
        """
    @staticmethod
    def filter_paste_nodes(prim_spec: pxr.Sdf.PrimSpec) -> bool:
        """
        Return True for nodes that are valid to paste into this graph, False if they aren't valid.
        
                Args:
                    prim_spec (Sdf.PrimSpec): PrimSpec to check for validity.
        
                Returns:
                    bool: True for Valid, False for Invalid.
                
        """
    @staticmethod
    def refresh_compounds():
        """
        Register default compounds
        """
    @staticmethod
    def show_materials(prim_list: typing.List[pxr.Usd.Prim]):
        """
        Show materials in Material Graph window
        """
    def __init__(self):
        ...
    def _destroy_window_async(self):
        ...
    def _is_window_focused(self) -> bool:
        """
        Returns True if the MDL Material Graph window exists and focused
        """
    def _menu_show_window(self, menu, value):
        ...
    def _on_extensions_changed(self, loaded: bool, ext_id: str):
        """
        Called when the Quick Search extension is loaded/unloaded
        """
    def _on_hotkey_ext_changed(self, ext_id: str, ext_change_type: omni.ext._extensions.ExtensionStateChangeType):
        ...
    def _register_stage_menu(self):
        ...
    def _unregister_stage_menu(self):
        ...
    def _visiblity_changed_fn(self, visible):
        ...
    def focus_on_nodes(self, nodes: typing.Optional[typing.List[typing.Any]] = None):
        ...
    def graph_copy(self):
        ...
    def graph_paste(self):
        ...
    def layout_all(self):
        ...
    def material_unpause_and_pause(self):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def set_expansion(self, mode: str):
        """
        Set the expansion mode of all graph nodes to be:
                "open", "minimize", or "close".
        
                Args:
                    mode (str): "open", "minimize", or "close"
                
        """
    def show_window(self, menu, value):
        """
        Show/hide the window
        """
    def toggle_material_compilation(self):
        ...
COMPOUND_DEFAULT_PATH: str = '${data}/shadergraphs'
COMPOUND_PATH_SETTING: str = '/persistent/exts/omni.kit.window.material_graph/compoundPaths'
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/omni/kit/window/material_graph')
MDL_AUTOGEN_PATH: str = '${data}/shadergraphs/mdl_usd'
SHADERS_PATH: str = '/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/data/shaders'
_extension_instance: GraphExtension  # value = <omni.kit.window.material_graph.graph_extension.GraphExtension object>
