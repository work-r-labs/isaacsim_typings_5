from __future__ import annotations
from omni import ui
import omni.ui._ui
import pathlib
__all__ = ['BrowserPropertyToolBar', 'BrowserToolBarBase', 'BrowserToolBarButtonDesc', 'ICON_PATH', 'ui']
class BrowserPropertyToolBar(BrowserToolBarBase):
    """
    
        Represent a tool bar with a button to display a Property widget (window).
        Args:
            on_toggle_property_fn (callable): Function called when show/hide property button clicked. Function signure:
                void on_toggle_property_fn()
        
    """
    def __init__(self, on_toggle_property_fn: callable):
        ...
    def destroy(self):
        ...
    @property
    def btn_property(self) -> omni.ui._ui.Button:
        ...
class BrowserToolBarBase:
    """
    
        Represent a base tool bar for browser.
        Args:
            descs (List[BrowserToolBarButtonDesc]): Default buttons to show on tool bar.
        
    """
    def __init__(self, descs: typing.List[omni.kit.browser.folder.core.property.browser_property_toolbar.BrowserToolBarButtonDesc]):
        ...
    def _build_buttons(self):
        ...
    def append_buttons(self, button_descs: typing.Union[omni.kit.browser.folder.core.property.browser_property_toolbar.BrowserToolBarButtonDesc, typing.List[omni.kit.browser.folder.core.property.browser_property_toolbar.BrowserToolBarButtonDesc]]) -> None:
        """
        
                Append buttons to toolbar.
                Args:
                    button_descs (Union[BrowserToolBarButtonDesc,                 List[BrowserToolBarButtonDesc]]): Desc of buttons to be appended.
                
        """
    def destroy(self) -> None:
        ...
    def get_button(self, desc: BrowserToolBarButtonDesc) -> typing.Optional[omni.ui._ui.Button]:
        """
        
                Get toolbar button by desc. Return None if not found.
                Args:
                    desc (BrowserToolBarButtonDesc): Button description.
                
        """
    @property
    def computed_height(self):
        ...
    @property
    def position_x(self):
        ...
    @property
    def spacer_visible(self) -> bool:
        """
        Visibility of spacers in toolbar
        """
    @spacer_visible.setter
    def spacer_visible(self, visible) -> None:
        ...
    @property
    def visible(self) -> bool:
        """
        
                Toolbar visibility.
                
        """
    @visible.setter
    def visible(self, value) -> None:
        ...
    @property
    def width(self):
        ...
class BrowserToolBarButtonDesc:
    """
    
        Represent a button in browser toolbar
        Args:
            image_url (Optional[str]): Image url of button. None means spacer.
            clicked_fn (callable): Function called when button clicked. Default None. Function signature:
                void clicked_fn()
            tooltips (Optional[str]): Button tooltips. Default None.
        
    """
    def __init__(self, image_url: typing.Optional[str], clicked_fn: callable = None, tooltips: typing.Optional[str] = None):
        ...
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.browser.folder.core-1.10.1/data/icons')
