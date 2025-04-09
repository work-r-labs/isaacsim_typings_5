from __future__ import annotations
import omni as omni
from omni.kit.menu.utils.builder_utils import LayoutSourceSearch
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.layout import MenuLayout
from omni.kit.menu.utils.utils import add_menu_items
__all__ = ['HelpMenuExtension', 'LayoutSourceSearch', 'MenuItemDescription', 'MenuLayout', 'add_menu_items', 'omni']
class HelpMenuExtension:
    def __del__(self):
        ...
    def __init__(self, ext_id):
        ...
    def open_ref_url(self, url):
        ...
