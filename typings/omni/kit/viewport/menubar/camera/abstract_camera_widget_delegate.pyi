from __future__ import annotations
import abc as abc
from omni import ui
import pxr.Sdf
from pxr import Sdf
import typing
import weakref as weakref
__all__: list = ['AbstractCameraButtonDelegate', 'AbstractCameraMenuItemDelegate', 'AbstractWidgetDelegate']
class AbstractCameraButtonDelegate(AbstractWidgetDelegate):
    """
    
        Self-register delegate to manage additional widgets in camera button.
        
    """
    _AbstractCameraButtonDelegate__g_registered: typing.ClassVar[list] = list()
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'build_widget', 'on_camera_path_changed', 'on_parent_destroyed'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @classmethod
    def get_instances(cls):
        """
        
                Retrieves all registered camera button delegates.
                
        """
    def __del__(self):
        ...
    def __init__(self):
        """
        Construct delegate and register.
        """
    def destroy(self):
        """
        Release resource and deregister all camera button delegates.
        """
class AbstractCameraMenuItemDelegate(AbstractWidgetDelegate):
    """
    
        Self-register delegate to manage additional widgets in camera menu item.
        
    """
    _AbstractCameraMenuItemDelegate__g_registered: typing.ClassVar[list] = list()
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'build_widget', 'on_camera_path_changed', 'on_parent_destroyed'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @classmethod
    def get_instances(cls):
        """
        
                Retrieves all registered camera menu item delegates.
                
        """
    def __del__(self):
        ...
    def __init__(self):
        """
        Construct delegate and register.
        """
    def destroy(self):
        """
        Release resource and deregister all camera menu item delegates.
        """
class AbstractWidgetDelegate(abc.ABC):
    """
    
        A base class for creating custom widgets in camera button and camera menu item.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'build_widget', 'on_camera_path_changed', 'on_parent_destroyed'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def build_widget(self, parent_id: int, viewport_api: ViewportAPI, camera_path: pxr.Sdf.Path) -> typing.Optional[omni.ui._ui.Widget]:
        """
        
                Builds widget. This must be overridden to provide the layout.
        
                Args:
                    parent_id (int): It's unique id of the camera item, with which you can use to manage the camera widget.
                    viewport_api (ViewportAPI): Viewport interface.
                    camera_path (Sdf.Path): The camera path to build widget for.
                
        """
    def destroy(self):
        """
        Release resources.
        """
    def on_camera_path_changed(self, parent_id: int, camera_path: pxr.Sdf.Path):
        """
        
                Callback when the tracked camera has changed.
        
                Args:
                    parent_id (int): It's unique id of the camera item, with which you can use to manage the camera widget.
                    camera_path (Sdf.Path): The new camera path.
                
        """
    def on_parent_destroyed(self, parent_id: int) -> None:
        """
        
                Called before the destroy of the parent widget to release the bound resources specific to the parent.
        
                Args:
                    parent_id (int): It's unique id of the camera item, with which you can use to manage the camera widget.
                
        """
    @property
    def order(self) -> int:
        """
        
                The order of the widget relative to the right of camera label.
                The lower the order number, the closer the widget to the camera label.
                
        """
