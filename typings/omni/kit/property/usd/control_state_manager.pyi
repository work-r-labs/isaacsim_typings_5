from __future__ import annotations
import omni as omni
from pxr import Usd
import typing
import weakref as weakref
__all__: list = ['ControlStateHandler', 'ControlStateManager']
class ControlStateHandler:
    def __init__(self, on_refresh_state: typing.Callable, on_build_state: typing.Callable, icon_path: str):
        """
        
                Initializes a new instance of the ControlStateHandler.
        
                Args:
                    on_refresh_state (Callable): function to be called when control state refreshes. Callable should returns a tuple(bool, bool).
                        The first bool decides if the flag of this state should be set. The second bool decides if a force rebuild should be triggered.
                    on_build_state (Callable): function to be called when build control state UI. Callable should returns a tuple(bool, Callable, str).
                        If first bool is True, subsequent states with lower (larger value) priority will be skipped.
                        Second Callable is the action to perform when click on the icon.
                        Third str is tooltip when hovering over icon.
                    icon_path (str): path to an SVG file to show next to attribute when this state is True.
                
        """
class ControlStateManager:
    _instance: typing.ClassVar[ControlStateManager]  # value = <omni.kit.property.usd.control_state_manager.ControlStateManager object>
    @classmethod
    def get_instance(cls):
        """
        Get current instance for ControlStateManager.
        """
    def __del__(self):
        ...
    def __init__(self, icon_path):
        """
        Initializes a new instance of the ControlStateManager.
        
                Args:
                    icon_path: Path for icons.
        """
    def _add_entry(self, flag: int, priority: float, entry: ControlStateHandler):
        ...
    def _register_builtin_handlers(self):
        ...
    def _register_connected(self):
        ...
    def _register_connected_error(self):
        ...
    def _register_keyed(self):
        ...
    def _register_locked(self):
        ...
    def _register_mixed(self):
        ...
    def _register_not_default(self):
        ...
    def _register_readonly(self):
        ...
    def _register_sampled(self):
        ...
    def build_control_state(self, control_state, **kwargs):
        """
        Gets control state values for UI.
        """
    def destory(self):
        """
        Cleans up control states.
        """
    def register_control_state(self, on_refresh_state: typing.Callable, on_build_state: typing.Callable, icon_path: str, priority: float = 0.0) -> int:
        """
        Registers a new control states.
        
                Args:
                    on_refresh_state (Callable): function to be called when control state refreshes. Callable should returns a tuple(bool, bool).
                        The first bool decides if the flag of this state should be set. The second bool decides if a force rebuild should be triggered.
                    on_build_state (Callable): function to be called when build control state UI. Callable should returns a tuple(bool, Callable, str).
                        If first bool is True, subsequent states with lower (larger value) priority will be skipped.
                        Second Callable is the action to perform when click on the icon.
                        Third str is tooltip when hovering over icon.
                    icon_path (str): path to an SVG file to show next to attribute when this state is True.
                    priority (float): priority override.
                
        """
    def unregister_control_state(self, flag):
        """
        Unregisters a existing control state.
        """
    def update_control_state(self, usd_model_base):
        """
        Updates control state.
        """
