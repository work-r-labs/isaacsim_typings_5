from __future__ import annotations
import abc as abc
import carb as carb
import omni.kit.viewport.menubar.camera.camera_widget_delegate_manager
from omni.kit.viewport.menubar.camera.camera_widget_delegate_manager import CameraWidgetDelegateManager
from omni.kit.viewport.menubar.camera.utils import get_camera_display
from omni.kit.viewport.menubar.core.delegate.label_menu_delegate import LabelMenuDelegate
from omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate import ViewportMenuDelegate
from omni import ui
import omni.ui._ui
from pxr import Sdf
import pxr.Sdf
__all__ = ['CameraWidgetDelegateManager', 'LabelMenuDelegate', 'NoCameraMenuItem', 'Sdf', 'SingleCameraMenuItem', 'SingleCameraMenuItemBase', 'ViewportMenuDelegate', 'abc', 'carb', 'get_camera_display', 'ui']
class NoCameraMenuItem(omni.ui._ui.MenuItem):
    """
    
        A single menu item represent a no camera in the camera list
        
    """
    def __init__(self):
        ...
class SingleCameraMenuItem(SingleCameraMenuItemBase):
    """
    
        A single menu item represent a single camera in the camera list
        
    """
    def _option_clicked(self):
        ...
class SingleCameraMenuItemBase(omni.ui._ui.MenuItem):
    """
    
        A base class for creating custom single camera menu items.
        
    """
    def _SingleCameraMenuItemBase__build_custom_widgets(self):
        ...
    def _SingleCameraMenuItemBase__get_lock_button_name(self):
        ...
    def _SingleCameraMenuItemBase__toggle_camera_lock(self):
        ...
    def __init__(self, camera_path: pxr.Sdf.Path, viewport_api: ViewportAPI, lock_model: omni.ui._ui.AbstractValueModel, root: omni.ui._ui.Menu, triggered_fn: typing.Callable, widget_delegate_manager: omni.kit.viewport.menubar.camera.camera_widget_delegate_manager.CameraWidgetDelegateManager, hotkey_text: str = '', show_hotkey_placeholder: bool = False):
        """
        
                A base class for creating custom single camera menu items.
        
                Args:
                    camera_path (Sdf.Path): Path to camera.
                    viewport_api (ViewportAPI): Viewport API.
                    lock_model (ui.AbstractValueModel): Value model to indicate if camera locked.
                    root (ui.Menu): Root menu.
                    triggered_fn (Callable): Callback when men item clicked.
                    widget_delegate_manager (CameraWidgetDelegateManager): Manager to custom button/menu item delegates.
        
                Keyword Args:
                    hotkey_text (str): Hotkey text. By default "" means no hotkey text displayed.
                    show_hotkey_placeholder (bool): If show placeholder for hotkey in menu item. Default False.
        
                
        """
    def _build_menuitem_widgets(self):
        """
        Build additional buttons in the camera menu item
        """
    def _on_lock_changed(self, model: omni.ui._ui.AbstractValueModel) -> None:
        ...
    def _option_clicked(self):
        """
        Function to implement when the option is clicked. Used by RTX Remix
        """
    def destroy(self):
        """
        Removes all the callbacks and circular references.
        """
    def set_checked(self, checked: bool) -> None:
        """
        Set menu state to be checked
        """
    @property
    def camera_path(self) -> pxr.Sdf.Path:
        """
        Path to camera
        """
    @property
    def viewport_api(self) -> ViewportAPI:
        """
        Viewport API
        """
