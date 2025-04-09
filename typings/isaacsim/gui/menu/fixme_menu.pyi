from __future__ import annotations
import omni as omni
from omni.kit.menu.utils.builder_utils import LayoutSourceSearch
from omni.kit.menu.utils.builder_utils import MenuAlignment
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.layout import MenuLayout
from omni import ui
__all__ = ['FixmeMenuExtension', 'LayoutSourceSearch', 'MenuAlignment', 'MenuItemDescription', 'MenuLayout', 'omni', 'ui']
class FixmeMenuExtension:
    class MenuDelegate(omni.ui._ui.MenuDelegate):
        def build_item(self, item: omni.ui._ui.MenuHelper):
            ...
        def get_menu_alignment(self):
            ...
    def __del__(self):
        ...
    def __init__(self, ext_id):
        ...
