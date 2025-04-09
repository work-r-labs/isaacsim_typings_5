from __future__ import annotations
import abc as abc
import carb as carb
import collections
from collections import defaultdict
from omni.kit.viewport.menubar.core.model.setting_model import SettingModelWithDefaultPath
from omni import ui
import omni.ui._ui
import typing
import weakref as weakref
__all__: list = ['AbstractViewportMenuItem', 'AbstractViewportMenubarItem', 'ViewportMenuModel', 'register', 'deregister', 'get_items', 'get_item', 'push_to_scope', 'pop_from_scope', 'destroy']
class AbstractViewportMenuItem(omni.ui._ui.AbstractItem):
    """
    Represent a viewport menu item.
    """
    def __init__(self, name: str = '', visible_setting_path: typing.Optional[str] = None, order_setting_path: typing.Optional[str] = None, expand_setting_path: typing.Optional[str] = None):
        """
        
                Construct a viewport menu item.
        
                Keyword Args:
                    name (str): Menu item name, defaults to "" to use self.
                    visible_setting_path (Optional[str]): Setting path for visibility, defaults to None.
                    order_setting_path (Optional[str]): Setting path for order, defaults to None. Order < 0 means in left of menubar. Order > 0 means in right of menubar.
                    expand_setting_path (Optional[str]): Setting path for expand state, defaults to None.
                
        """
    def can_contract(self, factory_args: dict) -> bool:
        """
        
                If menu item could contract to smaller size, defaults to False.
        
                Args:
                    factory_args (dict): Argument related to viewport for this menu bar item.
                
        """
    def contract(self, factory_args: dict) -> None:
        """
        
                Contract menu item to smaller size.
        
                Args:
                    factory_args (dict): Argument related to viewport for this menu bar item.
                
        """
    def destroy(self) -> None:
        """
        Remove from viewport menubar registry
        """
    def expand(self, factory_args: dict) -> None:
        """
        
                Expand display of menu item.
        
                Args:
                    factory_args (dict): Argument related to viewport for this menu bar item.
                
        """
    def get_display_status(self, factory_args: dict) -> MenuDisplayStatus:
        """
        
                Menu item display status.
        
                Args:
                    factory_args (dict): Argument related to viewport for this menu bar item.
                
        """
    def get_require_size(self, factory_args: dict, expand: bool = False) -> float:
        """
        
                Required size for menu item.
        
                Args:
                    factory_args (dict): Argument related to viewport for this menu bar item.
        
                keyword Args:
                    expand (bool): True for menu item to expand. False for menu item in current display status.
                
        """
    @property
    def name(self):
        """
        Item name
        """
    @property
    def parent(self):
        """
        Parent item
        """
class AbstractViewportMenubarItem(AbstractViewportMenuItem):
    """
    
        Represent a menubar.
        
    """
    def build_fn(self, menu_items: typing.List[omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem], factory_args: typing.Dict) -> None:
        """
        
                Build menubar.
        
                Args:
                    menu_items (List[AbstractViewportMenuItem]): Menu items to display on the menubar
                    factory_args (dict): Argument related to viewport for this menu bar item.
                
        """
class MenuDisplayStatus:
    """
    Menu item display status
    """
    EXPAND: typing.ClassVar[int] = 2
    LABEL: typing.ClassVar[int] = 1
    MAX: typing.ClassVar[int] = 3
    MIN: typing.ClassVar[int] = 0
def deregister(menu_item: AbstractViewportMenuItem):
    """
    Remove item from the storage
    """
def destroy():
    """
    Clear items
    """
def get_item(name: typing.Optional[str] = None) -> AbstractViewportMenuItem:
    """
    Get the items by name
    """
def get_items(parent_name: typing.Optional[str] = None) -> typing.List[omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem]:
    """
    Get the list of items by parent name
    """
def pop_from_scope():
    """
    Called from `__exit__` when using `with` statement.
    """
def push_to_scope(menu_container: AbstractViewportMenuItem):
    """
    
        Called from `__enter__` when using `with` statement. Puts the container
        to the stack so the children know their parents.
        
    """
def register(menu_item: typing.Union[omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenuItem, omni.kit.viewport.menubar.core.viewport_menu_model.AbstractViewportMenubarItem]) -> weakref.ProxyType[AbstractViewportMenuItem]:
    """
    
        Register the item in the storage. It keeps the item, so to destroy it,
        it's necessary to use `deregister` or `destroy`.
    
        It's called in the constructor of `ViewportMenuItem`, so once the item is
        created, it automatically registers here.
    
        Returns the proxy with the parent, so the child stores it and avoids
        circular reference.
        
    """
def singleton(class_):
    """
    A singleton decorator
    """
DEFAULT_MENUBAR_NAME: str = '__DEFAULT__MENUBAR__'
_name_to_menuitem: dict  # value = {'__DEFAULT__MENUBAR__': <omni.kit.viewport.menubar.core.menu_item.viewport_menubar_item.ViewportMenubar object>, '<omni.kit.viewport.menubar.core.menu_item.viewport_menu_spacer.ViewportMenuSpacer object>': <omni.kit.viewport.menubar.core.menu_item.viewport_menu_spacer.ViewportMenuSpacer object>, 'SyntheticData': <omni.syntheticdata.scripts.menu.SynthDataMenuContainer object>, 'Display': <omni.kit.viewport.menubar.display.display_menu_container.DisplayMenuContainer object>, 'Camera': <omni.kit.viewport.menubar.camera.camera_menu_container.CameraMenuContainer object>, 'Lighting': <omni.kit.viewport.menubar.lighting.menu_container.MenuContainer object>, 'Renderer': <omni.kit.viewport.menubar.render.renderer_menu_container.RendererMenuContainer object>, 'Settings': <omni.kit.viewport.menubar.settings.setting_menu_container.SettingMenuContainer object>}
_parentname_to_name: collections.defaultdict  # value = defaultdict(<class 'list'>, {None: ['__DEFAULT__MENUBAR__'], '__DEFAULT__MENUBAR__': ['<omni.kit.viewport.menubar.core.menu_item.viewport_menu_spacer.ViewportMenuSpacer object>', 'SyntheticData', 'Display', 'Camera', 'Lighting', 'Renderer', 'Settings']})
_scope_stack: list = list()
