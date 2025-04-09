"""

A generic GridView Widget for File Systems.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
from carb import events
from carb import log_warn
from functools import partial
import omni as omni
from omni.kit.widget.filebrowser.card import FileBrowserItemCard
from omni.kit.widget.filebrowser.clipboard import is_path_cut
from omni.kit.widget.filebrowser.model import FileBrowserItem
from omni.kit.widget.filebrowser.model import FileBrowserModel
from omni.kit.widget.filebrowser.model import FileBrowserUdimItem
from omni.kit.widget.filebrowser.thumbnails import find_thumbnails_for_files_async
from omni.kit.widget.filebrowser.view import FileBrowserView
from omni import ui
__all__: list = ['FileBrowserGridView', 'FileBrowserGridViewDelegate']
class FileBrowserGridView(omni.kit.widget.filebrowser.view.FileBrowserView):
    """
    
        UI Widget for display files or folders as icons in a directory in grid view.
    
        Keyword Args:
            allow_multi_selection (bool): Optional argument to enable multi selection, defaults to True.
            selection_changed_fn (Callable): Function called when selection changed. Function signature:
                void selection_changed_fn(selections: List[:obj:`FileBrowserItem`])
        
    """
    selections = ...
    def __init__(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel, **kwargs):
        ...
    def _on_item_changed(self, model, _):
        ...
    def _on_model_changed(self, model):
        """
        Called by super when the model is changed
        """
    def _on_selection_changed(self, selections: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]):
        ...
    def build_ui(self, restore_selections: typing.Optional[typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]] = None):
        """
        
                Build the UI of the grid view.
        
                Keyword Args:
                    restore_selections (List[:obj:`FileBrowserItem`]): List of file browser items to restore selection to.
                
        """
    def destroy(self):
        """
        Destructor.
        """
    def refresh_ui(self, item: typing.Optional[omni.kit.widget.filebrowser.model.FileBrowserItem] = None, selections: typing.Optional[typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]] = None):
        """
        
                Throttle the refreshes so that the UI can keep up with multiple refresh directives in succession.
        
                Keyword Args:
                    item (:obj:`FileBrowserItem`): Unused argument, kept for compatibility.
                    selection (List[:obj:`FileBrowserItem`]): List of file browser items to set the new selection to.
                
        """
    def scale_view(self, scale: float):
        """
        
                Change the scale of items inside the grid view.
                Args:
                    scale (float): the new scale to set.
                
        """
    def scroll_top(self):
        """
        Scroll the widget to top
        """
    def select_and_center(self, item: omni.kit.widget.filebrowser.model.FileBrowserItem, callback: typing.Optional[typing.Callable[[omni.kit.widget.filebrowser.model.FileBrowserItem], NoneType]] = None):
        """
        
                Select and center the view on the given item.
        
                Args:
                    item (:obj:`FileBrowserItem`): the item to set the new selection to.
                    callback (Callable): optional callback to call after setting the selection. Function signature:
                        void(item: :obj:`FileBrowserItem`)
                
        """
class FileBrowserGridViewDelegate:
    """
    
        The delegate that manages building browser items under the model as widgets inside the grid view.
    
        Args:
            widget (:obj: `ui.Frame`): The frame for the delegate to build widgets under.
            theme (str): The theme name to use.
    
        Keyword Args:
            mouse_pressed_fn (Callable): Function called on mouse press. Function signature:
                void mouse_pressed_fn(button: int, key_mode: int, item: :obj:`FileBrowserItem`, x: float=0, y: float=0)
            mouse_double_clicked_fn (Callable): Function called on mouse double click. Function signature:
                void mouse_double_clicked_fn(button: int, key_mode: int, item: :obj:`FileBrowserItem`, x: float=0, y: float=0)
            selection_changed_fn (Callable): Function called when selection changed. Function signature:
                void selection_changed_fn(selections: list[:obj:`FileBrowserItem`])
            drop_fn (Callable): Function called to handle drag-n-drops. Function signature:
                void drop_fn(dst_item: :obj:`FileBrowserItem`, src_path: str)
            thumbnail_provider (Callable): This callback returns the path to the item's thumbnail. If not specified,
                then a default thumbnail is used. Signature: str thumbnail_provider(item: :obj:`FileBrowserItem`).
            badges_provider (Callable): This callback provides the list of badges to layer atop the thumbnail
                in the grid view. Callback signature: List[str] badges_provider(item: :obj:`FileBrowserItem`)
            treeview_identifier (str): widget identifier for treeview, only used by tests.
            testing (bool): When enabled, forces items to immediately be built and made available.
        
    """
    def __init__(self, widget: omni.ui._ui.Frame, theme: str, **kwargs):
        ...
    def _on_drag(self, card: omni.kit.widget.filebrowser.card.FileBrowserItemCard, thumbnail: str):
        ...
    def _on_mouse_double_clicked(self, card: omni.kit.widget.filebrowser.card.FileBrowserItemCard, x, y, b, key_mod):
        ...
    def _on_mouse_pressed(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel, card: omni.kit.widget.filebrowser.card.FileBrowserItemCard, x, y, b, key_mod):
        ...
    def _on_mouse_released(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel, card: omni.kit.widget.filebrowser.card.FileBrowserItemCard, x, y, b, key_mod):
        ...
    def add_selection(self, card: omni.kit.widget.filebrowser.card.FileBrowserItemCard):
        """
        
                Add a new card to selection.
        
                Args:
                    card (:obj:`FileBrowserItemCard`): Item widget to add.
                
        """
    def build_card(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel, item: omni.kit.widget.filebrowser.model.FileBrowserItem) -> omni.kit.widget.filebrowser.card.FileBrowserItemCard:
        """
        
                Create a widget per item.
        
                Args:
                    model (:obj:`FileBrowserModel`): model to build the item with.
                    item (:obj:`FileBrowserItem`): the item to build the widget.
                
        """
    def build_grid(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel):
        """
        
                Build browser items under the model.
        
                Args:
                    model (:obj:`FileBrowserModel`): Model containing items to build.
                
        """
    def center_selection_async(self, selection: omni.kit.widget.filebrowser.model.FileBrowserItem, scroll_frame: typing.Optional[omni.ui._ui.Frame] = None, scroll_ratio = 0.0, refresh_interval = 2, callback: typing.Optional[typing.Callable[[omni.kit.widget.filebrowser.model.FileBrowserItem], NoneType]] = None):
        """
        
                Center the given item and add it to the selection.
        
                Args:
                    selection (:obj:`FileBrowserItem`): Item to center on.
                    scroll_frame (:obj:`ui.Frame`): Optional argument frame to scroll to the item's new position.
                    scroll_ratio (float): Optional argument ratio to scroll to the item's new position using item index ratio.
                
        """
    def clear_selections(self):
        """
         Clear current selection. 
        """
    def destroy(self):
        """
         Destructor. 
        """
    def extend_selections(self, cards: typing.List[omni.kit.widget.filebrowser.card.FileBrowserItemCard]):
        """
        
                Extend current selection.
        
                Args:
                    cards (List[:obj:`FileBrowserItemCard`]): List of item widgets to extend.
                
        """
    def refresh_thumbnails_async(self, urls: str):
        """
        
                Re-generate the thumbnails with given URLs.
        
                Args:
                    urls (List[str]): thumbnail URLs to update.
                
        """
    def remove_selection(self, card: omni.kit.widget.filebrowser.card.FileBrowserItemCard):
        """
        
                Remove a new card from the selection.
        
                Args:
                    card (:obj:`FileBrowserItemCard`): Item widget to remove.
                
        """
    def update_cards_on_thumbnails_generated(self, event: carb.events._events.IEvent):
        """
        
                When new thumbnails are generated, re-renders associated cards.
        
                Args:
                    events ( :obj:`IEvent`): event containing the thumbnail URLs to update.
                
        """
    def update_grid(self, model: omni.kit.widget.filebrowser.model.FileBrowserModel):
        """
        
                Generate a grid of cards and renders them with custom thumbnails.
        
                Args:
                    model (:obj:`FileBrowserModel`): Model containing items to update.
                
        """
    @property
    def scale(self) -> float:
        """
        
                Get the scale of items.
                
        """
    @scale.setter
    def scale(self, scale: float):
        ...
    @property
    def selections(self) -> typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]:
        """
        
                Get the current selection.
                
        """
    @selections.setter
    def selections(self, selections: typing.List[omni.kit.widget.filebrowser.model.FileBrowserItem]):
        ...
KEYBOARD_MODIFIER_FLAG_CONTROL: int = 2
KEYBOARD_MODIFIER_FLAG_SHIFT: int = 1
THUMBNAILS_GENERATED_EVENT: int = 4677668926123661862
UI_STYLES: dict  # value = {'NvidiaLight': {'Rectangle::Splitter': {'background_color': 4292927712, 'margin_width': 2}, 'Rectangle::Splitter:hovered': {'background_color': 4289753147}, 'Rectangle::Splitter:pressed': {'background_color': 4289753147}, 'Splitter': {'background_color': 4292927712, 'margin_width': 2}, 'TreeView': {'background_color': 4283650900, 'background_selected_color': 4285427310, 'secondary_color': 4289506476}, 'TreeView:hovered': {'background_color': 4285427310}, 'TreeView:selected': {'background_color': 4290689966}, 'TreeView.Column': {'background_color': 0, 'color': 4292269782, 'margin': 0}, 'TreeView.Header': {'background_color': 4283650900, 'color': 4292269782, 'border_color': 4285558896, 'border_width': 0.5}, 'TreeView.Header::name': {'margin': 3, 'alignment': <Alignment.LEFT: 2>}, 'TreeView.Header::date': {'margin': 3, 'alignment': <Alignment.CENTER: 72>}, 'TreeView.Header::size': {'margin': 3, 'alignment': <Alignment.RIGHT: 4>}, 'TreeView.Icon:selected': {'color': 4283650900}, 'TreeView.Header.Icon': {'color': 4287268727}, 'TreeView.Icon::default': {'color': 4287268727}, 'TreeView.Icon::file': {'color': 4287268727}, 'TreeView.Item': {'color': 4292269782}, 'TreeView.Item:selected': {'color': 4280952869}, 'TreeView.ScrollingFrame': {'background_color': 4283650900, 'secondary_color': 4292927712}, 'GridView.ScrollingFrame': {'background_color': 4283650900, 'secondary_color': 4292927712}, 'GridView.Grid': {'background_color': 0, 'margin_width': 10}, 'Card': {'background_color': 0, 'margin': 8}, 'Card:hovered': {'background_color': 4285427310, 'border_color': 4282006074, 'border_width': 0}, 'Card:pressed': {'background_color': 4285427310, 'border_color': 4282006074, 'border_width': 0}, 'Card:selected': {'background_color': 4290689966, 'border_color': 4287268727, 'border_width': 0}, 'Card.Image': {'background_color': 4291414473, 'color': 4294967295, 'corner_flag': <CornerFlag.TOP: 3>, 'alignment': <Alignment.CENTER: 72>, 'margin': 8}, 'Card.Badge': {'background_color': 4291414473, 'color': 4294967295}, 'Card.Badge::shadow': {'background_color': 4291414473, 'color': 3712238660}, 'Card.Label': {'background_color': 4291414473, 'color': 4292269782, 'font_size': 12, 'alignment': <Alignment.CENTER_TOP: 24>, 'margin_width': 8, 'margin_height': 2}, 'Card.Label:checked': {'color': 4280492319}, 'ZoomBar': {'background_color': 0, 'border_radius': 2}, 'ZoomBar.Slider': {'draw_mode': <SliderDrawMode.HANDLE: 1>, 'background_color': 4280492319, 'secondary_color': 4288519581, 'color': 0, 'alignment': <Alignment.CENTER: 72>, 'padding': 0, 'margin': 5, 'font_size': 8}, 'ZoomBar.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'ZoomBar.Button.Image': {'color': 4294967295, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'Recycle.Button.Image': {'image_url': 'resources/glyphs/trash.svg', 'background_color': 4283650900, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button:checked': {'background_color': 4282006074}}, 'NvidiaDark': {'Splitter': {'background_color': 0, 'margin_width': 0}, 'Splitter:hovered': {'background_color': 4289753147}, 'Splitter:pressed': {'background_color': 4289753147}, 'TreeView.ScrollingFrame': {'background_color': 4280492319}, 'TreeView': {'background_color': 4280492319, 'background_selected_color': 1715092026}, 'TreeView:selected': {'background_color': 4287268727}, 'TreeView.Column': {'background_color': 0, 'color': 4289571999, 'margin': 0}, 'TreeView.Header': {'background_color': 4281611314, 'color': 4288585374}, 'TreeView.Icon': {'color': 4294967295, 'padding': 0}, 'TreeView.Icon::Cut': {'background_color': 0, 'color': 2298478591}, 'TreeView.Icon::Cut:selected': {'background_color': 0, 'color': 2298478591}, 'TreeView.Icon::shadow': {'background_color': 0, 'color': 3712238660}, 'TreeView.Icon::expand': {'color': 4294967295}, 'TreeView.Icon:selected': {'color': 4294967295}, 'TreeView.Item': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'TreeView.Item:selected': {'color': 4280952869}, 'TreeView.Item::Cut': {'color': 2292096670, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'TreeView.Item::Cut:selected': {'color': 2284464165}, 'GridView.ScrollingFrame': {'background_color': 4280492319}, 'GridView.Grid': {'background_color': 0, 'margin_width': 10}, 'Card': {'background_color': 0, 'margin': 8}, 'Card:hovered': {'background_color': 4282006074, 'border_color': 4282006074, 'border_width': 2}, 'Card:pressed': {'background_color': 4282006074, 'border_color': 4282532159, 'border_width': 2}, 'Card:selected': {'background_color': 4287268727, 'border_color': 4287268727, 'border_width': 2}, 'Card.Image': {'background_color': 0, 'color': 4294967295, 'corner_flag': <CornerFlag.TOP: 3>, 'alignment': <Alignment.CENTER: 72>, 'margin': 8}, 'Card.Image::Cut': {'color': 2298478591}, 'Card.Badge': {'background_color': 0, 'color': 4294967295}, 'Card.Badge::shadow': {'background_color': 0, 'color': 3712238660}, 'Card.Label': {'background_color': 0, 'color': 4288585374, 'alignment': <Alignment.CENTER_TOP: 24>, 'margin_width': 8, 'margin_height': 2}, 'Card.Label::Cut': {'color': 2292096670}, 'Card.Label:checked': {'color': 4280492319}, 'Card.Label::Cut:checked': {'color': 2284003615}, 'ZoomBar': {'background_color': 4282729797, 'border_radius': 2}, 'ZoomBar.Slider': {'draw_mode': <SliderDrawMode.HANDLE: 1>, 'background_color': 3710066975, 'secondary_color': 4288585374, 'color': 0, 'alignment': <Alignment.CENTER: 72>, 'padding': 0, 'margin': 3}, 'ZoomBar.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'ZoomBar.Button.Image': {'color': 4294967295, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'Recycle.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'Recycle.Button.Image': {'image_url': 'resources/glyphs/trash.svg', 'background_color': 0, 'color': 4288585374, 'alignment': <Alignment.CENTER: 72>}, 'Recycle.Button.Image:hovered': {'background_color': 0, 'color': 4294967295}, 'Recycle.Button.Image:checked': {'background_color': 0, 'color': 4294967295}, 'Recycle.Rectangle': {'background_color': 4280492319, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button': {'background_color': 0, 'margin': 0, 'padding': 0}, 'RecycleFrame.Button:hovered': {'background_color': 4282006074}, 'RecycleFrame.Button:checked': {'background_color': 4282006074}, 'RecycleFrame.Button.Label': {'alignment': <Alignment.LEFT: 2>}, 'RecycleView.Frame': {'background_color': 0}}}
