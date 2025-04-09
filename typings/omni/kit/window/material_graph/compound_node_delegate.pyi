from __future__ import annotations
from functools import partial
import omni.kit.graph.delegate.default.compound_node_delegate
from omni.kit.graph.delegate.default.compound_node_delegate import CompoundInputOutputNodeDelegate as CompDelegateBase
from omni.kit.graph.delegate.default.compound_node_delegate import CompoundNodeDelegate as CompoundNodeDelegateBase
import omni.kit.widget.graph.abstract_graph_node_delegate
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeDescription
from omni.kit.widget.graph.abstract_graph_node_delegate import GraphNodeLayout
from omni.kit.widget.graph.graph_model import GraphModel
from omni.kit.window.material_graph.export_utils import Export
from omni.kit.window.material_graph.svg_picker import SvgPicker
from omni import ui
__all__ = ['CompDelegateBase', 'CompoundInputOutputNodeDelegate', 'CompoundNodeDelegate', 'CompoundNodeDelegateBase', 'Export', 'GraphModel', 'GraphNodeDescription', 'GraphNodeLayout', 'SvgPicker', 'partial', 'ui']
class CompoundInputOutputNodeDelegate(omni.kit.graph.delegate.default.compound_node_delegate.CompoundInputOutputNodeDelegate):
    def _mouse_pressed_fn(self, model, node, x, y, button, modifier):
        ...
    def node_background(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create widgets of the node background
        """
class CompoundNodeDelegate(omni.kit.graph.delegate.default.compound_node_delegate.CompoundNodeDelegate):
    """
    
        The delegate for the compound nodes.
        
    """
    def __init__(self):
        ...
    def _mouse_pressed_fn(self, model, node, x, y, button, modifier):
        ...
    def destroy(self):
        ...
    def get_node_layout(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to determine the node layout
        """
    def node_background(self, model, node_desc: omni.kit.widget.graph.abstract_graph_node_delegate.GraphNodeDescription):
        """
        Called to create widgets of the node background
        """
