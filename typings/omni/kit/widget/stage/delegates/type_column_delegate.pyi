from __future__ import annotations
import enum
from enum import Enum
import omni.kit.widget.stage.abstract_stage_column_delegate
from omni.kit.widget.stage.abstract_stage_column_delegate import AbstractStageColumnDelegate
from omni.kit.widget.stage.stage_item import StageItem
from omni.kit.widget.stage.stage_model import StageItemSortPolicy
from omni.kit.widget.stage.stage_model import StageModel
from omni import ui
import typing
__all__: list = ['TypeColumnDelegate']
class TypeColumnDelegate(omni.kit.widget.stage.abstract_stage_column_delegate.AbstractStageColumnDelegate):
    """
    The column delegate that represents the type column
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def _TypeColumnDelegate__initialize_policy_from_model(self):
        ...
    def _TypeColumnDelegate__on_name_label_clicked(self, x, y, b, m):
        ...
    def _TypeColumnDelegate__on_policy_changed(self):
        ...
    def _TypeColumnDelegate__update_label_from_policy(self):
        ...
    def __init__(self):
        ...
    def build_header(self, **kwargs):
        """
        Build the header
        """
    def build_widget(self, _, **kwargs):
        """
        Build the type widget
        """
    def destroy(self):
        ...
    def on_stage_items_destroyed(self, items: typing.List[omni.kit.widget.stage.stage_item.StageItem]):
        ...
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
class TypeColumnSortPolicy(enum.Enum):
    """
    An enumeration.
    """
    A_TO_Z: typing.ClassVar[TypeColumnSortPolicy]  # value = <TypeColumnSortPolicy.A_TO_Z: 1>
    DEFAULT: typing.ClassVar[TypeColumnSortPolicy]  # value = <TypeColumnSortPolicy.DEFAULT: 0>
    Z_TO_A: typing.ClassVar[TypeColumnSortPolicy]  # value = <TypeColumnSortPolicy.Z_TO_A: 2>
WIDGET_STYLES: dict = {'TreeView.Image::object_icon_grey': {'color': 2164260863}, 'TreeView.Item::object_name_grey': {'color': 4283255618}, 'TreeView.Item::object_name_missing': {'color': 4285494015}}
