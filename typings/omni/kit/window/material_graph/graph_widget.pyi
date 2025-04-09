from __future__ import annotations
import asyncio as asyncio
import carb as carb
from functools import partial
import json as json
import omni as omni
from omni.kit.graph.delegate.default.backdrop_delegate import BackdropDelegate
from omni.kit.graph.editor.core.graph_editor_core_widget import GraphEditorCoreWidget
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.graph.graph_model import GraphModel
from omni.kit.widget.material_preview.material_preview_producer import MaterialPreviewProducer
from omni.kit.window.filepicker.dialog import FilePickerDialog
from omni.kit.window.material_graph.compound_node_delegate import CompoundInputOutputNodeDelegate
from omni.kit.window.material_graph.compound_node_delegate import CompoundNodeDelegate
from omni.kit.window.material_graph.graph_view import MaterialGraphView
from omni.kit.window.material_graph.graphnode_delegate import GraphNodeDelegate
from omni.kit.window.material_graph.mdl_node_tree_delegate import MdlNodeTreeDelegate
from omni.kit.window.material_graph.mdl_node_tree_model import MdlNodeItem
from omni.kit.window.material_graph.mdl_node_tree_model import MdlNodeTreeModel
from omni.kit.window.material_graph.usdshade_graph_model import UsdShadeGraphModel
from omni import ui
import pathlib
from pathlib import Path
import pxr.Sdf
from pxr import Sdf
from pxr import Tf
from pxr import UsdShade
import traceback as traceback
import webbrowser as webbrowser
__all__: list = ['GraphWidget']
class GraphWidget(omni.kit.graph.editor.core.graph_editor_core_widget.GraphEditorCoreWidget):
    @staticmethod
    def _GraphWidget__on_filter_folder(item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> bool:
        """
        Used by pick folder dialog to hide all the files
        """
    def _GraphWidget__can_export_node(self):
        ...
    def _GraphWidget__export_material(self):
        ...
    def _GraphWidget__export_node(self):
        ...
    def _GraphWidget__on_apply_folder(self, filename: str, dir: str):
        """
        Called when the user press "Use This Folder" in the pick folder dialog
        """
    def _GraphWidget__on_material_preview_drawable_changed(self):
        """
        Called by MaterialPreviewProducer when the resolution is changed
        """
    def _GraphWidget__on_selection_changed(self, items):
        ...
    def __init__(self, **kwargs):
        ...
    def _add_image(self, event: omni.ui._ui.WidgetMouseDropEvent):
        """
        
                Called to create a texture node with the image that was droppped
                to the window.
                
        """
    def _clear_compounds_dirs(self):
        ...
    def _create_new(self):
        """
        Create new material
        """
    def _get_graph_view_hovered_position(self) -> typing.Optional[typing.Tuple[float]]:
        """
        Return the position of mouse if self._graph_view is hovered
        """
    def _import_prims(self, _, prims, focus = True):
        """
        Create a model and set it to the graph view
        """
    def _import_selection(self):
        """
        Import selected prims
        """
    def _on_drag_drop_external(self, e: carb.events._events.IEvent):
        """
        Called when external drop to Kit
        """
    def _on_stage_event(self, event):
        """
        When a new stage is opened, reset the model
        """
    def _pick_folder(self):
        """
        Open Pick Folder dialog to add compounds
        """
    def _refresh_compounds(self):
        """
        Refresh left panel
        """
    def _reload(self):
        ...
    def clear_all(self):
        ...
    def destroy(self):
        ...
    def get_material_prim(self, prim_path: pxr.Sdf.Path):
        ...
    def get_specialized_style(self):
        ...
    def get_toolbar_items(self, add_pause_button = False):
        ...
    def import_material_prim_from_selection(self):
        ...
    def on_accept_drop(self, drop_data: str):
        """
        Called to check if drop_data has the acceptable shading node description
        """
    def on_build_startup(self):
        ...
    def on_catalog_context_menu(self, items: typing.List[omni.ui._ui.AbstractItem]):
        ...
    def on_drop(self, event: omni.ui._ui.WidgetMouseDropEvent):
        """
        Called to create a node that was droppped to the window
        """
    def on_frame_selected_clicked(self):
        ...
    def on_layout_clicked(self):
        ...
    def on_left_mouse_button_double_clicked(self, items):
        ...
    def on_right_mouse_button_pressed(self, items):
        ...
    def on_toolbar_create_graph_clicked(self):
        ...
    def on_toolbar_edit_clicked(self):
        ...
    def on_toolbar_edit_graph_clicked(self):
        ...
    def on_toolbar_expansion_state_clicked(self, state):
        ...
    def on_toolbar_help_clicked(self):
        ...
    def on_toolbar_view_clicked(self):
        ...
    def toggle_material_compilation(self):
        ...
    def unpause_and_pause(self):
        ...
def omni_client_exists(path):
    ...
BACKGROUND: int = 4280492319
BORDER_CONSTANT: int = 4283003026
BORDER_CONSTRUCTOR: int = 4283789427
BORDER_CUSTOM: int = 4286806879
BORDER_MATERIAL: int = 4290346652
BORDER_MATH: int = 4283664970
BORDER_MISCELLANEOUS: int = 4288183328
BORDER_NODEGRAPH: int = 4293058227
BORDER_SELECTED: int = 4294967295
BORDER_SHADER: int = 4290211954
BORDER_TEXTURE: int = 4290930268
COMPOUND_PATH_SETTING: str = '/persistent/exts/omni.kit.window.material_graph/compoundPaths'
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/omni/kit/window/material_graph')
EXT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19')
ICON_BACKGROUND: int = 4281610282
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/icons')
NODE_BACKGROUND: int = 4283121724
NODE_BACKGROUND_SELECTED: int = 4286540902
TOOLBAR_ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.window.material_graph-1.8.19/icons/toolbar')
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
