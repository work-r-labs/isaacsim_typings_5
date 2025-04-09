from __future__ import annotations
import asyncio as asyncio
import omni as omni
from omni.kit.browser.core.models.browser_item import CategoryItem
from omni.kit.browser.core.models.browser_wrapper import ChildrenModelWrapper
from omni.kit.browser.core.models.browser_wrapper import SingleLevelWrapper
from omni.kit.browser.core.widgets.thumbnail_view import ThumbnailView
from omni import ui
__all__ = ['CategoryItem', 'ChildrenModelWrapper', 'OverviewView', 'SingleLevelWrapper', 'ThumbnailView', 'asyncio', 'omni', 'ui']
class OverviewView:
    """
    
        Represent an overview to show categories.
        Args:
            model (ChildrenModelWrapper): Model to show categories.
        
    """
    def __init__(self, model: omni.kit.browser.core.models.browser_wrapper.ChildrenModelWrapper, **kwargs):
        ...
    def _build_custom_header(self, collapsed: bool, title: str):
        ...
    def _build_ui(self):
        ...
    def _on_model_updated(self, model, item):
        ...
    def _on_selection_changed(self, root: omni.kit.browser.core.models.browser_item.CategoryItem, selections: typing.List[omni.kit.browser.core.models.browser_item.CategoryItem]):
        ...
    def center(self, enable: bool):
        ...
    def destroy(self):
        ...
    def filter(self, filter_words: typing.Optional[typing.List[str]]) -> None:
        """
        
                Filter detail items.
                Args:
                    filter_words: A string list to filter detail items. None means filtering nothing.
                
        """
    def set_selection_changed_fn(self, on_selection_changed_fn) -> None:
        """
        
                Set function called when selection changed.
                Args:
                    on_selection_changed_fn (callable): Function called when selection changed. Function signure:
                        void on_selection_changed_fn(root: [CategoryItem], selection: List[DetailItem])
                
        """
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
