from __future__ import annotations
from _ctypes import alignment
import enum
from enum import Enum
from functools import partial
from isaacsim.asset.importer.urdf._urdf import UrdfJointDriveType
from isaacsim.asset.importer.urdf._urdf import UrdfJointTargetType
from isaacsim.asset.importer.urdf._urdf import UrdfJointType
from isaacsim.asset.importer.urdf._urdf import acquire_urdf_interface
from isaacsim.asset.importer.urdf.scripts.ui.resetable_widget import ResetableLabelField
from isaacsim.asset.importer.urdf.scripts.ui.style import get_style
from omni import ui
import omni.ui._ui
import re
import typing
__all__ = ['ComboListModel', 'Enum', 'I', 'ITEM_HEIGHT', 'JointDriveType', 'JointSettingMode', 'ResetableLabelField', 'SearchableItemSortPolicy', 'TreeViewIDColumn', 'UrdfJointDriveType', 'UrdfJointItem', 'UrdfJointItemDelegate', 'UrdfJointListModel', 'UrdfJointTargetType', 'UrdfJointType', 'UrdfJointWidget', 'acquire_urdf_interface', 'alignment', 'get_style', 'partial', 'ui']
class ComboListModel(omni.ui._ui.AbstractItemModel):
    class ComboListItem(omni.ui._ui.AbstractItem):
        def __init__(self, item):
            ...
    def __init__(self, item_list, default_index):
        ...
    def get_current_index(self):
        ...
    def get_item_children(self, item):
        ...
    def get_item_list(self):
        ...
    def get_item_value_model(self, item = None, column_id = -1):
        ...
    def get_value_as_string(self):
        ...
    def is_default(self):
        ...
    def set_current_index(self, index):
        ...
    def set_items(self, items):
        ...
class JointDriveType(enum.Enum):
    """
    The mode of setting joint parameters.
    """
    ACCELERATION: typing.ClassVar[JointDriveType]  # value = <JointDriveType.ACCELERATION: 0>
    FORCE: typing.ClassVar[JointDriveType]  # value = <JointDriveType.FORCE: 1>
class JointSettingMode(enum.Enum):
    """
    The mode of setting joint parameters.
    """
    NATURAL_FREQUENCY: typing.ClassVar[JointSettingMode]  # value = <JointSettingMode.NATURAL_FREQUENCY: 1>
    STIFFNESS: typing.ClassVar[JointSettingMode]  # value = <JointSettingMode.STIFFNESS: 0>
class SearchableItemSortPolicy(enum.Enum):
    """
    Sort policy for stage items.
    """
    A_TO_Z: typing.ClassVar[SearchableItemSortPolicy]  # value = <SearchableItemSortPolicy.A_TO_Z: 1>
    DEFAULT: typing.ClassVar[SearchableItemSortPolicy]  # value = <SearchableItemSortPolicy.DEFAULT: 0>
    Z_TO_A: typing.ClassVar[SearchableItemSortPolicy]  # value = <SearchableItemSortPolicy.Z_TO_A: 2>
class TreeViewIDColumn:
    """
    
        This is the ID (first) column of the TreeView. It's not part of the treeview delegate, because it's cheaper to do
        item remove in this way. And we dont need to update it when the treeview list is smaller than DEFAULT_ITEM_NUM.
        
    """
    DEFAULT_ITEM_NUM: typing.ClassVar[int] = 0
    def __init__(self, num = 0):
        ...
    def _build_frame(self):
        ...
    def add_item(self):
        ...
    def remove_item(self):
        ...
class UrdfJointItem(omni.ui._ui.AbstractItem):
    target_type: typing.ClassVar[list] = ['None', 'Position', 'Velocity']
    target_type_with_mimic: typing.ClassVar[list] = ['None', 'Position', 'Velocity', 'Mimic']
    def __init__(self, config, urdf_robot, joint, value_changed_fn = None):
        ...
    def _get_item_target_type(self):
        ...
    def _on_value_changed(self, col_id = 1, _ = None):
        ...
    def compute_drive_strength(self):
        ...
    def get_item_value(self, col_id = 0):
        ...
    def get_value_model(self, col_id = 0):
        ...
    def on_update_damping(self, model, *args):
        ...
    def on_update_damping_ratio(self, model, *args):
        ...
    def on_update_natural_frequency(self, model, *args):
        ...
    def on_update_strength(self, model, *args):
        ...
    def set_item_target_type(self, value):
        ...
    def set_item_value(self, col_id, value):
        ...
    @property
    def damping(self):
        ...
    @damping.setter
    def damping(self, value: float):
        ...
    @property
    def damping_ratio(self):
        ...
    @damping_ratio.setter
    def damping_ratio(self, value: float):
        ...
    @property
    def drive_type(self):
        ...
    @drive_type.setter
    def drive_type(self, value: JointDriveType):
        ...
    @property
    def natural_frequency(self):
        ...
    @natural_frequency.setter
    def natural_frequency(self, value: float):
        ...
    @property
    def strength(self):
        ...
    @strength.setter
    def strength(self, value: float):
        ...
class UrdfJointItemDelegate(omni.ui._ui.AbstractItemDelegate):
    header: typing.ClassVar[list] = ['Name', 'Target', 'Strength', 'Damping', 'Nat. Freq.', 'Damping R.']
    header_tooltip: typing.ClassVar[list] = ['Name', 'Target', 'Strength', 'Damping', 'Natural Frequency', 'Damping Ratio']
    def _UrdfJointItemDelegate__on_target_change(self, item, current_target: str):
        ...
    def __init__(self, model):
        ...
    def build_branch(self, model, item = None, column_id = 0, level = 0, expanded = False):
        ...
    def build_header(self, column_id = 0):
        ...
    def build_widget(self, model, item = None, index = 0, level = 0, expanded = False):
        ...
    def set_mode(self, mode):
        ...
    def sort_button_pressed_fn(self, b, column_id):
        ...
    def update_defaults(self):
        ...
    def update_mimic(self):
        ...
class UrdfJointListModel(omni.ui._ui.AbstractItemModel):
    def __init__(self, config, urdf_robot, joints_list, value_changed_fn, **kwargs):
        ...
    def _on_joint_changed(self, joint, col_id):
        ...
    def get_item_children(self, item = None):
        """
        Returns all the children when the widget asks it.
        """
    def get_item_value(self, item, column_id):
        ...
    def get_item_value_model(self, item, column_id):
        """
        
                Return value model.
                It's the object that tracks the specific value.
                
        """
    def get_item_value_model_count(self, item):
        """
        The number of columns
        """
    def set_drive_type(self, drive_type):
        ...
    def set_mode(self, mode):
        ...
    def sort_by_name(self, policy, column_id):
        ...
class UrdfJointWidget:
    def __init__(self, config, urdf_robot, joints, value_changed_fn = None):
        ...
    def _build_ui(self):
        ...
    def _on_value_changed(self, joint_item, col_id = 1):
        ...
    def set_bulk_edit(self, enable_bulk_edit: bool):
        ...
    def switch_drive_type(self, drive_type: JointDriveType):
        ...
    def switch_mode(self, switch: JointSettingMode):
        ...
    def update_mimic(self):
        ...
I: re.RegexFlag  # value = re.IGNORECASE
ITEM_HEIGHT: int = 26
