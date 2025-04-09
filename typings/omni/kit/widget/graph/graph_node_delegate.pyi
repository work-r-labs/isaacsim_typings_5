"""
This module provides the GraphNodeDelegate class with styling and routing functionality for graph node representations in NVIDIA's Omniverse applications.
"""
from __future__ import annotations
from omni.kit.widget.graph.graph_model import GraphModel
from omni.kit.widget.graph.graph_node_delegate_closed import GraphNodeDelegateClosed
from omni.kit.widget.graph.graph_node_delegate_full import GraphNodeDelegateFull
import omni.kit.widget.graph.graph_node_delegate_router
from omni.kit.widget.graph.graph_node_delegate_router import GraphNodeDelegateRouter
from omni import ui
import pathlib
from pathlib import Path
__all__: list = ['GraphNodeDelegate']
class GraphNodeDelegate(omni.kit.widget.graph.graph_node_delegate_router.GraphNodeDelegateRouter):
    """
    A class providing styling and routing for graph node representations in Omniverse applications.
    
        This delegate offers a customizable interface for nodes within a graph, allowing them to be displayed with a unified Omniverse design. It supports both fully expanded and collapsed states for the nodes.
        
    """
    @staticmethod
    def get_style():
        """
        Gets the style dictionary for the graph node delegate.
        
                Returns:
                    dict: A dictionary containing the style configuration for the graph node delegate.
        """
    @staticmethod
    def specialized_color_style(name, color, icon, icon_tint_color = None):
        """
        Return part of the style that has everything to color special node type.
        
                Args:
                    name (str): Node type
                    color (int): Node color
                    icon (str): Filename to the icon the node type should display
                    icon_tint_color (int, optional): Icon tint color
        
                Returns:
                    dict: A dictionary containing the specialized color style for a node type.
        """
    @staticmethod
    def specialized_port_style(name, color):
        """
        Return part of the style that has everything to color the customizable part of the port.
        
                Args:
                    name (str): Port type
                    color (int): Port color
        
                Returns:
                    dict: A dictionary containing the specialized port style configuration.
        """
    def __init__(self):
        """
        Initialize the GraphNodeDelegate with full and collapsed states.
        """
BACKGROUND_COLOR: int = 4281610282
BORDER_DEFAULT: int = 4292585046
BORDER_SELECTED: int = 4294967295
CONNECTION: int = 4286628480
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.graph-1.12.17+d02c707b/omni/kit/widget/graph')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.graph-1.12.17+d02c707b/icons')
LABEL_COLOR: int = 4290032820
NODE_BACKGROUND: int = 4284962899
NODE_BACKGROUND_SELECTED: int = 4286540902
