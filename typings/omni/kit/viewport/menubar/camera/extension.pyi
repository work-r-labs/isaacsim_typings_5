from __future__ import annotations
import omni as omni
from omni.kit.viewport.menubar.camera.camera_menu_container import CameraMenuContainer
from omni.kit.viewport.menubar.camera.commands import register_commands
from omni.kit.viewport.menubar.camera.commands import unregister_commands
from omni.kit.viewport.menubar.camera.menu_item.single_camera_menu_item import SingleCameraMenuItemBase
from omni import ui
__all__: list = ['ViewportCameraMenuBarExtension', 'get_instance']
class ViewportCameraMenuBarExtension(omni.ext._extensions.IExt):
    """
    The main class that manages the camera settings integration into the viewport menu bar
    """
    def __init__(self):
        """
        
                Construct the extension.
                
        """
    def deregister_menu_item(self, create_menu_item_fn: typing.Callable[[ForwardRef('viewport_context'), omni.ui._ui.Menu], NoneType]):
        """
        
                Deregister a custom menu item.
        
                Args:
                    create_menu_item_fn (Callable): Callback function to create custom menu item.
                
        """
    def on_shutdown(self):
        """
        Callback when extesion shutdown
        """
    def on_startup(self, ext_id):
        """
        Callback when extension startup
        """
    def register_menu_item(self, create_menu_item_fn: typing.Callable[[ForwardRef('viewport_context'), omni.ui._ui.Menu], NoneType], order: int = 0):
        """
        
                Register a custom menu item.
        
                Args:
                    create_menu_item_fn (Callable): Callback function to create custom menu item.
                Keyword args:
                    order (int): Position to put custom menu item in popup menu window.
                
        """
    def register_menu_item_type(self, menu_item_type: typing.Callable[..., ForwardRef('SingleCameraMenuItemBase')]):
        """
        
                Register a custom menu type for the default created camera
        
                Args:
                    menu_item_type: callable that will create the menu item
                
        """
def get_instance() -> typing.Optional[omni.kit.viewport.menubar.camera.extension.ViewportCameraMenuBarExtension]:
    """
    
        Retrieves the singleton instance of the viewport camera menu bar extension.
        
    """
_extension_instance: ViewportCameraMenuBarExtension  # value = <omni.kit.viewport.menubar.camera.extension.ViewportCameraMenuBarExtension object>
