"""

Base Model classes for the filebrowser entity.
"""
from __future__ import annotations
import carb as carb
from functools import partial
from omni.kit.widget.filebrowser.clipboard import is_path_cut
import omni.kit.widget.filebrowser.model
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni import ui
import omni.ui._ui
import os as os
import pathlib
__all__: list = ['FileBrowserItemCard']
class FileBrowserItemCard(omni.ui._ui.Widget):
    """
    
        Widget used by FileBrowserGridView to build the browser item.
    
        Args:
            item (:obj:`FileBrowserItem`): Item to build the widget with.
    
        Keyword Args:
            width (int): width of the widget, defaults to 60.
            height (int): height of the widget, defaults to 60.
            mouse_pressed_fn (Callable): Function called on mouse press. Function signature:
                void mouse_pressed_fn(pane: int, button: int, key_mode: int, item: :obj:`FileBrowserItem`)
            mouse_double_clicked_fn (Callable): Function called on mouse double click. Function signature:
                void mouse_double_clicked_fn(pane: int, button: int, key_mode: int, item: :obj:`FileBrowserItem`)
            mouse_released_fn (Callable): Function called on mouse release. Function signature:
                void mouse_pressed_fn(pane: int, button: int, key_mode: int, item: :obj:`FileBrowserItem`)
            drop_fn (Callable): Function called to handle drag-n-drops. Function signature:
                void drop_fn(dst_item: :obj:`FileBrowserItem`, event: :obj:`ui.WidgetMouseDropEvent`)
            get_thumbnail_fn (Callable): Function called to get the thumbnail from the item. Function signature:
                str badges_provider(item: :obj:`FileBrowserItem`)
            get_badges_fn (Callable): Function called to get badges from the item. Function signature:
                List[str] badges_provider(item: :obj:`FileBrowserItem`)
            custom_thumbnail (str): Thumbnail to override the default one.
            drag_fn (Callable): Function called to handle dragging thumbnails. Function signature:
                void drag_fn(thumbnail: str)
    
        
    """
    def __init__(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, **kwargs):
        ...
    def _build_ui(self):
        ...
    def _draw_thumbnail_async(self, thumbnail: str):
        ...
    def _get_thumbnail(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> str:
        ...
    def _on_drop(self, event: omni.ui._ui.WidgetMouseDropEvent):
        ...
    def apply_cut_style(self):
        """
         Apply cut style to the widget. 
        """
    def destroy(self):
        """
         Destructor 
        """
    def draw_badges(self):
        """
        
                Draw badges if get_badgets_fn is provided in the constructor.
                
        """
    def draw_thumbnail(self, thumbnail: str):
        """
        
                Asynchronously redraw thumbnail with the given file.
        
                Args:
                    thumbnail (str): thumbnail path.
                
        """
    def on_drag(self, thumbnail: typing.Optional[str] = None):
        """
        
                Default drag handler, create a thumbnail at the given path in the current widget container.
        
                Args:
                    thumbnail (str): thumbnail path.
        
                Returns:
                    The current item path.
                
        """
    def refresh_thumbnail_async(self, thumbnail: str):
        """
        
                Asynchronously redraw thumbnail with the given file.
        
                Args:
                    thumbnail (str): thumbnail path.
                
        """
    def remove_cut_style(self):
        """
         Remove cut style from the widget. 
        """
    @property
    def item(self) -> omni.kit.widget.filebrowser.model.FileBrowserItem:
        """
         Return the item associated with the widget. 
        """
    @property
    def selected(self) -> bool:
        """
         Return True when selected. 
        """
    @selected.setter
    def selected(self, value: bool):
        """
         Set selected or not. 
        """
ALERT_ERROR: int = 3
ALERT_WARNING: int = 2
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.filebrowser-2.10.52+d02c707b/icons')
THUMBNAIL_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.widget.filebrowser-2.10.52+d02c707b/data/thumbnails')
UI_STYLES: dict  # value = {'NvidiaLight': {'Rectangle::Splitter': {'background_color': 4292927712, 'margin_width': 2}, 'Rectangle::Splitter:hovered': {'background_color': 4289753147}, 'Rectangle::Splitter:pressed': {'background_color': 4289753147}, 'Splitter': {'background_color': 4292927712, 'margin_width': 2}, 'TreeView': {'background_color': 4283650900, 'background_selected_color': 4285427310, 'secondary_color': 4289506476}, 'TreeView:hovered': {'background_color': 4285427310}, 'TreeView:selected': {'background_color': 4290689966}, 'TreeView.Column': {'background_color': 0, 'color': 4292269782, 'margin': 0}, 'TreeView.Header': {'background_color': 4283650900, 'color': 4292269782, 'border_color': 4285558896, 'border_width': 0.5}, 'TreeView.Header::name': {'margin': 3, 'alignment': <Alignment.LEFT: 2>}, 'TreeView.Header::date': {'margin': 3, 'alignment': <Alignment.CENTER: 72>}, 'TreeView.Header::size': {'margin': 3, 'alignment': <Alignment.RIGHT: 4>}, 'TreeView.Icon:selected': {'color': 4283650900}, 'TreeView.Header.Icon': {'color': 4287268727}, 'TreeView.Icon::default': {'color': 4287268727}, 'TreeView.Icon::file': {'color': 4287268727}, 'TreeView.Item': {'color': 4292269782}, 'TreeView.Item:selected': {'color': 4280952869}, 'TreeView.ScrollingFrame': {'background_color': 4283650900, 'secondary_color': 4292927712}, 'GridView.ScrollingFrame': {'background_color': 4283650900, 'secondary_color': 4292927712}, 'GridView.Grid': {'background_color': 0, 'margin_width': 10}, 'Card': {'background_color': 0, 'margin': 8}, 'Card:hovered': {'background_color': 4285427310, 'border_color': 4282006074, 'border_width': 0}, 'Card:pressed': {'background_color': 4285427310, 'border_color': 4282006074, 'border_width': 0}, 'Card:selected': {'background_color': 4290689966, 'border_color': 4287268727, 'border_width': 0}, 'Card.Image': {'background_color': 4291414473, 'color': 4294967295, 'corner_flag': <CornerFlag.TOP: 3>, 'alignment': <Alignment.CENTER: 72>, 'margin': 8}, 'Card.Badge': {'background_color': 4291414473, 'color': 4294967295}, 'Card.Badge::shadow': {'background_color': 4291414473, 'color': 3712238660}, 'Card.Label': {'background_color': 4291414473, 'color': 4292269782, 'font_size': 12, 'alignment': <Alignment.CENTER_TOP: 24>, 'margin_width': 8, 'margin_height': 2}, 'Card.Label:checked': {'color': 4280492319}, 'ZoomBar': {'background_color': 0, 'border_radius': 2}, 'ZoomBar.Slider': {'draw_mode': <SliderDrawMode.HANDLE: 1>, 'background_color': 4280492319, 'secondary_color': 4288519581, 'color': 0, 'alignment': <Alignment.CENTER: 72>, 'padding': 0, 'margin': 5, 'font_size': 8}, 'ZoomBar.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'ZoomBar.Button.Image': {'color': 4294967295, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'Recycle.Button.Image': {'image_url': 'resources/glyphs/trash.svg', 'background_color': 4283650900, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button:checked': {'background_color': 4282006074}}, 'NvidiaDark': {'Splitter': {'background_color': 0, 'margin_width': 0}, 'Splitter:hovered': {'background_color': 4289753147}, 'Splitter:pressed': {'background_color': 4289753147}, 'TreeView.ScrollingFrame': {'background_color': 4280492319}, 'TreeView': {'background_color': 4280492319, 'background_selected_color': 1715092026}, 'TreeView:selected': {'background_color': 4287268727}, 'TreeView.Column': {'background_color': 0, 'color': 4289571999, 'margin': 0}, 'TreeView.Header': {'background_color': 4281611314, 'color': 4288585374}, 'TreeView.Icon': {'color': 4294967295, 'padding': 0}, 'TreeView.Icon::Cut': {'background_color': 0, 'color': 2298478591}, 'TreeView.Icon::Cut:selected': {'background_color': 0, 'color': 2298478591}, 'TreeView.Icon::shadow': {'background_color': 0, 'color': 3712238660}, 'TreeView.Icon::expand': {'color': 4294967295}, 'TreeView.Icon:selected': {'color': 4294967295}, 'TreeView.Item': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'TreeView.Item:selected': {'color': 4280952869}, 'TreeView.Item::Cut': {'color': 2292096670, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'TreeView.Item::Cut:selected': {'color': 2284464165}, 'GridView.ScrollingFrame': {'background_color': 4280492319}, 'GridView.Grid': {'background_color': 0, 'margin_width': 10}, 'Card': {'background_color': 0, 'margin': 8}, 'Card:hovered': {'background_color': 4282006074, 'border_color': 4282006074, 'border_width': 2}, 'Card:pressed': {'background_color': 4282006074, 'border_color': 4282532159, 'border_width': 2}, 'Card:selected': {'background_color': 4287268727, 'border_color': 4287268727, 'border_width': 2}, 'Card.Image': {'background_color': 0, 'color': 4294967295, 'corner_flag': <CornerFlag.TOP: 3>, 'alignment': <Alignment.CENTER: 72>, 'margin': 8}, 'Card.Image::Cut': {'color': 2298478591}, 'Card.Badge': {'background_color': 0, 'color': 4294967295}, 'Card.Badge::shadow': {'background_color': 0, 'color': 3712238660}, 'Card.Label': {'background_color': 0, 'color': 4288585374, 'alignment': <Alignment.CENTER_TOP: 24>, 'margin_width': 8, 'margin_height': 2}, 'Card.Label::Cut': {'color': 2292096670}, 'Card.Label:checked': {'color': 4280492319}, 'Card.Label::Cut:checked': {'color': 2284003615}, 'ZoomBar': {'background_color': 4282729797, 'border_radius': 2}, 'ZoomBar.Slider': {'draw_mode': <SliderDrawMode.HANDLE: 1>, 'background_color': 3710066975, 'secondary_color': 4288585374, 'color': 0, 'alignment': <Alignment.CENTER: 72>, 'padding': 0, 'margin': 3}, 'ZoomBar.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'ZoomBar.Button.Image': {'color': 4294967295, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'Recycle.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'Recycle.Button.Image': {'image_url': 'resources/glyphs/trash.svg', 'background_color': 0, 'color': 4288585374, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Image:hovered': {'background_color': 0, 'color': 4294967295}, 'Recycle.Button.Image:checked': {'background_color': 0, 'color': 4294967295}, 'Recycle.Rectangle': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button:checked': {'background_color': 4282006074}, 'RecycleFrame.Button.Label': {'alignment': <Alignment.LEFT: 2>}, 'RecycleView.Frame': {'background_color': 0}}}
