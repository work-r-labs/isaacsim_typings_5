from __future__ import annotations
from omni.kit.viewport.window.extension import ViewportWindowExtension
from omni.kit.viewport.window.window import ViewportWindow
from . import dragdrop
from . import events
from . import extension
from . import layers
from . import legacy
from . import manipulator
from . import menu_entry
from . import raycast
from . import scene
from . import stats
from . import viewport_actions
from . import window
__all__: list = ['ViewportWindow', 'get_viewport_window_instances', 'set_viewport_window_default_style']
def get_viewport_window_instances(usd_context_name: str | None = ''):
    """
    
        Get all known ViewportWindow instances, optionally filtering with a UsdContext name.
    
        Args:
            usd_context_name (str, None): An optional argument to limit enumeration to ViewportWindows attached to a
                specific UsdContext.
        Returns:
            An iterable object for enumerating all found ViewportWindow instances.
        
    """
def set_viewport_window_default_style(style: dict, overwrite: bool = False, usd_context_name: str | None = '', apply: bool = True):
    """
    
        Set the default style for all ViewportWindows, optionally filtering based on the UsdContext the ViewportWindow
        is attached to.
    
        Args:
            style (dict): An omni.ui style dictionary
            overwrite (bool): Whether to overwrite any existing style or augment it.
            usd_context_name (str, None): An optional argument to limit application to ViewportWindows attached to a
                specific UsdContext.
            apply (bool): Whether to apply the style to existing ViewportWindows, or not.
        
    """
