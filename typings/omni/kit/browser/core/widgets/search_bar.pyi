from __future__ import annotations
import omni.kit.browser.core.widgets.browser_widget
from omni.kit.browser.core.widgets.browser_widget import BrowserWidget
from omni.kit.widget.searchfield.searchfield import SearchField
from omni import ui
import omni.ui._ui
__all__ = ['BrowserSearchBar', 'BrowserWidget', 'OptionMenuDescription', 'OptionsMenu', 'SearchField', 'UI_STYLES', 'ui']
class BrowserSearchBar:
    """
    
        Represent a search bar for browser widget.
        Keyword args:
            enable_navigation_visibility (bool): True to show navigation butoon, False to hide. Default True.
            options_menu (Optional[OptionsMenu]): Options menu displayed when option button clicked. If None, no option button displayed.
                Default is standard options menu.
            style (Dict): Extra ui style for search bar. Default is empty.
            subscribe_edit_changed (bool): Default True to search when input changed. False only search when input ended.
        
    """
    def __init__(self, enable_navigation_visibility: bool = True, options_menu: typing.Optional[omni.kit.browser.core.widgets.search_bar.OptionsMenu] = ..., style = {}, subscribe_edit_changed = True):
        ...
    def _build_ui(self):
        ...
    def _on_search(self, search_words: typing.Optional[typing.List[str]]) -> None:
        ...
    def _trigger_options_menu(self) -> None:
        ...
    def _trigger_show_navigation(self) -> None:
        ...
    def add_on_search_fn(self, on_search_fn: callable) -> None:
        """
        
                Add extra function called when searching.
                Args:
                    on_search_fn (callable): Function called when searching. Function signure:
                        void on_search_fn(Optional[List[str]])
                
        """
    def bind_browser_widget(self, browser_widget: omni.kit.browser.core.widgets.browser_widget.BrowserWidget) -> None:
        """
        
                Bind browser widget used for search bar.
                Browser widget is created after search bar, so need to bind it later.
                Args:
                    browser_widget (): Browser widget used for search bar.
                
        """
    def clear_search(self):
        ...
    def destroy(self) -> None:
        """
        
                Clean up
                
        """
    def remove_on_search_fn(self, on_search_fn: callable) -> bool:
        """
        
                Remove extra function called when searching.
                Args:
                    on_search_fn (callable): Function called when searching.
                
        """
    def set_navigation_clicked_fn(self, on_clicked_fn: typing.Optional[<built-in function callable>]):
        """
        
                Change click callback for navigation button.
                Args:
                    on_clicked_fn (Optional[callable]): Function called when naviagation button clicked. None to set to default callback.
                        Otherwise change to new callback. Function signure: void on_clicked_fn()
                
        """
    @property
    def navigation_button(self) -> omni.ui._ui.Button:
        ...
    @property
    def width(self) -> omni.ui._ui.Length:
        """
         Width of search bar
        """
    @width.setter
    def width(self, value: omni.ui._ui.Length) -> None:
        ...
class OptionMenuDescription:
    """
    
        Represent a menu item in options menu.
        Args:
            name (str): Name of menu item. If "" means a seperator.
            clicked_fn (callable): Function called when menu item clicked. Defualt None. Function signure:
                void clicked_fn()
            enabled_fn (callable): Function called to check menu item enabled or not before show. Default None means already enabled.
                Function signure: bool enabled_fn()
            enabled_fn (callable): Function called to show menu item or not. Default None means always show.
                Function signure: bool visible_fn()
            get_text_fn (callable): Function called to show menu item text. Default None to always use name.
                Function signure: str get_text_fn()
        
    """
    def __init__(self, name: str, clicked_fn: callable = None, enabled_fn: callable = None, visible_fn: callable = None, get_text_fn: callable = None):
        ...
