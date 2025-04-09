from __future__ import annotations
import colorsys as colorsys
from omni.kit.graph.delegate.default.delegate_closed import GraphNodeDelegateClosed
from omni.kit.graph.delegate.default.delegate_full import GraphNodeDelegateFull
from omni.kit.widget.graph.graph_model import GraphModel
import omni.kit.widget.graph.graph_node_delegate_router
from omni.kit.widget.graph.graph_node_delegate_router import GraphNodeDelegateRouter
from omni import ui
import omni.ui.color_utils
import pathlib
from pathlib import Path
__all__ = ['BACKGROUND_COLOR', 'BORDER_DEFAULT', 'BORDER_SELECTED', 'CONNECTION', 'CURRENT_PATH', 'GraphModel', 'GraphNodeDelegate', 'GraphNodeDelegateClosed', 'GraphNodeDelegateFull', 'GraphNodeDelegateRouter', 'ICON_PATH', 'LABEL_COLOR', 'NODE_BACKGROUND', 'NODE_BACKGROUND_SELECTED', 'Path', 'cl', 'color_to_hex', 'colorsys', 'hex_to_color', 'ui']
class GraphNodeDelegate(omni.kit.widget.graph.graph_node_delegate_router.GraphNodeDelegateRouter):
    """
    
        The delegate with the Omniverse design that has both full and collapsed states.
        
    """
    @staticmethod
    def get_style(border = None, background = None, node_background = None, icon_background = None, border_selected = None, node_background_selected = None):
        """
        Return style that can be used with this delegate
        """
    @staticmethod
    def specialized_color_style(name, color, icon, icon_tint_color = None):
        """
        
                Return part of the style that has everything to color special node type.
        
                Args:
                    name: Node type
                    color: Node color
                    icon: Filename to the icon the node type should display
                    icon_tint_color: Icon tint color
                
        """
    @staticmethod
    def specialized_port_style(name, color):
        """
        
                Return part of the style that has everything to color the customizable part of the port.
        
                Args:
                    name: Port type type
                    color: Port color
                
        """
    def __init__(self):
        ...
def color_to_hex(color: tuple) -> int:
    """
    Convert float rgb to int
    """
def hex_to_color(hex: int) -> tuple:
    ...
BACKGROUND_COLOR: int = 4281610282
BORDER_DEFAULT: int = 4292585046
BORDER_SELECTED: int = 4294967295
CONNECTION: int = 4286628480
CURRENT_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.graph.delegate.default-1.2.2/omni/kit/graph/delegate/default')
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.graph.delegate.default-1.2.2/icons')
LABEL_COLOR: int = 4290032820
NODE_BACKGROUND: int = 4284962899
NODE_BACKGROUND_SELECTED: int = 4286540902
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
