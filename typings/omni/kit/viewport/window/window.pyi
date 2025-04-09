from __future__ import annotations
import carb as carb
import contextlib as contextlib
from omni import ui
import omni.ui._ui
import typing
import weakref as weakref
__all__: list = ['ViewportWindow']
class ViewportWindow(omni.ui._ui.Window):
    _ViewportWindow__APP_WINDOW_HIDE_UI: typing.ClassVar[str] = '/app/window/hideUi'
    _ViewportWindow__DOUBLE_CLICK_COI: typing.ClassVar[str] = '/persistent/app/viewport/coiDoubleClick'
    _ViewportWindow__GAMEPAD_CONTROL: typing.ClassVar[str] = '/persistent/app/omniverse/gamepadCameraControl'
    _ViewportWindow__OBJECT_CENTRIC: typing.ClassVar[str] = '/persistent/app/viewport/objectCentricNavigation'
    _ViewportWindow__g_default_style: typing.ClassVar[dict] = {'ViewportBackgroundColor': {'background_color': 4278190080}, 'ViewportStats::Root': {'margin_width': 5, 'margin_height': 3}, 'ViewportStats::Spacer': {'margin': 18}, 'ViewportStats::Group': {'margin_width': 10, 'margin_height': 5}, 'ViewportStats::Stack': {}, 'ViewportStats::Background': {'background_color': 3425314852, 'border_radius': 5}, 'ViewportStats::Label': {'margin_height': 1.75}, 'ViewportStats::LabelError': {'margin_height': 1.75, 'color': 4278190335}, 'ViewportStats::LabelWarning': {'margin_height': 1.75, 'color': 4278255615}, 'ViewportStats::LabelDisabled': {'margin_height': 1.75, 'color': 4286611584}}
    _ViewportWindow__g_instances: typing.ClassVar[list]  # value = [<weakproxy at 0x709fb3f1c0e0 to ViewportWindow at 0x709fbe3fac50>]
    active_window: typing.ClassVar[weakref.ProxyType]  # value = <weakproxy at 0x709ee4163d30 to ViewportWindow at 0x709fbe3fac50>
    @staticmethod
    def _ViewportWindow__clean_instances(dead, self = None):
        ...
    @staticmethod
    def _ViewportWindow__resolve_window_args(width, height, flags):
        ...
    @staticmethod
    def get_instances(usd_context_name: str | None = ''):
        ...
    @staticmethod
    def set_default_style(style, overwrite: bool = False, usd_context_name: str | None = '', apply: bool = True):
        ...
    def _ViewportWindow__dock_changed(self, is_docked):
        ...
    def _ViewportWindow__external_drop(self, edd, payload):
        ...
    def _ViewportWindow__focused_changed(self, focused: bool):
        ...
    def _ViewportWindow__frame_built(self, *args, **kwargs):
        ...
    def _ViewportWindow__hide_ui(self, *args, **kwargs):
        ...
    def _ViewportWindow__on_minimized(self, event: carb.events._events.IEvent = None, **kwargs):
        ...
    def _ViewportWindow__selected_in_dock_changed(self, is_selected):
        ...
    def _ViewportWindow__set_double_click_coi(self, *args, **kwargs):
        ...
    def _ViewportWindow__set_gamepad_enabled(self, *args, force_off: bool = False, **kwargs):
        ...
    def _ViewportWindow__set_object_centric(self, *args, **kwargs):
        ...
    def __del__(self):
        ...
    def __init__(self, name: str | None = None, usd_context_name: str = '', width: int = None, height: int = None, flags: int = None, style: dict = None, usd_drop_support: bool = True, hydra_engine_options: typing.Optional[dict] = None, **ui_kw_args):
        """
        
                ViewportWindow constructor
        
                Args:
                    name (str): The name of the Window.
                    usd_context_name (str): The name of a UsdContext this ViewportWindow will be viewing.
                    width(int): The width of the Window.
                    height(int): The height of the Window.
                    flags(int): omni.ui.WINDOW flags to use for the Window.
                    style (dict): Optional style overrides to apply to the Window's frame.
                    usd_drop_support (bool): Enable Usd drop support (requires {py:mod}`omni.kit.window.drop_support`)
                    hydra_engine_options (dict, None): Optional dictionary to use in creation of the HydraEngine
                    *args: Additional arguments to pass to omni.ui.Window
                    **kwargs: Additional keyword arguments to pass to omni.ui.Window
                
        """
    def _find_viewport_layer(self, layer_id: str, category: str = None, layers = None):
        ...
    def _post_toast_message(self, message: str, message_id: str = None):
        ...
    def add_external_drag_drop_support(self, callback_fn: typing.Callable = None):
        """
        
                Add a callback for an external drag-drop event onto the ViewportWindow
        
                Args:
                     callback_fn (Callable): Object to be invoked when the item is dragged or dropped over the ViewportWindow
                
        """
    def destroy(self):
        """
        Destroy the ViewportWindow instance
        """
    def get_frame(self, name: str) -> omni.ui._ui.Frame:
        """
        
                Add a unique {py:class}`omni.ui.Frame` into the view hierarchy.
                This will return a newly created {py:class}`omni.ui.Frame` on the first call for a unique name,
                or return a previously created {py:class}`omni.ui.Frame` for the same unique name.
        
                Args:
                    name (str): A unique identifier for the frame.
                Returns:
                    An {py:class}`omni.ui.Frame`.
                
        """
    def remove_external_drag_drop_support(self):
        """
        Disable external drag-drop into the ViewportWindow
        """
    def set_style(self, style):
        """
        
                Set the style for the ViewportWindow
        
                Args:
                     style: The omni.ui style object to apply.
                
        """
    @property
    def name(self):
        """
        Return the name of the ViewportWindow
        """
    @property
    def viewport_api(self):
        """
        Return the active ViewportAPI for the ViewportWindow
        """
    @property
    def viewport_widget(self):
        """
        Return the active omni.kit.widget.viewport.ViewportWidget for the ViewportWindow
        """
    @property
    def visible(self) -> bool:
        """
        This property holds whether the window is visible.
        """
    @visible.setter
    def visible(self, visible: bool):
        ...
