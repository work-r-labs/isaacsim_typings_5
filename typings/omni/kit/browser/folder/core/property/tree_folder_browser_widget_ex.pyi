from __future__ import annotations
import asyncio as asyncio
import carb as carb
import math as math
import omni as omni
from omni.kit.browser.folder.core.models.folder_browser_item import FileDetailItem
from omni.kit.browser.folder.core.property.browser_property_delegate import BrowserPropertyDelegate
from omni.kit.browser.folder.core.property.browser_property_toolbar import BrowserPropertyToolBar
from omni.kit.browser.folder.core.property.browser_property_view import BrowserPropertyView
from omni.kit.browser.folder.core.widgets.tree_folder_browser_widget import TreeFolderBrowserWidget
from omni import ui
import typing
__all__ = ['BrowserPropertyDelegate', 'BrowserPropertyToolBar', 'BrowserPropertyView', 'FileDetailItem', 'Layout', 'PROPERTY_STYLES', 'TreeFolderBrowserWidget', 'TreeFolderBrowserWidgetEx', 'asyncio', 'carb', 'math', 'omni', 'ui']
class Layout:
    H_DEFAULT_TOOLKITS_WIDTH: typing.ClassVar[int] = 450
    H_MIN_PROPERTY_WIDTH: typing.ClassVar[int] = 75
    H_MIN_VIEW_WIDTH: typing.ClassVar[int] = 200
    V_DEFAULT_TOOLKITS_HEIGHT: typing.ClassVar[int] = 280
    V_MAX_WINDOW_WIDTH: typing.ClassVar[int] = 400
    V_MIN_PROPERTY_HEIGHT: typing.ClassVar[int] = 20
    V_MIN_VIEW_HEIGHT: typing.ClassVar[int] = 156
    V_SEARCH_BAR_WIDTH: typing.ClassVar[omni.ui._ui.Pixel]  # value = 400.000000px
class TreeFolderBrowserWidgetEx(omni.kit.browser.folder.core.widgets.tree_folder_browser_widget.TreeFolderBrowserWidget):
    """
    
        Folder browser widget with property view.
        
    """
    def _TreeFolderBrowserWidgetEx__update_search_bar_width(self, vertical: bool):
        ...
    def __init__(self, *args, property_delegates: typing.List[omni.kit.browser.folder.core.property.browser_property_delegate.BrowserPropertyDelegate] = list(), **kwargs):
        ...
    def _build_browser_widgets(self):
        ...
    def _build_search_toolbar(self):
        ...
    def _has_space_for_property(self) -> bool:
        ...
    def _on_detail_selection_changed(self, selections: typing.List[omni.kit.browser.folder.core.models.folder_browser_item.FileDetailItem]) -> None:
        ...
    def _on_height_changed(self, height) -> None:
        ...
    def _on_size_changed(self) -> None:
        ...
    def _on_width_changed(self, width) -> None:
        ...
    def _splitter_offset_x_changed(self, offset_x: omni.ui._ui.Length) -> None:
        ...
    def _splitter_offset_y_changed(self, offset_y: omni.ui._ui.Length) -> None:
        ...
    def _switch_layout(self, vertical: bool) -> None:
        ...
    def _toggle_property_view(self) -> None:
        ...
    def _update_layout_async(self) -> None:
        ...
    def build_property_view(self) -> omni.kit.browser.folder.core.property.browser_property_view.BrowserPropertyView:
        """
        
                Build property view.
                
        """
    def build_widgets(self) -> None:
        """
        
                Build widgets with property view and additional tool bar with button to show/hide property view.
                
        """
PROPERTY_STYLES: dict = {'PropertyToolBar.Button': {'background_color': 0, 'padding': 3, 'margin': 0}, 'PropertyToolBar.Button:selected': {'background_color': 'shade:4280492319;light=4283650900'}, 'Splitter': {'background_color': 0, 'margin_width': 0}, 'Splitter:hovered': {'background_color': 4289753147}, 'Splitter:pressed': {'background_color': 4289753147}}
