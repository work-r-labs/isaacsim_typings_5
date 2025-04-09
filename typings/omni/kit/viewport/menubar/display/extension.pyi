from __future__ import annotations
import omni as omni
from omni.kit.viewport.menubar.core.model.category_model import BaseCategoryItem
from omni.kit.viewport.menubar.display.display_menu_container import DisplayMenuContainer
__all__: list = ['ViewportDisplayMenuBarExtension', 'get_instance']
class ViewportDisplayMenuBarExtension(omni.ext._extensions.IExt):
    """
    The Entry Point for the Display Settings in Viewport Menu Bar
    """
    def deregister_custom_category_item(self, category: str, item: omni.kit.viewport.menubar.core.model.category_model.BaseCategoryItem):
        """
        
                Deregister custom display setting in category.
        
                Args:
                    category (str): Category to remove menu item. Can be an existing category e.g. "Heads Up Display" or a new one.
                    item (item: BaseCategoryItem): Item to remove.
                
        """
    def deregister_custom_setting(self, text: str):
        """
        
                Deregister custom display setting.
        
                Args:
                    text (str): Text shown in menu item.
                
        """
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id):
        ...
    def register_custom_category_item(self, category: str, item: omni.kit.viewport.menubar.core.model.category_model.BaseCategoryItem, section: str = 'default'):
        """
        
                Register custom display setting in category.
        
                Args:
                    category (str): Category to add menu item. Can be an existing category e.g. "Heads Up Display" or a new one.
                    item (item: BaseCategoryItem): Item to append.
                    section (str): Optional section to organize category, default no section.
                
        """
    def register_custom_setting(self, text: str, setting_path: str):
        """
        
                Register custom display setting.
        
                Args:
                    text (str): Text shown in menu item.
                    setting_path (str): Setting path for custom display setting (bool value).
                
        """
def get_instance() -> typing.Optional[omni.kit.viewport.menubar.display.extension.ViewportDisplayMenuBarExtension]:
    """
    
        Get extension instance.
        
    """
DEFAULT_SECTION: str = 'default'
_extension_instance: ViewportDisplayMenuBarExtension  # value = <omni.kit.viewport.menubar.display.extension.ViewportDisplayMenuBarExtension object>
