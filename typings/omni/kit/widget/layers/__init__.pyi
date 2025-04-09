from __future__ import annotations
from omni.kit.usd.layers._impl.layer_utils import LayerUtils
from omni.kit.widget.layers.context_menu import ContextMenu
from omni.kit.widget.layers.extension import LayerExtension
from omni.kit.widget.layers.layer_item import LayerItem
from omni.kit.widget.layers.layer_model import LayerModel
from omni.kit.widget.layers.prim_spec_item import PrimSpecItem
from . import actions
from . import context_menu
from . import extension
from . import external_drag_drop_helper
from . import globals
from . import layer_color_scheme
from . import layer_delegate
from . import layer_icons
from . import layer_item
from . import layer_link_window
from . import layer_model
from . import layer_model_utils
from . import layer_option_button
from . import layer_settings
from . import layer_widgets
from . import link_delegate
from . import models
from . import path_utils
from . import prim_spec_item
from . import selection_watch
from . import singleton
from . import window
__all__: list = ['LayerExtension', 'ContextMenu', 'LayerItem', 'PrimSpecItem', 'LayerModel', 'LayerUtils', 'get_instance']
def get_instance():
    """
    
        Returns the instance of the LayerExtension.
    
        Returns:
            :obj:'omni.ext.IExt': The instance of the LayerExtension.
    
        
    """