class OptionsMenu:
    """
    
        Represent the options menu, which shows when clicking the options button on search bar.
        User could add own menu items by append_menu_item.
        
    """
    def __init__(self):
        ...
    def _is_remove_collection_enabled(self) -> None:
        ...
    def _on_add_collection(self) -> None:
        """
        
                Function called when "Add Collection" menu item in options menu clicked
                
        """
    def _on_remove_collection(self) -> None:
        ...
    def append_menu_item(self, desc: OptionMenuDescription) -> None:
        """
        
                Append a menu item to options menu.
                
        """
    def bind_browser_widget(self, browser_widget: omni.kit.browser.core.widgets.browser_widget.BrowserWidget) -> None:
        """
        
                Bind browser widget used for search bar.
                Browser widget is created later, so need to bind it later.
                Args:
                    browser_widget (): Browser widget used for search bar.
                
        """
    def destroy(self) -> None:
        ...
    def set_add_collection_fn(self, on_add_collection_fn: callable) -> None:
        """
        
                Set function called when menu item "Add Collection" clicked.
                Args:
                    on_add_collection_fn (callable): Function called when menu item "Add Collection" clicked. Function signure:
                        void on_add_collection_fn()
                
        """
    def show(self) -> None:
        """
        
                Show options menu.
                
        """
UI_STYLES: dict  # value = {'CollectionList': {'background_color': 'shade:4280492319;light=4283650900', 'selected_color': 'shade:4283189827;light=4282927176', 'color': 'shade:4288782753;light=4292927712', 'border_radius': 1}, 'TreeView': {'background_color': 0, 'background_selected_color': 4285427310}, 'TreeView:selected': {'background_color': 0, 'secondary_color': 0}, 'TreeView.Frame': {'background_color': 'shade:4280492319;light=4283650900', 'secondary_color': 'shade:4286611584;light=4288585374', 'border_radius': 0, 'scrollbar_size': 10}, 'TreeView.Branch.Line': {'color': 'shade:4284177243', 'background_color': 'shade:4284177243', 'margin': 0}, 'TreeView.Item': {'color': 'shade:4289045925', 'border_width': 1.5, 'border_color': 'shade:4289045925'}, 'TreeView.Item:selected': {'color': 'shade:4289045925'}, 'TreeView.Item.Name': {'background_color': 0, 'color': 'shade:4288782753;light=4292927712'}, 'TreeView.Item.Name:selected': {'color': 'shade:4294952756;light=4291137818'}, 'TreeView.Item.Count': {'background_color': 0, 'color': 'shade:4283453264;light=4288782753'}, 'TreeView.Item.Count:selected': {'color': 'shade:4288782753;light=4292927712'}, 'TreeView.Mark': {'color': 0, 'border_width': 4}, 'TreeView.Mark:selected': {'color': 'shade:4294952756;light=4291137818', 'border_width': 4}, 'GridView.Frame': {'background_color': 'shade:4280492319;light=4283650900', 'secondary_color': 'shade:4286611584;light=4288585374', 'border_radius': 0, 'scrollbar_size': 10}, 'GridView.Grid': {'background_color': 0}, 'GridView.Item': {'background_color': 0, 'color': 'shade:4288782753;light=4292927712'}, 'GridView.Image': {'border_width': 0}, 'GridView.Image:selected': {'border_width': 2, 'border_color': 'shade:4294952756;light=4291137818', 'border_radius': 3.0}, 'GridView.Image.Placeholder': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.browser.core-2.3.11/icons/cloud_download.svg', 'color': 'shade:4289243304'}, 'CollapsableFrame': {'background_color': 0, 'secondary_color': 0, 'padding': 0, 'margin': 0}, 'Overview.Frame': {'background_color': 0}, 'Overview.Header.Arrow': {'background_color': 4287795858}, 'Overview.Header.Label': {'color': 4287795858}, 'Overview.Header.Line': {'color': 4285558896}, 'SearchBar.Button': {'background_color': 0, 'padding': 3, 'margin': 0, 'stack_direction': <Direction.LEFT_TO_RIGHT: 0>}, 'SearchBar.Button:hovered': {'background_color': 4282006074}, 'SearchBar.Button:pressed': {'background_color': 'shade:4280492319;light=4283650900'}, 'SearchBar.Button:selected': {'background_color': 'shade:4280492319;light=4283650900'}, 'SearchBar.Button.Image::navigation': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.browser.core-2.3.11/icons/navtree.svg', 'color': 'shade:4289243304'}, 'SearchBar.Button.Image::options': {'image_url': '/home/chris/isaacsim/extscache/omni.kit.browser.core-2.3.11/icons/options.svg', 'color': 'shade:4289243304'}, 'SearchBar.Button.Label': {'color': 4289506476}, 'Splitter': {'background_color': 0, 'margin_width': 0}, 'Splitter:hovered': {'background_color': 4289753147}, 'Splitter:pressed': {'background_color': 4289753147}}
