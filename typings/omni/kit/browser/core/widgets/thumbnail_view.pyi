from __future__ import annotations
import carb as carb
import omni.kit.browser.core.models.browser_item
from omni.kit.browser.core.models.browser_item import DetailItem
import omni.kit.browser.core.models.browser_model
from omni.kit.browser.core.models.browser_model import AbstractBrowserModel
import omni.kit.browser.core.widgets.detail_delegate
from omni.kit.browser.core.widgets.detail_delegate import DetailDelegate
from omni import ui
import omni.ui._ui
__all__ = ['AbstractBrowserModel', 'DetailDelegate', 'DetailItem', 'KEYBOARD_MODIFIER_FLAG_CONTROL', 'KEYBOARD_MODIFIER_FLAG_SHIFT', 'ThumbnailView', 'carb', 'ui']
class ThumbnailView(omni.ui._ui.VGrid):
    """
    
        GridView to show thumbnails of details or categories.
    
        Keyword Args:
            delegate (DetailDelegate): delegate object to represent detail item
            thumbnail_size (int): width of thumbnail, in pixel. Default 128.
            thumbnail_aspect (float): Aspect ratio of thumbnail. Default 1.0 (width / height).
            extra_filter_fn (callable): Extra filter function called to filter items. Return True to show item otherwise hide.
                Default None. Function signure: bool extra_filter_fn(item: DetailItem)
            thumbnail_padding_width (int): padding width between thumbnails, default 1
            thumbnail_padding_height (int): padding height between thumbnails, default 1
            multiple_drag (bool): True to allow drag multiple items. Default False.
    
        Properties:
            selection (List[DetailItem]): selected detail items. Readonly.
            thumbnail_size (int): size of thumbnail, in pixel. Read and write.
        
    """
    model: omni.kit.browser.core.models.browser_model.AbstractBrowserModel
    selection: typing.List[omni.kit.browser.core.models.browser_item.DetailItem]
    def __init__(self, model, delegate: omni.kit.browser.core.widgets.detail_delegate.DetailDelegate = None, thumbnail_size: int = 128, thumbnail_aspect: float = 1, extra_filter_fn: callable = None, thumbnail_padding_width: int = 1, thumbnail_padding_height: int = 1, multiple_drag: bool = False):
        ...
    def _add_selection(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        ...
    def _build_detail_frame(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        ...
    def _build_detail_item(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        ...
    def _build_ui(self) -> None:
        ...
    def _clear_selections(self) -> None:
        ...
    def _is_item_visible(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> bool:
        ...
    def _model_item_changed(self, model: omni.ui._ui.AbstractItemModel, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        ...
    def _on_click(self, flag: int, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        ...
    def _on_mouse_pressed(self, btn: int, flag: int, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        ...
    def _on_right_click(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> None:
        ...
    def _remove_selection(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> bool:
        ...
    def clear(self) -> None:
        """
        Clear all items and selections
        """
    def destroy(self):
        ...
    def filter(self, filter_words: typing.Optional[typing.List[str]]) -> None:
        """
        
                Filter detail items.
                Args:
                    filter_words: A string list to filter detail items. None means filtering nothing.
                
        """
    def on_drag(self, item: omni.kit.browser.core.models.browser_item.DetailItem) -> str:
        ...
    def refresh(self):
        """
        
                Refresh details items for visibility.
                
        """
    def set_extra_filter_fn(self, extra_filter_fn: typing.Optional[<built-in function callable>]) -> None:
        ...
    def set_selection_changed_fn(self, on_selection_changed_fn) -> None:
        """
        
                Set function called when selection changed.
                Args:
                    on_selection_changed_fn (callable): Function called when selection changed. Function signure:
                        void on_selection_changed_fn(selection: List[DetailItem])
                
        """
    @property
    def thumbnail_padding_height(self) -> int:
        """
        Padding width between deaiil items
        """
    @thumbnail_padding_height.setter
    def thumbnail_padding_height(self, value: int) -> None:
        ...
    @property
    def thumbnail_padding_width(self) -> int:
        """
        Padding width between deaiil items
        """
    @thumbnail_padding_width.setter
    def thumbnail_padding_width(self, value: int) -> None:
        ...
    @property
    def thumbnail_size(self) -> int:
        """
        Thumbnail size of detail item
        """
    @thumbnail_size.setter
    def thumbnail_size(self, value: int) -> None:
        """
        Thumbnail size of detail item
        """
KEYBOARD_MODIFIER_FLAG_CONTROL: int = 2
KEYBOARD_MODIFIER_FLAG_SHIFT: int = 1
