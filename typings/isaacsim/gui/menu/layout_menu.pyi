from __future__ import annotations
import omni as omni
from omni.kit.menu.utils.builder_utils import LayoutSourceSearch
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.layout import MenuLayout
__all__: list[str] = ['LayoutMenuExtension', 'LayoutSourceSearch', 'MenuItemDescription', 'MenuLayout', 'omni']
class LayoutMenuExtension:
    def __init__(self, ext_id):
        ...
    def shutdown(self):
        ...
