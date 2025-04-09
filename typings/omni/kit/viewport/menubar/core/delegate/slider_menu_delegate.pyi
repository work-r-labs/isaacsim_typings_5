from __future__ import annotations
import omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate
from omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate import AbstractWidgetMenuDelegate
from omni import ui
import omni.ui._ui
__all__: list = ['SliderMenuDelegate']
class SliderMenuDelegate(omni.kit.viewport.menubar.core.delegate.abstract_widget_menu_delegate.AbstractWidgetMenuDelegate):
    """
    A menu delegate that creates slider within a viewport menubar.
    """
    def _SliderMenuDelegate__on_checkbox_changed(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def _SliderMenuDelegate__on_slider_changed(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def __del__(self):
        ...
    def __init__(self, model: typing.Optional[omni.ui._ui.AbstractValueModel] = None, min: typing.Union[float, int, NoneType] = None, max: typing.Union[float, int, NoneType] = None, tooltip: typing.Optional[str] = None, width: int = 300, slider_class: typing.Union[omni.ui._ui.FloatSlider, omni.ui._ui.IntSlider] = omni.ui._ui.FloatSlider, show_checkbox_if_min: bool = False, default_value_on: typing.Union[float, int, NoneType] = None, enabled: bool = True, reserve_status: bool = False, has_reset: bool = False, step: typing.Union[float, int, NoneType] = None):
        """
        
                Constructor.
        
                kwargs:
                    model (Optional[ui.AbstractValueModel]): Slider data model, defaults to None.
                    min (Union[float, int, None]): Slider min value, defaults to None.
                    max (Union[float, int, None]): Slider max value, defaults to None.
                    tooltip (Optional[str]): Delegate tooltip, defaults to None.
                    width (int): Slider width, in pixels, defaults to 270. Deprecated.
                    slider_class (Union[ui.FloatSlider, ui.IntSlider]): Slider class, defaults to ui.FloatSlider.
                    show_checkbox_if_min (bool): Show checkbox instead of slider if value equals min, defaults to False.
                    default_value_on (Union[float, int, None]): When checkbox is ON, value to display in slider, defaults to None.
                    enabled (bool): Delegate enabled state, defaults to True.
                    reserve_status (bool): Show additional space before widgets, defaults to False. Used to align with other menu items which have status icon.
                    has_reset (bool): Show reset button, defaults to False.
                    step (Union[float, int, None]): Slider step value defaults to None means use slider default.
                
        """
    def build_widget(self, item: omni.ui._ui.MenuHelper) -> None:
        """
        
                Build a label and a slider.
        
                Args:
                    item (ui.MenuHelper): Menu item.
                
        """
    def calculate_step(self, min: float, max: float, slider: omni.ui._ui.Widget) -> float:
        """
        
                Calculate step by min/max.
        
                Args:
                    min (fl0at): Min value.
                    max (float): Max value.
                    slider (ui.Widget): Slider widget.
                
        """
    def destroy(self) -> None:
        """
        Release resources.
        """
    def set_range(self, min: float, max: float) -> None:
        """
        
                Set slider value range.
        
                Args:
                    min (fl0at): Min value.
                    max (float): Max value.
                
        """
    @property
    def max(self) -> typing.Union[float, int]:
        """
        Slider max value
        """
    @max.setter
    def max(self, value: typing.Union[float, int]) -> None:
        ...
    @property
    def min(self) -> typing.Union[float, int]:
        """
        Slider min value
        """
    @min.setter
    def min(self, value: typing.Union[float, int]) -> None:
        ...
