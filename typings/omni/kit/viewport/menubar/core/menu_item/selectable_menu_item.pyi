from __future__ import annotations
from omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate import ViewportMenuDelegate
from omni import ui
import omni.ui._ui
__all__: list = ['SelectableMenuItem']
class SelectableMenuItem(omni.ui._ui.MenuItem):
    """
    A menu item can be selected.
    """
    def __del__(self):
        ...
    def __init__(self, name: str, model: typing.Optional[omni.ui._ui.AbstractValueModel] = None, delegate: typing.Optional[omni.ui._ui.MenuDelegate] = None, hide_on_click: bool = False, toggle: bool = True, triggered_fn: typing.Callable = None, trigger_will_set_model: bool = False, **kwargs):
        """
        
                Constructor.
        
                keyword Args:
                    model (Optional[ui.AbstractValueModel]): Model for selected state, defaults to none.
                    delegate (Optional[ui.MenuDelegate]): Menu item delegate, defaults to None means using ViewportMenuDelegate.
                    hide_on_click (bool): Hide menu when radio menu item clicked, defaults to False.
                    toggle (bool): Whether this item can be toggled to (on/off) or always triggers on, defaults to True
                    triggered_fn (callable): Callback when menu item clicked, defaults to None.
                    trigger_will_set_model (bool): Update selected state model when menu item clicked, defaults to False.
                    For other kwargs, please refer to ui.MenuItem
                
        """
    def _on_triggered(self) -> None:
        ...
    def _on_value_changed(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def destroy(self) -> None:
        """
        Release resources
        """
