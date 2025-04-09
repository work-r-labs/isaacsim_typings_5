from __future__ import annotations
import omni.kit.widget.zoombar.zoom_bar
from omni.kit.widget.zoombar.zoom_bar import ZoomBar
__all__ = ['FileZoomBar', 'ZoomBar']
class FileZoomBar(omni.kit.widget.zoombar.zoom_bar.ZoomBar):
    """
    
        Reprent a zoom bar used for file system to replace omni.kit.window.filepicker.ZoomBar with same args.
    
        Keyword args:
            grid_view_scale (int): Initial value of the slider. Default 2.
            show_grid_view (bool): Show in icon mode or detail mode. Default False means show in detail mode.
            on_toggle_grid_view_fn (callable): Function called when view mode changed. Default None, also means view mode will never be changed. Function signure:
                void on_toggle_grid_view_fn(icon_mode: bool)
            on_scale_grid_view_fn (callable): Function called when slider value changed. Value is mapped to {0: 0.25, 1: 0.5, 2: 0.75, 3: 1, 4: 1.5, 5: 2.0}.
                Default None. Function signure:
                void on_scale_grid_view_fn(value: float)
        
    """
    def __init__(self, show_grid_view: bool = False, grid_view_scale: int = 2, on_toggle_grid_view_fn: callable = None, on_scale_grid_view_fn: callable = None):
        ...
    def _on_scale_grid_view(self, value: int):
        ...
