from __future__ import annotations
import carb as carb
from omni.kit.widget.zoombar.style import get_style
from omni import ui
import omni.ui._ui
__all__ = ['ZoomBar', 'carb', 'get_style', 'ui']
class ZoomBar:
    """
    
        Reprent a bar with a slider for icon size and a button to switch icon/detail mode.
    
        Keyword args:
            min (int): Min value of the slider. Default 0.
            max (int): Max value of the slider. Default 5.
            value (int): Initial value of the slider. Default 2.
            width (int): Width of the slider, in pixels. Default 150.
            icon_mode (bool): Show in icon mode or detail mode. Default False means show in detail mode.
            on_view_mode_chagned_fn (callable): Function called when view mode changed. Default None, also means view mode will never be changed. Function signure:
                void on_view_mode_changed_fn(icon_mode: bool)
            on_value_changed_fn (callable): Function called when slider value changed. Default None. Function signure:
                void on_value_changed_fn(value: int)
            style (dict): Custom style of the control. Default {}} to use default style.
        
    """
    def __init__(self, min: int = 0, max: int = 5, value: int = 2, width: int = 150, icon_mode: bool = False, on_view_mode_changed_fn: callable = None, on_value_changed_fn: callable = None, style: typing.Dict = {}):
        ...
    def _build_ui(self):
        ...
    def _get_view_mode_button_style_type_name(self) -> str:
        ...
    def _on_change_view_mode(self):
        ...
    def _on_value_changed(self, model: omni.ui._ui.SimpleIntModel):
        ...
    def destroy(self):
        ...
    def set_on_hovered_fn(self, on_hovered_fn: typing.Callable[[bool], NoneType]) -> None:
        """
        
                Set callback function when hovered state changed.
                
        """
    @property
    def model(self) -> omni.ui._ui.AbstractValueModel:
        ...
