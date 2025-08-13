from __future__ import annotations
import omni as omni
from omni.kit.menu.utils.builder_utils import LayoutSourceSearch
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.layout import MenuLayout
from omni.kit.menu.utils.utils import add_menu_items
__all__: list[str] = ['HelpMenuExtension', 'LayoutSourceSearch', 'MenuItemDescription', 'MenuLayout', 'add_menu_items', 'omni', 'resolve_physics_ref_url']
class HelpMenuExtension:
    def __init__(self, ext_id):
        ...
    def open_ref_url(self, url):
        ...
    def shutdown(self):
        ...
def resolve_physics_ref_url():
    ...
