"""

A generic Tree View Widget for File Systems.
"""
from __future__ import annotations
import _asyncio
import asyncio as asyncio
import carb as carb
from carb import log_warn
from datetime import datetime
from functools import partial
from omni.kit.widget.filebrowser.abstract_column_delegate import AbstractColumnDelegate
from omni.kit.widget.filebrowser.abstract_column_delegate import ColumnItem
from omni.kit.widget.filebrowser.clipboard import is_path_cut
from omni.kit.widget.filebrowser.date_format_menu import DatetimeFormatMenu
import omni.kit.widget.filebrowser.model
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFields
from omni.kit.widget.filebrowser.model import FileBrowserModel
import omni.kit.widget.filebrowser.view
from omni.kit.widget.filebrowser.view import FileBrowserView
from omni import ui
import omni.ui._ui
import pathlib
__all__: list = ['AwaitWithFrame', 'FileBrowserTreeView', 'FileBrowserTreeViewDelegate']
class AwaitWithFrame:
    """
    
        A future-like object that runs the given future and makes sure it's
        always in the given frame's scope. It allows for creating widgets
        asynchronously.
        
    """
    def __await__(self):
        ...
    def __init__(self, frame: omni.ui._ui.Frame, future: _asyncio.Future):
        ...
class FileBrowserTreeView(omni.kit.widget.filebrowser.view.FileBrowserView):
    """
    
        UI Widget for display files or folders as icons in a directory in tree view.
    
        Keyword Args:
            root_visible (bool): Set to True to show the root item.
            header_visible (bool): Set to True to show the column headers.
            allow_multi_selection (bool): Optional argument to enable multi selection, defaults to True.
            selection_changed_fn (Callable): Function called when selection changed. Function signature:
                void selection_changed_fn(selections: List[:obj:`FileBrowserItem`])
            mouse_pressed_fn (Callable): Function called on mouse press. Function signature:
                void mouse_pressed_fn(item: :obj:`FileBrowserItem`, x: float, y: float, button: int, key_mode: int)
            mouse_double_clicked_fn (Callable): Function called on mouse double click. Function signature:
                void mouse_double_clicked_fn(item: :obj:`FileBrowserItem`, x: float, y: float,  button: int, key_mode: int)
            treeview_identifier (str): widget identifier for treeview, only used by tests.
        
    """
    def __init__(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel, **kwargs):
        ...
    def _on_column_clicked(self, column_id: int):
        ...
    def _on_column_delegate_changed(self):
        """
        Called by ColumnDelegateRegistry
        """
    def _on_datetime_format_changed(self):
        ...
    def _on_item_changed(self, model, item):
        """
        Called by the model when something is changed
        """
    def _on_model_changed(self, model):
        """
        Called by super when the model is changed
        """
    def _on_mouse_double_clicked(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, x, y, button, key_mod):
        ...
    def _on_mouse_pressed(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, x, y, button, key_mod):
        ...
    def _on_selection_changed(self, selections: [omni.kit.widget.filebrowser.model.FileBrowserItem]):
        ...
    def build_ui(self):
        """
         Build the tree view. 
        """
    def destroy(self):
        """
         Destructor. 
        """
    def is_expanded(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> bool:
        """
         Return True if the item is expanded. 
        """
    def refresh_ui(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem = None):
        """
        
                Throttle the refreshes so that the UI can keep up with multiple refresh directives in succession.
        
                Args:
                    item (:obj:`FileBrowserItem`): The item to refresh.
                
        """
    def scroll_top(self):
        """
        Scroll the widget to top
        """
    def select_and_center(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        """
        
                Select and center the view on the given item.
        
                Args:
                    item (:obj:`FileBrowserItem`): the item to set the new selection to.
                
        """
    def set_expanded(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, expanded: bool, recursive: bool = False):
        """
        
                Set the expansion state of the given item.
        
                Args:
                    item (:obj:`FileBrowserItem`): The item to effect.
                    expanded (bool): True to expand, False to collapse.
                    recursive (bool): Apply state recursively to descendent nodes. Default False.
        
                
        """
    @property
    def selections(self):
        """
         Get selected items in the tree view. 
        """
    @property
    def tree_view(self):
        """
         Get the tree view. 
        """
class FileBrowserTreeViewDelegate(omni.ui._ui.AbstractItemDelegate):
    """
    
        The delegate that manages building browser items under the model as widgets inside the tree view.
    
        Args:
            headers (Tuple[str]): Tuple of columns to show in the tree view.
            theme (str): The theme name to use.
    
        Keyword Args:
            mouse_pressed_fn (Callable): Function called on mouse press. Function signature:
                void mouse_pressed_fn(item: :obj:`FileBrowserItem`, x: float, y: float, button: int, key_mode: int)
            mouse_double_clicked_fn (Callable): Function called on mouse double click. Function signature:
                void mouse_double_clicked_fn(item: :obj:`FileBrowserItem`, x: float, y: float,  button: int, key_mode: int)
            column_clicked_fn (Callable): Function called when column clicked. Function signature:
                void column_clicked_fn(column_id: int)
            datetime_format_changed_fn (Callable): Function called when datetime format changed. Function signature:
                void datetime_format_changed_fn()
            sort_by_column (int): The column index to sort items, defaults to 0.
            sort_ascending (bool): Sort in ascending or otherwise descending order, defaults to ascending.
            builtin_columnt_count (int): Set count of builtin columns.
            icon_provider (object): Set this to override default icons.
        
    """
    def __init__(self, headers: typing.Tuple[str], theme: str, **kwargs):
        ...
    def _draw_item_icon(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, expanded: bool):
        ...
    def _get_style_variant(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        ...
    def _on_date_format_clicked(self):
        ...
    def build_branch(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel, item: omni.kit.widget.filebrowser.model.FileBrowserItem, column_id: int, level: int, expanded: bool):
        """
        
                Create a branch widget that opens or closes subtree.
        
                Args:
                    model (:obj:`FileBrowserModel`): The model to build the branch with.
                    item (:obj:`FileBrowserItem`): The item to build.
                    column_id (int): ID of the column.
                    level (int): level of the item inside the tree.
                    expanded (bool): Set if the item is expanded.
                
        """
    def build_header(self, column_id: int):
        """
        
                Build the given column.
        
                Args:
                    column_id (int): ID of the column.
                
        """
    def build_widget(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel, item: omni.kit.widget.filebrowser.model.FileBrowserItem, column_id: int, level: int, expanded: bool):
        """
        
                Create a widget per item.
        
                Args:
                    model (:obj:`FileBrowserModel`): The model to build the widget with.
                    item (:obj:`FileBrowserItem`): The item to build.
                    column_id (int): ID of the column.
                    level (int): level of the item inside the tree.
                    expanded (bool): Set if the item is expanded.
                
        """
    def clear_futures(self):
        """
        Stop and destroy all working futures
        """
    def destroy(self):
        """
         Destructor. 
        """
    def set_column_delegates(self, delegates: typing.List[omni.kit.widget.filebrowser.abstract_column_delegate.AbstractColumnDelegate]):
        """
        Add custom columns
        """
    @property
    def sort_ascending(self) -> bool:
        """
         Return True when sort in ascending order.
        """
    @sort_ascending.setter
    def sort_ascending(self, value: bool):
        ...
    @property
    def sort_by_column(self) -> int:
        """
         Return the column index used for sorting. 
        """
    @sort_by_column.setter
    def sort_by_column(self, column_id: int):
        ...
ALERT_ERROR: int = 3
ALERT_WARNING: int = 2
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.filebrowser-2.10.52+d02c707b/icons')
UI_STYLES: dict  # value = {'NvidiaLight': {'Rectangle::Splitter': {'background_color': 4292927712, 'margin_width': 2}, 'Rectangle::Splitter:hovered': {'background_color': 4289753147}, 'Rectangle::Splitter:pressed': {'background_color': 4289753147}, 'Splitter': {'background_color': 4292927712, 'margin_width': 2}, 'TreeView': {'background_color': 4283650900, 'background_selected_color': 4285427310, 'secondary_color': 4289506476}, 'TreeView:hovered': {'background_color': 4285427310}, 'TreeView:selected': {'background_color': 4290689966}, 'TreeView.Column': {'background_color': 0, 'color': 4292269782, 'margin': 0}, 'TreeView.Header': {'background_color': 4283650900, 'color': 4292269782, 'border_color': 4285558896, 'border_width': 0.5}, 'TreeView.Header::name': {'margin': 3, 'alignment': <Alignment.LEFT: 2>}, 'TreeView.Header::date': {'margin': 3, 'alignment': <Alignment.CENTER: 72>}, 'TreeView.Header::size': {'margin': 3, 'alignment': <Alignment.RIGHT: 4>}, 'TreeView.Icon:selected': {'color': 4283650900}, 'TreeView.Header.Icon': {'color': 4287268727}, 'TreeView.Icon::default': {'color': 4287268727}, 'TreeView.Icon::file': {'color': 4287268727}, 'TreeView.Item': {'color': 4292269782}, 'TreeView.Item:selected': {'color': 4280952869}, 'TreeView.ScrollingFrame': {'background_color': 4283650900, 'secondary_color': 4292927712}, 'GridView.ScrollingFrame': {'background_color': 4283650900, 'secondary_color': 4292927712}, 'GridView.Grid': {'background_color': 0, 'margin_width': 10}, 'Card': {'background_color': 0, 'margin': 8}, 'Card:hovered': {'background_color': 4285427310, 'border_color': 4282006074, 'border_width': 0}, 'Card:pressed': {'background_color': 4285427310, 'border_color': 4282006074, 'border_width': 0}, 'Card:selected': {'background_color': 4290689966, 'border_color': 4287268727, 'border_width': 0}, 'Card.Image': {'background_color': 4291414473, 'color': 4294967295, 'corner_flag': <CornerFlag.TOP: 3>, 'alignment': <Alignment.CENTER: 72>, 'margin': 8}, 'Card.Badge': {'background_color': 4291414473, 'color': 4294967295}, 'Card.Badge::shadow': {'background_color': 4291414473, 'color': 3712238660}, 'Card.Label': {'background_color': 4291414473, 'color': 4292269782, 'font_size': 12, 'alignment': <Alignment.CENTER_TOP: 24>, 'margin_width': 8, 'margin_height': 2}, 'Card.Label:checked': {'color': 4280492319}, 'ZoomBar': {'background_color': 0, 'border_radius': 2}, 'ZoomBar.Slider': {'draw_mode': <SliderDrawMode.HANDLE: 1>, 'background_color': 4280492319, 'secondary_color': 4288519581, 'color': 0, 'alignment': <Alignment.CENTER: 72>, 'padding': 0, 'margin': 5, 'font_size': 8}, 'ZoomBar.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'ZoomBar.Button.Image': {'color': 4294967295, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'Recycle.Button.Image': {'image_url': 'resources/glyphs/trash.svg', 'background_color': 4283650900, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button:checked': {'background_color': 4282006074}}, 'NvidiaDark': {'Splitter': {'background_color': 0, 'margin_width': 0}, 'Splitter:hovered': {'background_color': 4289753147}, 'Splitter:pressed': {'background_color': 4289753147}, 'TreeView.ScrollingFrame': {'background_color': 4280492319}, 'TreeView': {'background_color': 4280492319, 'background_selected_color': 1715092026}, 'TreeView:selected': {'background_color': 4287268727}, 'TreeView.Column': {'background_color': 0, 'color': 4289571999, 'margin': 0}, 'TreeView.Header': {'background_color': 4281611314, 'color': 4288585374}, 'TreeView.Icon': {'color': 4294967295, 'padding': 0}, 'TreeView.Icon::Cut': {'background_color': 0, 'color': 2298478591}, 'TreeView.Icon::Cut:selected': {'background_color': 0, 'color': 2298478591}, 'TreeView.Icon::shadow': {'background_color': 0, 'color': 3712238660}, 'TreeView.Icon::expand': {'color': 4294967295}, 'TreeView.Icon:selected': {'color': 4294967295}, 'TreeView.Item': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'TreeView.Item:selected': {'color': 4280952869}, 'TreeView.Item::Cut': {'color': 2292096670, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'TreeView.Item::Cut:selected': {'color': 2284464165}, 'GridView.ScrollingFrame': {'background_color': 4280492319}, 'GridView.Grid': {'background_color': 0, 'margin_width': 10}, 'Card': {'background_color': 0, 'margin': 8}, 'Card:hovered': {'background_color': 4282006074, 'border_color': 4282006074, 'border_width': 2}, 'Card:pressed': {'background_color': 4282006074, 'border_color': 4282532159, 'border_width': 2}, 'Card:selected': {'background_color': 4287268727, 'border_color': 4287268727, 'border_width': 2}, 'Card.Image': {'background_color': 0, 'color': 4294967295, 'corner_flag': <CornerFlag.TOP: 3>, 'alignment': <Alignment.CENTER: 72>, 'margin': 8}, 'Card.Image::Cut': {'color': 2298478591}, 'Card.Badge': {'background_color': 0, 'color': 4294967295}, 'Card.Badge::shadow': {'background_color': 0, 'color': 3712238660}, 'Card.Label': {'background_color': 0, 'color': 4288585374, 'alignment': <Alignment.CENTER_TOP: 24>, 'margin_width': 8, 'margin_height': 2}, 'Card.Label::Cut': {'color': 2292096670}, 'Card.Label:checked': {'color': 4280492319}, 'Card.Label::Cut:checked': {'color': 2284003615}, 'ZoomBar': {'background_color': 4282729797, 'border_radius': 2}, 'ZoomBar.Slider': {'draw_mode': <SliderDrawMode.HANDLE: 1>, 'background_color': 3710066975, 'secondary_color': 4288585374, 'color': 0, 'alignment': <Alignment.CENTER: 72>, 'padding': 0, 'margin': 3}, 'ZoomBar.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'ZoomBar.Button.Image': {'color': 4294967295, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'Recycle.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'Recycle.Button.Image': {'image_url': 'resources/glyphs/trash.svg', 'background_color': 0, 'color': 4288585374, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Image:hovered': {'background_color': 0, 'color': 4294967295}, 'Recycle.Button.Image:checked': {'background_color': 0, 'color': 4294967295}, 'Recycle.Rectangle': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button:checked': {'background_color': 4282006074}, 'RecycleFrame.Button.Label': {'alignment': <Alignment.LEFT: 2>}, 'RecycleView.Frame': {'background_color': 0}}}
