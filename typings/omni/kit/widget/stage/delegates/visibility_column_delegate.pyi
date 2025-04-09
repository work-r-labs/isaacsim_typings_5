from __future__ import annotations
import enum
from enum import Enum
import omni.kit.widget.stage.abstract_stage_column_delegate
from omni.kit.widget.stage.abstract_stage_column_delegate import AbstractStageColumnDelegate
from omni.kit.widget.stage.stage_item import StageItem
from omni.kit.widget.stage.stage_model import StageItemSortPolicy
from omni.kit.widget.stage.stage_model import StageModel
from omni import ui
from pxr import UsdGeom
import typing
__all__: list = ['VisibilityColumnDelegate']
class VisibilityColumnDelegate(omni.kit.widget.stage.abstract_stage_column_delegate.AbstractStageColumnDelegate):
    """
    The column delegate that represents the visibility column
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def _VisibilityColumnDelegate__initialize_policy_from_model(self):
        ...
    def _VisibilityColumnDelegate__on_policy_changed(self):
        ...
    def _VisibilityColumnDelegate__on_visiblity_clicked(self, x, y, b, m):
        ...
    def __init__(self):
        ...
    def build_header(self, **kwargs):
        """
        Build the header
        """
    def build_widget(self, _, **kwargs):
        """
        Build the eye widget
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
    def resizable(self):
        ...
    @property
    def sortable(self):
        ...
class VisibilityColumnSortPolicy(enum.Enum):
    """
    An enumeration.
    """
    DEFAULT: typing.ClassVar[VisibilityColumnSortPolicy]  # value = <VisibilityColumnSortPolicy.DEFAULT: 0>
    INVISIBLE_TO_VISIBLE: typing.ClassVar[VisibilityColumnSortPolicy]  # value = <VisibilityColumnSortPolicy.INVISIBLE_TO_VISIBLE: 1>
    VISIBLE_TO_INVISIBLE: typing.ClassVar[VisibilityColumnSortPolicy]  # value = <VisibilityColumnSortPolicy.VISIBLE_TO_INVISIBLE: 2>
def _get_header_styles():
    ...
def _get_widget_styles():
    ...
