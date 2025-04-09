from __future__ import annotations
import omni as omni
from omni.kit.viewport.menubar.render.menu_item.single_render_menu_item import SingleRenderMenuItem
from omni.kit.viewport.menubar.render.menu_item.single_render_menu_item import SingleRenderMenuItemBase
from omni.kit.viewport.menubar.render.renderer_menu_container import RendererMenuContainer
__all__: list = ['ViewportRenderMenuBarExtension', 'get_instance', 'SingleRenderMenuItemBase', 'SingleRenderMenuItem']
class ViewportRenderMenuBarExtension(omni.ext._extensions.IExt):
    """
    The main class that manages the render settings integration into the viewport menu bar
    """
    @staticmethod
    def _ViewportRenderMenuBarExtension__auto_enable_renderers():
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def register_menu_item_type(self, menu_item_type: typing.Callable[..., ForwardRef('SingleRenderMenuItemBase')]):
        """
        
                Register a custom menu type for the default created renderer
        
                Args:
                    menu_item_type: callable that will create the menu item
                
        """
def get_instance() -> typing.Optional[omni.kit.viewport.menubar.render.extension.ViewportRenderMenuBarExtension]:
    """
    
        Retrieves the singleton instance of the viewport render menu bar extension.
        
    """
_extension_instance: ViewportRenderMenuBarExtension  # value = <omni.kit.viewport.menubar.render.extension.ViewportRenderMenuBarExtension object>
