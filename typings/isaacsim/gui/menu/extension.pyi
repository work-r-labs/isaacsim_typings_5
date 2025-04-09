from __future__ import annotations
import gc as gc
from isaacsim.gui.menu.create_menu import CreateMenuExtension
from isaacsim.gui.menu.edit_menu.edit_menu import EditMenuExtension
from isaacsim.gui.menu.file_menu.file_menu import FileMenuExtension
from isaacsim.gui.menu.fixme_menu import FixmeMenuExtension
from isaacsim.gui.menu.help_menu import HelpMenuExtension
from isaacsim.gui.menu.hooks_menu import HookMenuHandler
from isaacsim.gui.menu.layout_menu import LayoutMenuExtension
from isaacsim.gui.menu.tools_menu import ToolsMenuExtension
from isaacsim.gui.menu.utilities_menu import UtilitiesMenuExtension
from isaacsim.gui.menu.window_menu import WindowMenuExtension
import omni as omni
from omni.kit.menu.utils.builder_utils import MenuItemDescription
from omni.kit.menu.utils.utils import add_menu_items
from omni.kit.menu.utils.utils import remove_menu_items
__all__ = ['CreateMenuExtension', 'EditMenuExtension', 'Extension', 'FileMenuExtension', 'FixmeMenuExtension', 'HelpMenuExtension', 'HookMenuHandler', 'LayoutMenuExtension', 'MenuItemDescription', 'ToolsMenuExtension', 'UtilitiesMenuExtension', 'WindowMenuExtension', 'add_menu_items', 'gc', 'omni', 'remove_menu_items']
class Extension(omni.ext._extensions.IExt):
    def on_shutdown(self):
        ...
    def on_startup(self, ext_id: str):
        ...
