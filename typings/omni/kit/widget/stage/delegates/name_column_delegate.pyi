from __future__ import annotations
import asyncio as asyncio
import enum
from enum import Enum
from functools import partial
import math as math
import omni.kit.widget.stage.abstract_stage_column_delegate
from omni.kit.widget.stage.abstract_stage_column_delegate import AbstractStageColumnDelegate
import omni.kit.widget.stage.stage_item
from omni.kit.widget.stage.stage_item import StageItem
from omni.kit.widget.stage.stage_model import StageItemSortPolicy
from omni.kit.widget.stage.stage_model import StageModel
from omni import ui
import typing
__all__: list = ['NameColumnDelegate']
class NameColumnDelegate(omni.kit.widget.stage.abstract_stage_column_delegate.AbstractStageColumnDelegate):
    """
    The column delegate that represents the type column
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    sort_policy = ...
    def _NameColumnDelegate__build_rename_field(self, item: omni.kit.widget.stage.stage_item.StageItem, name_labels, parent_stack):
        ...
    def _NameColumnDelegate__draw_all_icons(self, item: omni.kit.widget.stage.stage_item.StageItem, item_is_native, is_highlighted):
        ...
    def _NameColumnDelegate__get_all_icons_to_draw(self, item: omni.kit.widget.stage.stage_item.StageItem, item_is_native):
        ...
    def _NameColumnDelegate__initialize_policy_from_model(self):
        ...
    def _NameColumnDelegate__on_name_label_clicked(self, x, y, b, m):
        ...
    def _NameColumnDelegate__on_policy_changed(self):
        ...
    def _NameColumnDelegate__update_label_from_policy(self):
        ...
    def __init__(self):
        ...
    def build_header(self, **kwargs):
        """
        Build the header
        """
    def build_widget(self, _, **kwargs):
        ...
    def build_widget_sync(self, _, **kwargs):
        """
        Build the type widget
        """
    def destroy(self):
        ...
    def get_type_icon(self, node_type):
        """
        Convert USD Type to icon file name
        """
    def on_header_hovered(self, hovered):
        ...
    def on_stage_items_destroyed(self, items: typing.List[omni.kit.widget.stage.stage_item.StageItem]):
        ...
    def rename_item(self, item: omni.kit.widget.stage.stage_item.StageItem):
        ...
    def set_highlighting(self, enable: bool = None, text: str = None):
        """
        
                Specify if the widgets should consider highlighting. Also set the text that should be highlighted in flat mode.
                
        """
    @property
    def initial_width(self):
        """
        The width of the column
        """
    @property
    def minimum_width(self):
        ...
    @property
    def order(self):
        ...
    @property
    def sortable(self):
        ...
class NameColumnSortPolicy(enum.Enum):
    """
    An enumeration.
    """
    A_TO_Z: typing.ClassVar[NameColumnSortPolicy]  # value = <NameColumnSortPolicy.A_TO_Z: 2>
    NEW_TO_OLD: typing.ClassVar[NameColumnSortPolicy]  # value = <NameColumnSortPolicy.NEW_TO_OLD: 0>
    OLD_TO_NEW: typing.ClassVar[NameColumnSortPolicy]  # value = <NameColumnSortPolicy.OLD_TO_NEW: 1>
    Z_TO_A: typing.ClassVar[NameColumnSortPolicy]  # value = <NameColumnSortPolicy.Z_TO_A: 3>
def split_selection(text, selection):
    """
    
        Split given text to substrings to draw selected text. Result starts with unselected text.
        Example: "helloworld" "o" -> ["hell", "o", "w", "o", "rld"]
        Example: "helloworld" "helloworld" -> ["", "helloworld"]
        
    """
COLOR_LIVE_GREEN: int = 4278237291
COLOR_LIVE_SEL: int = 4278253678
COLOR_RELOAD_ORANGE: int = 4278225100
COLOR_RELOAD_SEL: int = 4278233855
WIDGET_STYLES: dict = {'TreeView.Image::object_icon_grey': {'color': 2164260863}, 'TreeView.Item::object_name_grey': {'color': 4283255618}, 'TreeView.Item::object_name_missing': {'color': 4285494015}, 'TreeView.Item::object_name_missing:hovered': {'color': 4285494015}, 'TreeView.Item::object_name_missing:selected': {'color': 4285494015}, 'TreeView.Item.Outdated': {'color': 4278225100}, 'TreeView.Item.Outdated:hovered': {'color': 4278233855}, 'TreeView.Item.Outdated:selected': {'color': 4278233855}, 'TreeView.Item.Live': {'color': 4278237291}, 'TreeView.Item.Live:hovered': {'color': 4278253678}, 'TreeView.Item.Live:selected': {'color': 4278253678}, 'TreeView.Image::not_active': {'color': 4294967295}}
