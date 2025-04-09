from __future__ import annotations
import abc as abc
from omni.kit.viewport.menubar.core.delegate.viewport_menu_delegate import ViewportMenuDelegate
from omni import ui
import omni.ui._ui
__all__ = ['SingleRenderMenuItem', 'SingleRenderMenuItemBase', 'ViewportMenuDelegate', 'abc', 'ui']
class SingleRenderMenuItem(SingleRenderMenuItemBase):
    """
    
        A default implementation for a single renderer menu item, with an option to open render settings
        
    """
    def _option_clicked(self):
        """
        
                Open the render settings window when clicking the option icon on the right of this menu item.
                
        """
class SingleRenderMenuItemBase(omni.ui._ui.MenuItem):
    """
    
        A base menu item represent a single renderer
        
    """
    def __init__(self, display_name: str, engine_name: str, hd_engine_renderer: HdEngineRenderer, hd_renderer: HdRenderer, viewport_api: ViewportAPI, enabled: bool, checked: bool, hide_on_click: bool, triggered_fn: typing.Callable, hotkey_text: str = '', show_hotkey_placeholder: bool = False):
        """
        
                A base class for creating custom single renderer menu items.
        
                Args:
                    display_name (str): Menu's text
                    engine_name (str): Renderer engine name
                    hd_engine_renderer (HdEngineRenderer): Renderer engine
                    hd_renderer (HdRenderer): Renderer
                    viewport_api (ViewportAPI): Viewport API
                    enabled (bool): If menu item enabled
                    checked (bool): If menu item checked
                    hide_on_click (bool): If hide menu item when clicked
                    triggered_fn (Callable): Callback when men item clicked
        
                Keyword Args:
                    hotkey_text (str): Hotkey text. By default "" means no hotkey text displayed
                    show_hotkey_placeholder (bool): If show placeholder for hotkey in menu item. Default False
        
                
        """
    def _build_menuitem_widgets(self):
        ...
    def _option_clicked(self):
        """
        
                Function to implement when the option is clicked. Used by RTX Remix
        
                :meta public:
                
        """
    def destroy(self):
        """
        
                Remove custom ui widgets.
                
        """
    def set_checked(self, checked: bool) -> None:
        """
        
                Set menu state to be checked
                
        """
    @property
    def engine_name(self) -> str:
        """
        
                Render engine name binding to this menu item.
                
        """
    @property
    def hd_engine_renderer(self) -> HdEngineRenderer:
        """
        
                Renderer engine binding to this menu item.
                
        """
    @property
    def hd_renderer(self) -> HdRenderer:
        """
        
                Renderer binding to this menu item.
                
        """
    @property
    def viewport_api(self) -> ViewportAPI:
        """
        
                Viewport API binding to this menu item.
                
        """
