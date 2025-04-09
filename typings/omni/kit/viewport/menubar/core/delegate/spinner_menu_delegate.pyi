from __future__ import annotations
from omni import ui
import omni.ui._ui
import omni.ui.color_utils
__all__: list = ['SpinnerMenuDelegate']
class SpinnerMenuDelegate(omni.ui._ui.MenuDelegate):
    """
    
        A menu delegate that creates a spinner within a viewport menubar.
    
        Use slider instead of spinner if omni.kit.widget.spinner not enabled.
        
    """
    def __del__(self):
        ...
    def __init__(self, model: typing.Optional[omni.ui._ui.AbstractValueModel] = None, tooltip: typing.Optional[str] = None, width: typing.Optional[omni.ui._ui.Length] = None, height: omni.ui._ui.Length = 0, min: typing.Union[float, int, NoneType] = None, max: typing.Union[float, int, NoneType] = None, step: typing.Union[float, int] = 1, enabled: bool = True, text: bool = True, icon_name: typing.Optional[str] = None, icon_width: omni.ui._ui.Length = 30, icon_height: omni.ui._ui.Length = 30, use_in_menubar: bool = False, precision: typing.Optional[int] = 1):
        """
        
                Constructor.
        
                Args:
                    model (Optional[ui.AbstractValueModel]): Spinner data model, defaults to None
                    tooltip (Optional[str]): Spinner tooltip, defaults to None.
                    width (Optional[ui.Length]): Delegate width, defaults to None means ui.Fraction(1).
                    height (ui.Length): Delegate Height, defaults to 0 means auto height.
                    min (Union[float, int, None]): Spinner min value, defaults to None.
                    max (Union[float, int, None]): Spinner max value, defaults to None.
                    step (Union[float, int]): Spinner step value, defaults to 1.
                    enabled (bool): Delegate starts enabled, defaults to True.
                    text (bool): Show text before spinner, defaults to True.
                    icon_name (Optional[str]): Name of additional icon to be displayed before text, defaults to None means no additional icon.
                    icon_width (ui.Length): Width of additional icon. Only available when icon_name is valid, defaults to 30 pixels.
                    icon_height (ui.Length): Height of additional icon. Only available when icon_name is valid, defaults to 30 pixels.
                    use_in_menubar (bool): Show menu item in menu bar, defaults to False.
                    precision (Optional[int]): Data precision, defaults to 1.
                
        """
    def build_item(self, item: omni.ui._ui.MenuItem) -> None:
        """
        
                Build a spinner.
        
                Use slider instead if omni.kit.widget.spinner not enabled.
        
                Args:
                    item (ui.MenuItem): Menu item.
                
        """
    def destroy(self) -> None:
        """
        Release resources.
        """
    @property
    def enabled(self) -> bool:
        """
        Delegate enabled state.
        """
    @enabled.setter
    def enabled(self, value) -> None:
        ...
SPINNER_STYLE: dict  # value = {'Spinner.Field': {'background_color': 0, 'color': 'viewport_menubar_light'}, 'Spinner.Field:disabled': {'color': 'viewport_menubar_medium'}, 'Spinner.Arrow': {'background_color': 'viewport_menubar_light'}, 'Spinner.Arrow:disabled': {'background_color': 'viewport_menubar_medium'}}
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
