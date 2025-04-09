"""
UI widget for navigating a filesystem.
"""
from __future__ import annotations
from _queue import Empty
import carb as carb
from carb import log_error
from carb import log_warn
from functools import partial
import omni as omni
from omni.kit.widget.filebrowser.clipboard import get_clipboard_items
from omni.kit.widget.filebrowser.clipboard import is_clipboard_cut
from omni.kit.widget.filebrowser.grid_view import FileBrowserGridView
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserItemFactory
from omni.kit.widget.filebrowser.model import FileBrowserModel
from omni.kit.widget.filebrowser.tree_view import FileBrowserTreeView
from omni.kit.widget.filebrowser.zoom_bar import ZoomBar
from omni import ui
import pathlib
__all__: list = ['FileBrowserWidget']
class FileBrowserWidget:
    """
    
        The basic UI widget for navigating a filesystem as a tree or grid view.
        The filesystem can either be from your local machine or the Omniverse Nucleus server.
    
        Args:
            title (str): Widget title. Default None.
    
        Keyword Args:
            layout (int): The overall layout of the window, one of: {LAYOUT_SPLIT_PANES, LAYOUT_SINGLE_PANE_SLIM,
                LAYOUT_SINGLE_PANE_WIDE, LAYOUT_DEFAULT}. Default LAYOUT_SPLIT_PANES.
            splitter_offset (int): Position of vertical splitter bar. Default 300.
            tooltip (bool): Display tooltips when hovering over items. Default False.
            allow_multi_selection (bool): Allow multiple items to be selected at once. Default True.
            mouse_pressed_fn (Callable): Function called on mouse press. Function signature:
                void mouse_pressed_fn(pane: int, button: int, key_mode: int, item: :obj:`FileBrowserItem`, x: float=0, y: float=0)
            mouse_double_clicked_fn (Callable): Function called on mouse double click. Function signature:
                void mouse_double_clicked_fn(pane: int, button: int, key_mode: int, item: :obj:`FileBrowserItem`, x: float=0, y: float=0)
            selection_changed_fn (Callable): Function called when selection changed. Function signature:
                void selection_changed_fn(pane: int, selections: list[:obj:`FileBrowserItem`])
            drop_fn (Callable): Function called to handle drag-n-drops. Function signature:
                void drop_fn(dst_item: :obj:`FileBrowserItem`, src_path: str)
            filter_fn (Callable): This user function should return True if the given tree view item is
                visible, False otherwise. Function signature: bool filter_fn(item: :obj:`FileBrowserItem`)
            show_grid_view (bool): If True, initialize the folder view to display icons. Default False.
            show_recycle_widget (bool): If True, show recycle view in the left bottom corner. Default False.
            grid_view_scale (int): Scales grid view, ranges from 0-5. Default 2.
            on_toggle_grid_view_fn (Callable): Callback after toggle grid view is executed. Default None.
            on_scale_grid_view_fn (Callable): Callback after scale grid view is executed. Default None.
            icon_provider (Callable): This callback provides an icon to replace the default one in the tree
                view. Signature: str icon_provider(item: :obj:`FileBrowserItem`, expanded: bool).
            thumbnail_provider (Callable): This callback returns the path to the item's thumbnail. If not specified,
                then a default thumbnail is used. Signature: str thumbnail_provider(item: :obj:`FileBrowserItem`).
            badges_provider (Callable): This callback provides the list of badges to layer atop the thumbnail
                in the grid view. Callback signature: List[str] badges_provider(item: :obj:`FileBrowserItem`)
            treeview_identifier (str): widget identifier for treeview, only used by tests.
            enable_zoombar (bool): Enables/disables zoombar. Default True.
        
    """
    def __init__(self, title: str, **kwargs):
        ...
    def _auto_refresh_folder(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        ...
    def _build_grid_view(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel) -> omni.kit.widget.filebrowser.grid_view.FileBrowserGridView:
        ...
    def _build_split_panes_view(self) -> omni.kit.widget.filebrowser.tree_view.FileBrowserTreeView:
        ...
    def _build_table_view(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel) -> omni.kit.widget.filebrowser.tree_view.FileBrowserTreeView:
        ...
    def _build_tree_view(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel, header_visible: bool = True, files_visible: bool = True, slim_view: bool = True, selection_changed_fn: typing.Callable = None) -> omni.kit.widget.filebrowser.tree_view.FileBrowserTreeView:
        ...
    def _build_ui(self):
        ...
    def _on_mouse_double_clicked(self, pane: int, button: int, key_mod: int, item: omni.kit.widget.filebrowser.model.FileBrowserItem, x: float = 0, y: float = 0):
        ...
    def _on_mouse_pressed(self, pane: int, button: int, key_mod: int, item: omni.kit.widget.filebrowser.model.FileBrowserItem, x: float = 0, y: float = 0):
        ...
    def _on_selection_changed(self, pane: int, selected: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]):
        ...
    def add_model_as_subtree(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel, parent: omni.kit.widget.filebrowser.model.FileBrowserItem = None):
        """
        
                Add a new model as the subtree of the tree view root model or the given parent item.
        
                Args:
                    model (:obj:`FileBrowserModel`): the model to add.
                    parent (:obj:`FileBrowserItem`): If set, add the model as a child to this item instead of the tree view root model.
                
        """
    def clear_item_alert(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem):
        """
        
                Clear the alert of the given item.
        
                Args:
                    item (:obj:`FileBrowserItem`): Item to clear the alert.
                
        """
    def create_grouping_item(self, name: str, path: str, parent: omni.kit.widget.filebrowser.model.FileBrowserItem = None) -> omni.kit.widget.filebrowser.model.FileBrowserItem:
        """
        
                Create a folder item at the given path and add it as child to the tree view root model or the given parent item.
        
                Args:
                    name (str): name of the item.
                    path (str): path of the item.
                    parent (str): If set, add the item as a child to this item instead of the tree view root model.
                
        """
    def delete_child(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, parent: omni.kit.widget.filebrowser.model.FileBrowserItem = None):
        """
        
                Delete an item from the tree view root model or the given parent item.
        
                Args:
                    model (:obj:`FileBrowserModel`): the item to remove.
                    parent (:obj:`FileBrowserItem`): If set, remove the item from this item instead of the tree view root model.
                
        """
    def delete_child_by_name(self, item_name: str, parent: omni.kit.widget.filebrowser.model.FileBrowserItem = None):
        """
        
                Delete an item from the tree view root model or the given parent item.
        
                Args:
                    item_name (str): the item name to remove.
                    parent (:obj:`FileBrowserItem`): If set, remove the item from this item instead of the tree view root model.
                
        """
    def destroy(self):
        """
        
                Destructor. Called by extension before destroying this object. It doesn't happen automatically.
                Without this hot reloading doesn't work.
        
                
        """
    def get_root(self, pane: int = None) -> omni.kit.widget.filebrowser.model.FileBrowserItem:
        """
         Get the root item of the treeview by pane. 
        """
    def get_selected_item(self, pane: int = 1) -> omni.kit.widget.filebrowser.model.FileBrowserItem:
        """
        
                Return last of selected item from the specified pane.
        
                ARGS:
                    pane (int): One of TREEVIEW_PANE, LISTVIEW_PANE. Returns the union if None is specified.
        
                Returns:
                    `FileBrowserItem` or None
                
        """
    def get_selections(self, pane: int = 1) -> [omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        
                Return list of selected items from the specified pane.
        
                ARGS:
                    pane (int): One of TREEVIEW_PANE, LISTVIEW_PANE. Returns the union if None is specified.
        
                Returns:
                    list[:obj:`FileBrowserItem`]
                
        """
    def hide_notification(self):
        """
        
                Hide the notification frame.
                
        """
    def link_views(self, src_widget: object):
        """
        
                Link this widget to the given widget, i.e. the 2 widgets will therafter display the same
                models but not necessarily share the same view.
        
                Args:
                    src_widget (:obj:`FilePickerWidget`): The source widget.
        
                
        """
    def refresh_ui(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem = None, listview_only: bool = False):
        """
        
                Redraw the subtree rooted at the given item. If item is None, then redraws entire tree.
        
                Args:
                    item (:obj:`FileBrowserItem`): Root of subtree to redraw. Default None, i.e. root.
        
                
        """
    def scale_grid_view(self, scale: float):
        """
         Set the scale of item inside grid view. 
        """
    def select_and_center(self, selection: omni.kit.widget.filebrowser.model.FileBrowserItem, pane: int = 1):
        """
        
                Select and centers the tree view on the given item, expanding the tree if needed.
        
                Args:
                    selection (:obj:`FileBrowserItem`): The selected item.
                    pane (int): One of TREEVIEW_PANE, LISTVIEW_PANE.
        
                
        """
    def set_expanded(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, expanded: bool, recursive: bool = False):
        """
        
                Set the expansion state of the given item.
        
                Args:
                    item (:obj:`FileBrowserItem`): The item to effect.
                    expanded (bool): True to expand, False to collapse.
                    recursive (bool): Apply state recursively to descendent nodes. Default False.
        
                
        """
    def set_item_alert(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, alert_level: int, msg: str):
        """
        
                Set the alert message of the given item.
        
                Args:
                    item (:obj:`FileBrowserItem`): Item to set alert.
                    alert_level (int): level of alert.
                    msg (str): message to alert.
                
        """
    def set_item_error(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, msg: str):
        """
        
                Set the error message of the given item.
        
                Args:
                    item (:obj:`FileBrowserItem`): Item to set alert.
                    alert_level (int): level of alert.
                    msg (str): message to alert.
                
        """
    def set_item_info(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, msg: str):
        """
        
                Set the info message of the given item.
        
                Args:
                    item (:obj:`FileBrowserItem`): Item to set alert.
                    alert_level (int): level of alert.
                    msg (str): message to alert.
                
        """
    def set_item_warning(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, msg: str):
        """
        
                Set the warning message of the given item.
        
                Args:
                    item (:obj:`FileBrowserItem`): Item to set alert.
                    alert_level (int): level of alert.
                    msg (str): message to alert.
                
        """
    def set_selections(self, selections: [omni.kit.widget.filebrowser.model.FileBrowserItem], pane: int = 1):
        """
        
                Selected given items in given pane.
        
                ARGS:
                    selections (list[:obj:`FileBrowserItem`]): list of selections.
                    pane (int): One of TREEVIEW_PANE, LISTVIEW_PANE, or None for both. Default None.
        
                
        """
    def show_model(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel):
        """
        
                Show the given model.
                
        """
    def show_notification(self):
        """
        
                Show the notification frame.
                
        """
    def toggle_grid_view(self, show_grid_view: bool):
        """
         Toggle on/of grid view. 
        """
    @property
    def show_grid_view(self):
        """
         Return True if grid view is visible. 
        """
    @property
    def show_udim_sequence(self):
        """
         Return True if the list model has UDIM sequence visible. 
        """
    @show_udim_sequence.setter
    def show_udim_sequence(self, value: bool):
        ...
ALERT_ERROR: int = 3
ALERT_INFO: int = 1
ALERT_WARNING: int = 2
DATETIME_FORMAT_SETTING: str = '/persistent/app/datetime/format'
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.filebrowser-2.10.52+d02c707b/icons')
LAYOUT_DEFAULT: int = 3
LAYOUT_SINGLE_PANE_LIST: int = 4
LAYOUT_SINGLE_PANE_SLIM: int = 1
LAYOUT_SINGLE_PANE_WIDE: int = 2
LAYOUT_SPLIT_PANES: int = 3
LISTVIEW_PANE: int = 2
SCALE_MAP: dict = {0: 0.25, 1: 0.5, 2: 0.75, 3: 1, 4: 1.5, 5: 2.0}
TREEVIEW_PANE: int = 1
UI_STYLES: dict  # value = {'NvidiaLight': {'Rectangle::Splitter': {'background_color': 4292927712, 'margin_width': 2}, 'Rectangle::Splitter:hovered': {'background_color': 4289753147}, 'Rectangle::Splitter:pressed': {'background_color': 4289753147}, 'Splitter': {'background_color': 4292927712, 'margin_width': 2}, 'TreeView': {'background_color': 4283650900, 'background_selected_color': 4285427310, 'secondary_color': 4289506476}, 'TreeView:hovered': {'background_color': 4285427310}, 'TreeView:selected': {'background_color': 4290689966}, 'TreeView.Column': {'background_color': 0, 'color': 4292269782, 'margin': 0}, 'TreeView.Header': {'background_color': 4283650900, 'color': 4292269782, 'border_color': 4285558896, 'border_width': 0.5}, 'TreeView.Header::name': {'margin': 3, 'alignment': <Alignment.LEFT: 2>}, 'TreeView.Header::date': {'margin': 3, 'alignment': <Alignment.CENTER: 72>}, 'TreeView.Header::size': {'margin': 3, 'alignment': <Alignment.RIGHT: 4>}, 'TreeView.Icon:selected': {'color': 4283650900}, 'TreeView.Header.Icon': {'color': 4287268727}, 'TreeView.Icon::default': {'color': 4287268727}, 'TreeView.Icon::file': {'color': 4287268727}, 'TreeView.Item': {'color': 4292269782}, 'TreeView.Item:selected': {'color': 4280952869}, 'TreeView.ScrollingFrame': {'background_color': 4283650900, 'secondary_color': 4292927712}, 'GridView.ScrollingFrame': {'background_color': 4283650900, 'secondary_color': 4292927712}, 'GridView.Grid': {'background_color': 0, 'margin_width': 10}, 'Card': {'background_color': 0, 'margin': 8}, 'Card:hovered': {'background_color': 4285427310, 'border_color': 4282006074, 'border_width': 0}, 'Card:pressed': {'background_color': 4285427310, 'border_color': 4282006074, 'border_width': 0}, 'Card:selected': {'background_color': 4290689966, 'border_color': 4287268727, 'border_width': 0}, 'Card.Image': {'background_color': 4291414473, 'color': 4294967295, 'corner_flag': <CornerFlag.TOP: 3>, 'alignment': <Alignment.CENTER: 72>, 'margin': 8}, 'Card.Badge': {'background_color': 4291414473, 'color': 4294967295}, 'Card.Badge::shadow': {'background_color': 4291414473, 'color': 3712238660}, 'Card.Label': {'background_color': 4291414473, 'color': 4292269782, 'font_size': 12, 'alignment': <Alignment.CENTER_TOP: 24>, 'margin_width': 8, 'margin_height': 2}, 'Card.Label:checked': {'color': 4280492319}, 'ZoomBar': {'background_color': 0, 'border_radius': 2}, 'ZoomBar.Slider': {'draw_mode': <SliderDrawMode.HANDLE: 1>, 'background_color': 4280492319, 'secondary_color': 4288519581, 'color': 0, 'alignment': <Alignment.CENTER: 72>, 'padding': 0, 'margin': 5, 'font_size': 8}, 'ZoomBar.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'ZoomBar.Button.Image': {'color': 4294967295, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'Recycle.Button.Image': {'image_url': 'resources/glyphs/trash.svg', 'background_color': 4283650900, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button:checked': {'background_color': 4282006074}}, 'NvidiaDark': {'Splitter': {'background_color': 0, 'margin_width': 0}, 'Splitter:hovered': {'background_color': 4289753147}, 'Splitter:pressed': {'background_color': 4289753147}, 'TreeView.ScrollingFrame': {'background_color': 4280492319}, 'TreeView': {'background_color': 4280492319, 'background_selected_color': 1715092026}, 'TreeView:selected': {'background_color': 4287268727}, 'TreeView.Column': {'background_color': 0, 'color': 4289571999, 'margin': 0}, 'TreeView.Header': {'background_color': 4281611314, 'color': 4288585374}, 'TreeView.Icon': {'color': 4294967295, 'padding': 0}, 'TreeView.Icon::Cut': {'background_color': 0, 'color': 2298478591}, 'TreeView.Icon::Cut:selected': {'background_color': 0, 'color': 2298478591}, 'TreeView.Icon::shadow': {'background_color': 0, 'color': 3712238660}, 'TreeView.Icon::expand': {'color': 4294967295}, 'TreeView.Icon:selected': {'color': 4294967295}, 'TreeView.Item': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'TreeView.Item:selected': {'color': 4280952869}, 'TreeView.Item::Cut': {'color': 2292096670, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'TreeView.Item::Cut:selected': {'color': 2284464165}, 'GridView.ScrollingFrame': {'background_color': 4280492319}, 'GridView.Grid': {'background_color': 0, 'margin_width': 10}, 'Card': {'background_color': 0, 'margin': 8}, 'Card:hovered': {'background_color': 4282006074, 'border_color': 4282006074, 'border_width': 2}, 'Card:pressed': {'background_color': 4282006074, 'border_color': 4282532159, 'border_width': 2}, 'Card:selected': {'background_color': 4287268727, 'border_color': 4287268727, 'border_width': 2}, 'Card.Image': {'background_color': 0, 'color': 4294967295, 'corner_flag': <CornerFlag.TOP: 3>, 'alignment': <Alignment.CENTER: 72>, 'margin': 8}, 'Card.Image::Cut': {'color': 2298478591}, 'Card.Badge': {'background_color': 0, 'color': 4294967295}, 'Card.Badge::shadow': {'background_color': 0, 'color': 3712238660}, 'Card.Label': {'background_color': 0, 'color': 4288585374, 'alignment': <Alignment.CENTER_TOP: 24>, 'margin_width': 8, 'margin_height': 2}, 'Card.Label::Cut': {'color': 2292096670}, 'Card.Label:checked': {'color': 4280492319}, 'Card.Label::Cut:checked': {'color': 2284003615}, 'ZoomBar': {'background_color': 4282729797, 'border_radius': 2}, 'ZoomBar.Slider': {'draw_mode': <SliderDrawMode.HANDLE: 1>, 'background_color': 3710066975, 'secondary_color': 4288585374, 'color': 0, 'alignment': <Alignment.CENTER: 72>, 'padding': 0, 'margin': 3}, 'ZoomBar.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'ZoomBar.Button.Image': {'color': 4294967295, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'Recycle.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'Recycle.Button.Image': {'image_url': 'resources/glyphs/trash.svg', 'background_color': 0, 'color': 4288585374, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Image:hovered': {'background_color': 0, 'color': 4294967295}, 'Recycle.Button.Image:checked': {'background_color': 0, 'color': 4294967295}, 'Recycle.Rectangle': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button:checked': {'background_color': 4282006074}, 'RecycleFrame.Button.Label': {'alignment': <Alignment.LEFT: 2>}, 'RecycleView.Frame': {'background_color': 0}}}
