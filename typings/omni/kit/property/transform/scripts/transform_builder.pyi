"""
A module for building and managing transform widgets for USD primitives in Omniverse Kit applications.

This module provides functionality to create user interface elements for manipulating the transform properties (translation, rotation, scale) of USD primitives. It supports operations such as adding, multiplying, and resetting transformations directly from the UI, and handles both single and multiple selection of primitives.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
from collections import defaultdict
import copy as copy
import enum
from enum import Enum
import functools as functools
import omni as omni
from omni.hydra.scene_api.bindings._omni_hydra_scene_api import get_wgs84_coords
from omni.kit.property.transform.scripts.transform_model import VecAttributeModel
from omni.kit.property.transform.scripts import xform_op_utils
from omni.kit.property.usd.usd_attribute_model import GfMatrixAttributeModel
from omni.kit.property.usd.usd_attribute_model import GfQuatAttributeModel
from omni.kit.property.usd.usd_attribute_model import GfQuatEulerAttributeModel
from omni.kit.property.usd.usd_attribute_model import GfVecAttributeModel
from omni.kit.property.usd.usd_attribute_model import GfVecAttributeSingleChannelModel
from omni.kit.property.usd.usd_attribute_model import UsdAttributeModel
from omni.kit.property.usd.usd_model_base import UsdBase
from omni.kit.property.usd.usd_property_widget_builder import UsdPropertiesWidgetBuilder
from omni.kit.widget.highlight_label.highlight_label import HighlightLabel
from omni import ui
import pathlib
from pxr import Gf
from pxr import Sdf
import pxr.Tf
from pxr import Tf
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
import typing
import usdrt as usdrt
__all__ = ['Enum', 'FabricGfMatrixAttributeModel', 'FabricGfQuatAttributeModel', 'FabricGfQuatEulerAttributeModel', 'FabricGfVecAttributeSingleChannelModel', 'Gf', 'GfMatrixAttributeModel', 'GfQuatAttributeModel', 'GfQuatEulerAttributeModel', 'GfVecAttributeModel', 'GfVecAttributeSingleChannelModel', 'HighlightLabel', 'ICON_PATH', 'LABEL_PADDING', 'OperationTypes', 'Sdf', 'TRANSFORM_MODE_GLOBAL', 'TRANSFORM_MODE_LOCAL', 'TRANSFORM_MOVE_MODE_SETTING', 'TRANSFORM_OP_MOVE', 'TRANSFORM_OP_ROTATE', 'TRANSFORM_OP_SCALE', 'TRANSFORM_OP_SETTING', 'TRANSFORM_ROTATE_MODE_SETTING', 'Tf', 'TransformWatchModel', 'TransformWidgets', 'USDNoAttributeOpWidget', 'USDResetXformStackWidget', 'USDXformOpOrientWidget', 'USDXformOpRotateScalarWidget', 'USDXformOpRotateWidget', 'USDXformOpScaleWidget', 'USDXformOpTransformWidget', 'USDXformOpTranslateWidget', 'USDXformOpWidget', 'Usd', 'UsdAttributeModel', 'UsdBase', 'UsdGeom', 'UsdPropertiesWidgetBuilder', 'VecAttributeModel', 'asyncio', 'carb', 'copy', 'defaultdict', 'euler_view_button_style', 'functools', 'get_wgs84_coords', 'omni', 'quat_view_button_style', 'ui', 'usdrt', 'xform_op_utils']
class FabricGfMatrixAttributeModel(omni.kit.property.usd.usd_attribute_model.GfMatrixAttributeModel):
    """
    A class for handling matrix attribute models in the Fabric engine.
    
        This class provides functionality for manipulating GfMatrix-based attributes within the Fabric engine. It extends the GfMatrixAttributeModel, allowing for the display and manipulation of matrix values without altering the USD values directly.
    
            Args:
                stage: The Usd.Stage on which the matrix attributes exist.
                attribute_paths (List[Sdf.Path]): A list of paths to the matrix attributes.
                comp_count (int): The number of components in the matrix (e.g., 4 for a 4x4 matrix).
                tf_type (Tf.Type): The type of the transformation represented by the matrix.
                self_refresh (bool): Indicates whether the model should refresh itself automatically.
                metadata (dict): A dictionary containing metadata for the matrix attributes.
    """
    def __init__(self, stage, attribute_paths: typing.List[pxr.Sdf.Path], comp_count: int, tf_type: pxr.Tf.Type, self_refresh: bool, metadata: dict):
        """
        Initializes a FabricGfMatrixAttributeModel instance.
        """
    def _on_dirty(self):
        ...
    def get_item_children(self, item):
        """
        Gets children items of a specific item.
        
                Args:
                    item (Item): The item to retrieve children from.
        """
    def set_fabric_value(self, value):
        """
        Sets the fabric value for the matrix attribute.
        
                Args:
                    value (float): The new fabric value to set for the matrix attribute.
        """
    def set_value(self, *args):
        """
        Sets the value for the matrix attribute.
        
                Args:
                    value (float): The new value to set for the matrix attribute.
        """
class FabricGfQuatAttributeModel(omni.kit.property.usd.usd_attribute_model.GfQuatAttributeModel):
    """
    A class representing a quaternion attribute for fabric with USD support.
    
        This model allows for manipulation of quaternion-based transformations in a fabric context while maintaining compatibility with USD attributes.
    
            Args:
                stage (Usd.Stage): The USD stage to which the attribute belongs.
                attribute_paths (List[Sdf.Path]): The Sdf.Paths to the quaternion attributes.
                tf_type (Tf.Type): The type of the transformation.
                self_refresh (bool): Indicates whether the model should automatically refresh.
                metadata (dict): A dictionary containing metadata for the attribute.
    """
    def __init__(self, stage, attribute_paths: typing.List[pxr.Sdf.Path], tf_type: pxr.Tf.Type, self_refresh: bool, metadata: dict):
        """
        Initializes the FabricGfQuatAttributeModel instance.
        """
    def _on_dirty(self):
        ...
    def set_fabric_value(self, value):
        """
        Sets the internal fabric value without changing the USD attribute.
        
                Args:
                    value (Any): The new internal fabric value to set.
        """
    def set_value(self, value):
        """
        Sets the attribute value and marks the internal fabric value as invalid.
        
                Args:
                    value (Any): The new value to set for the attribute.
        """
class FabricGfQuatEulerAttributeModel(omni.kit.property.usd.usd_attribute_model.GfQuatEulerAttributeModel):
    """
    A model for representing quaternion or euler attributes for the Fabric engine.
    
        This model facilitates the manipulation of rotation attributes in both quaternion (quat) or euler angles. It allows
        for setting and getting rotation values, and converting between different rotation representations as required by
        the Fabric engine.
    
            Args:
                stage (Usd.Stage): The stage on which the attribute exists.
                attribute_paths (List[Sdf.Path]): A list of paths to the attributes.
                tf_type (Tf.Type): The transformation type, either a quaternion or euler rotation.
                self_refresh (bool): A flag indicating whether the model should refresh itself.
                metadata (dict): A dictionary containing metadata for the attribute.
    """
    def __init__(self, stage, attribute_paths: typing.List[pxr.Sdf.Path], tf_type: pxr.Tf.Type, self_refresh: bool, metadata: dict):
        """
        Initializes a FabricGfQuatEulerAttributeModel instance.
        """
    def _on_dirty(self):
        ...
    def set_fabric_value(self, value):
        """
        Sets the fabric value of the attribute.
        
                Args:
                    value: The fabric value to set.
        """
    def set_value(self, value):
        """
        Sets the value of the attribute.
        
                Args:
                    value: The value to set.
        """
class FabricGfVecAttributeSingleChannelModel(omni.kit.property.usd.usd_attribute_model.GfVecAttributeSingleChannelModel):
    """
    A model representing a single channel of a GfVec attribute for fabric manipulation.
    
        This model extends the GfVecAttributeSingleChannelModel to support the representation
        and manipulation of fabric values without changing the underlying USD values. It provides
        methods to get and set the value of the attribute as various data types (string, float, int, bool),
        and to set a fabric-specific value.
    
            Args:
                stage (Usd.Stage): The stage containing the attribute.
                attribute_paths (List[Sdf.Path]): A list of paths to the attributes.
                channel_index (int): The index of the channel within the GfVec attribute.
                self_refresh (bool): Whether the model should refresh itself.
                metadata (dict): Metadata associated with the attribute.
                change_on_edit_end (bool): Whether to change the value only at the end of an edit.
    
            Keyword Args:
                Additional keyword arguments are supported but not listed explicitly.
    """
    def __init__(self, stage, attribute_paths: typing.List[pxr.Sdf.Path], channel_index: int, self_refresh: bool, metadata: dict, change_on_edit_end = True, **kwargs):
        """
        Initializes the FabricGfVecAttributeSingleChannelModel instance.
        """
    def _on_dirty(self):
        ...
    def get_value_as_bool(self) -> bool:
        """
        Returns the value of the attribute as a boolean.
        """
    def get_value_as_float(self) -> float:
        """
        Returns the value of the attribute as a float.
        """
    def get_value_as_int(self) -> int:
        """
        Returns the value of the attribute as an integer.
        """
    def get_value_as_string(self, **kwargs) -> str:
        """
        Returns the value of the attribute as a string.
        
                Keyword Args:
                    precision (int): The numeric precision for formatting the string.
        """
    def set_fabric_value(self, value):
        """
        Sets the fabric value of the attribute.
        
                Args:
                    value (float): The new fabric value to set.
        """
    def set_value(self, value):
        """
        Sets the value of the attribute.
        
                Args:
                    value (float): The new value to set.
        """
class OperationTypes(enum.Enum):
    """
    An enumeration for defining operation types.
    
        This enumeration defines different types of operations that can be performed. It includes operations for addition, multiplication, and marking invalid operations.
    
            Attributes:
                ADD (int): Represents an addition operation.
                MULTIPLY (int): Represents a multiplication operation.
                INVALID (int): Represents an invalid or unrecognized operation.
    """
    ADD: typing.ClassVar[OperationTypes]  # value = <OperationTypes.ADD: 0>
    INVALID: typing.ClassVar[OperationTypes]  # value = <OperationTypes.INVALID: 2>
    MULTIPLY: typing.ClassVar[OperationTypes]  # value = <OperationTypes.MULTIPLY: 1>
class TransformWatchModel(omni.ui._ui.AbstractValueModel):
    """
    A class for monitoring changes to a USD transform component.
    
        This model tracks changes to a specific component of a transform in USD, updating its value
        as the transform changes. It is typically used for displaying transform component values in a UI.
    
            Args:
                component_index (int): The index of the transform component to monitor.
                stage (Usd.Stage): The USD stage where the monitored transform is located.
    """
    def __init__(self, component_index, stage):
        """
        Initializes the TransformWatchModel with a component index and USD stage.
        """
    def _on_usd_changed(self, path = None):
        ...
    def clean(self):
        """
        Cleans up resources and unsubscribes from USD changes.
        """
    def get_value_as_float(self) -> float:
        """
        Returns the current value as a float.
        """
    def get_value_as_string(self) -> str:
        """
        Returns the current value as a string.
        """
    def set_value(self, new_value: typing.Any) -> None:
        """
        Sets the value of the model.
        
                Args:
                    new_value (Any): The new value to be set.
        """
class TransformWidgets:
    """
    A widget for transforming selected USD primitives.
    
        This widget provides a user interface for applying transformations such as translate, rotate, and scale to selected USD primitives. It supports uniform and non-uniform scaling, and can display and modify transformations in both global and local coordinate spaces.
    
            Args:
                parent_widget: A reference to the parent widget that contains this transform widget.
    """
    def __del__(self):
        ...
    def __init__(self, parent_widget):
        """
        Initializes a TransformWidgets instance.
        
                Args:
                    parent_widget: A reference to the parent widget to contain this transform widget.
        """
    def _clear_widgets(self):
        ...
    def _create_multi_string_with_labels(self, ui_widget, model, labels, comp_count):
        ...
    def _create_xform_op_widget(self, prim_paths, collapsable_frame, stage, attr, op_name = None, is_valid_op = False, op_order_attr = None, op_order_index = -1):
        ...
    def _end_string_edit(self, transform):
        ...
    def _get_common_xformop(self, prim_paths):
        ...
    def _get_offset_data(self, text: str):
        ...
    def _get_widget(self, transform):
        ...
    def _on_double_click(self, transform):
        ...
    def _on_press(self):
        ...
    def _on_rotate_offset(self, offset_text: str, index: int, stage: pxr.Usd.Stage, prim_paths: typing.List[pxr.Sdf.Path]):
        ...
    def _on_scale_offset(self, offset_text: str, index: int, stage: pxr.Usd.Stage, prim_paths: typing.List[pxr.Sdf.Path]):
        ...
    def _on_translate_offset(self, offset_text: str, index: int, stage: pxr.Usd.Stage, prim_paths: typing.List[pxr.Sdf.Path]):
        ...
    def _start_field_edit(self, index, transform):
        ...
    def _swapping(self, transform):
        ...
    def build_transform_frame(self, prim_paths, collapsable_frame, stage):
        """
        Builds the transformation UI for the selected USD prim(s).
        
                Args:
                    prim_paths (List[Sdf.Path]): The USD prim paths to build the transform UI for.
                    collapsable_frame (ui.Frame): The frame to contain the transform UI.
                    stage (Usd.Stage): The stage the prims belong to.
        
                Returns:
                    Tuple[defaultdict, bool]: Returns a models dict and a boolean indicating empty xform ops.
        """
    def build_transform_offset_frame(self, prim_paths, collapsable_frame, stage):
        """
        Builds the transformation offset UI for the selected USD prim(s).
        
                Args:
                    prim_paths (List[Sdf.Path]): The USD prim paths to build the offset UI for.
                    collapsable_frame (ui.Frame): The frame to contain the offset UI.
                    stage (Usd.Stage): The stage the prims belong to.
        """
    def clear_widgets(self):
        ...
    def get_widgets(self):
        ...
    def update_from_matrix(self, matrix: usdrt.Gf.Matrix4d):
        """
        Updates the widget from the given transformation matrix.
        
                Args:
                    matrix (usdrt.Gf.Matrix4d): The transformation matrix to update the widget from.
        """
class USDNoAttributeOpWidget(USDXformOpWidget):
    """
    A widget representing a USD operation without an associated attribute.
    
        This widget is used to represent operations that are present in the xformOpOrder but do not have a corresponding attribute in the USD stage. It provides options to disable or delete the operation directly from the UI.
    
            Args:
                prim_paths (List[Sdf.Path]): The paths to the USD prims.
                collapsable_frame (ui.Frame): Reference to the collapsable frame that contains this widget.
                stage (Usd.Stage): The USD stage where the operation exists.
                attr (Usd.Attribute): The attribute associated with the operation, if any.
                op_name (str): The name of the operation.
                is_valid_op (bool): Flag indicating if the operation is valid.
                op_order_attr_path (Sdf.Path): The path to the attribute that specifies the operation order.
                op_order_index (int): The index of the operation in the operation order list.
    """
    def rebuild(self):
        """
        Rebuilds the widget without any specific attributes.
        """
class USDResetXformStackWidget(USDXformOpWidget):
    """
    A widget for resetting transformation stacks on USD prims.
    
        This widget provides the functionality to reset the transformation stack of selected USD primitives to a
        specified state. It invalidates all transform operations above the reset position and recalculates the
        world transform from the operations below the reset position.
    
            Args:
                prim_paths (List[Sdf.Path]): Paths of the selected USD primitives.
                collapsable_frame (ui.Frame): The UI frame that can be collapsed or expanded.
                stage (Usd.Stage): The current USD stage.
                attr (Usd.Attribute): The attribute associated with the reset operation.
                op_name (str): The name of the reset operation.
                is_valid_op (bool): Indicates whether the operation is valid.
                op_order_attr_path (Sdf.Path): The attribute path for the order of operations.
                op_order_index (int): The index of the reset operation in the order of operations list.
    """
    def rebuild(self):
        """
        Rebuilds the widget for USDResetXformStack.
        
                This method clears any existing widgets and initializes the necessary UI components for the USDResetXformStack widget.
        
                Args:
                    prim_paths (List[Sdf.Path]): List of USD prim paths to rebuild the widget for.
                    collapsable_frame (ui.Frame): The frame that can be expanded or collapsed to show or hide the widget.
                    stage (Usd.Stage): The stage where the USD prims are located.
        """
class USDXformOpOrientWidget(USDXformOpWidget):
    """
    A class representing the widget for manipulating the orient attribute in USD.
    
        This widget allows for the editing of quaternion-based orientation attributes of a USD prim. It provides a user interface for inputting quaternion values directly or modifying them through an interactive euler angle representation.
    
            Args:
                prim_paths (List[Sdf.Path]): The USD prim paths that the widget will operate on.
                collapsable_frame (ui.Frame): A frame in the UI that can be collapsed.
                stage (Usd.Stage): The stage where the prim paths are located.
                attr_path (Sdf.Path): The path to the orient attribute.
                op_name (str): The name of the operation for this widget.
                is_valid_op (bool): Indicates if the operation is valid.
                op_order_attr_path (Sdf.Path): The path to the attribute that specifies the order of operations.
                op_order_index (int): The index of this operation in the operation order.
                label_kwargs (dict, optional): Keyword arguments for configuring the label of the widget.
    """
    @classmethod
    def display_name(cls, attr_name: str) -> str:
        """
        Generates a display name for orient transform operation.
        
                Args:
                    attr_name (str): The name of the attribute representing the orient transform operation.
        
                Returns:
                    str: A string representing the display name for the orient transform operation.
        """
    def __init__(self, prim_paths, collapsable_frame, stage, attr_path, op_name, is_valid_op, op_order_attr_path, op_order_index, label_kwargs = None):
        """
        Initializes the USDXformOpOrientWidget instance.
        
                Args:
                    prim_paths (List[Sdf.Path]): Paths to the USD prims to construct the widget for.
                    collapsable_frame (ui.Frame): The UI frame that can be collapsed or expanded.
                    stage (Usd.Stage): The stage containing the prims.
                    attr_path (Sdf.Path): The path to the orient attribute.
                    op_name (str): The name of the orient operation.
                    is_valid_op (bool): Indicates whether the operation is valid.
                    op_order_attr_path (Sdf.Path): The path to the attribute that defines the operation order.
                    op_order_index (int): The index of the operation in the operation order.
                    label_kwargs (dict, optional): Additional keyword arguments for label formatting.
        """
    def _build_euler_widgets(self, attr, attr_name, type_name, label_name, label_tooltip, metadata):
        ...
    def _build_header(self, attr, attr_name, type_name, label_name, label_tooltip, metadata):
        ...
    def _build_orient_widgets(self, attr, attr_name, type_name, label_name, label_tooltip, metadata):
        ...
    def rebuild(self):
        """
        Rebuilds the widget to represent the orient operation.
        """
    def update_fabric_value_only(self, vec_value):
        """
        Updates the fabric value of the orient attribute without changing the USD value.
        
                Args:
                    vec_value (Gf.Quat): The new fabric value to set for the orient attribute.
        """
class USDXformOpRotateScalarWidget(USDXformOpWidget):
    """
    A widget for applying scalar rotation to a single axis of selected USD prims.
    
        This widget allows for rotation of selected prims around a single specified axis (X, Y, or Z). Users can input scalar values to directly set the rotation angle, or use a slider to adjust the angle interactively. The rotation operation can be performed in either local or global space, depending on the current transform mode setting.
        
    """
    @classmethod
    def display_name(cls, attr_name: str) -> str:
        """
        Generates the display name for the rotate operation.
        
                Args:
                    attr_name (str): The full attribute name of the rotate operation.
        
                Returns:
                    str: The display name for the rotate operation.
        """
    def rebuild(self):
        """
        Rebuilds the widget for a scalar rotate operation attribute.
        """
class USDXformOpRotateWidget(USDXformOpWidget):
    """
    A widget for manipulating rotation of USD primitives.
    
        This widget allows users to interactively adjust the rotation of selected USD primitives. It supports different rotation orders (e.g., XYZ, XZY, YXZ, etc.) and can represent rotations in both quaternion and euler angles. Users can switch between quaternion and euler views, and also change the rotation order dynamically.
    
            Args:
                prim_paths (List[Sdf.Path]): The paths of the selected USD primitives.
                collapsable_frame: The collapsable frame containing the widget.
                stage (Usd.Stage): The USD stage that the primitives belong to.
                attr_path (Sdf.Path): The path to the rotation attribute.
                op_name (str): The name of the rotation operation.
                is_valid_op (bool): Indicates if the operation is valid.
                op_order_attr_path (Sdf.Path): The path to the attribute that specifies the operation order.
                op_order_index (int): The index of the operation in the operation order.
                label_kwargs (dict, optional): Additional keyword arguments for label customization.
    """
    ROTATE_AXIS_ORDER_INDEX: typing.ClassVar[dict] = {'xformOp:rotateXYZ': [0, 1, 2], 'xformOp:rotateXZY': [0, 2, 1], 'xformOp:rotateYXZ': [1, 0, 2], 'xformOp:rotateYZX': [1, 2, 0], 'xformOp:rotateZXY': [2, 0, 1], 'xformOp:rotateZYX': [2, 1, 0]}
    ROTATE_AXIS_ORDER_MAP: typing.ClassVar[dict] = {'xformOp:rotateXYZ': ['X', 'Y', 'Z'], 'xformOp:rotateXZY': ['X', 'Z', 'Y'], 'xformOp:rotateYXZ': ['Y', 'X', 'Z'], 'xformOp:rotateYZX': ['Y', 'Z', 'X'], 'xformOp:rotateZXY': ['Z', 'X', 'Y'], 'xformOp:rotateZYX': ['Z', 'Y', 'X']}
    ROTATE_ORDERS: typing.ClassVar[list] = ['XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX']
    @staticmethod
    def get_rotation_order_index(order):
        """
        Gets the index of the rotation order from a predefined list.
        
                Args:
                    order (str): The rotation order to get the index for.
        
                Returns:
                    int: The index of the rotation order.
        """
    @classmethod
    def display_name(cls, attr_name: str) -> str:
        """
        Generates a display name for the rotate widget based on attribute name.
        
                Args:
                    attr_name (str): The name of the attribute to generate a display name for.
        
                Returns:
                    str: The generated display name.
        """
    def __del__(self):
        ...
    def __init__(self, prim_paths, collapsable_frame, stage, attr_path, op_name, is_valid_op, op_order_attr_path, op_order_index, label_kwargs = None):
        """
        Initializes a USDXformOpRotateWidget instance.
        """
    def _change_rotation_order(self, desired_order_index):
        ...
    def _on_mouse_click(self, button, parent, order):
        ...
    def rebuild(self):
        """
        Rebuilds the widget based on the current state.
        """
    def update_fabric_value_only(self, vec_value):
        """
        Updates the widget's fabric value without affecting the USD value.
        
                Args:
                    vec_value (Gf.Vec3f): The vector value to update the widget with.
        """
class USDXformOpScaleWidget(USDXformOpWidget):
    """
    A widget for adjusting the scale of a USD primitive's xformOp.
    
        This class provides a user interface within the property panel to interactively scale a USD primitive. It supports uniform and non-uniform scaling, and can work with multiple selection.
    
            Args:
                prim_paths (List[Sdf.Path]): The paths to the primitives being edited.
                collapsable_frame (ui.Frame): The parent frame that can be collapsed.
                stage (Usd.Stage): The stage where the primitives exist.
                attr_path (Sdf.Path): The path to the scale attribute.
                op_name (str): The name of the operation attributing to the scaling.
                is_valid_op (bool): Flag indicating if the operation is valid.
                op_order_attr_path (Sdf.Path): The path to the xformOp order attribute.
                op_order_index (int): The index of the operation in the xformOp order.
                parent_widget: The widget that contains this scale operation widget.
                label_kwargs (dict): Additional keyword arguments for label customization.
    """
    @classmethod
    def display_name(cls, attr_name: str) -> str:
        """
        Generates a display name for scale transform operations.
        
                Args:
                    attr_name (str): The name of the attribute associated with the transform operation.
        
                Returns:
                    str: The display name for the scale transform operation.
        """
    def __init__(self, prim_paths, collapsable_frame, stage, attr_path, op_name, is_valid_op, op_order_attr_path, op_order_index, parent_widget, label_kwargs = None):
        """
        Initializes a USDXformOpScaleWidget instance.
        
                Args:
                    prim_paths (List[Sdf.Path]): The paths of the prims associated with the widget.
                    collapsable_frame (ui.Frame): The frame that can be collapsed in the UI.
                    stage (Usd.Stage): The stage in which the prims reside.
                    attr_path (Sdf.Path): The path to the attribute.
                    op_name (str): The name of the operation.
                    is_valid_op (bool): Indicates if the operation is valid.
                    op_order_attr_path (Sdf.Path): The path to the attribute that defines the order of operations.
                    op_order_index (int): The index of the operation in the order.
                    parent_widget: The parent widget this widget is part of.
                    label_kwargs (dict, optional): Additional keyword arguments for the label.
        """
    def rebuild(self):
        """
        Reconstructs the scale widget with current stage and attribute information.
        """
class USDXformOpTransformWidget(USDXformOpWidget):
    """
    A widget for applying transform operations to USD prims.
    
        This widget provides an interface to apply translation, rotation, and scaling operations to selected USD prims within the stage. It supports operations in both local and global coordinate spaces, and facilitates both direct manipulation and numerical input of transform values.
    
            Args:
                prim_paths (List[Sdf.Path]): List of paths to the prims that the transform operations are applied to.
                collapsable_frame (ui.Frame): The UI frame that this widget will be a part of.
                stage (Usd.Stage): The stage where the prims are located.
    """
    @classmethod
    def display_name(cls, attr_name: str) -> str:
        """
        Returns the display name for the transform operation.
        
                Args:
                    attr_name (str): The name of the attribute representing the operation.
        
                Returns:
                    str: The formatted display name.
        """
    def rebuild(self):
        """
        Rebuilds the widget for the transform operation.
        """
    def update_fabric_value_only(self, vec_value):
        """
        Updates the value of the transform operation without affecting the USD value.
        
                Args:
                    vec_value (usdrt.Gf.Matrix4d): The new value for the transform operation.
        """
class USDXformOpTranslateWidget(USDXformOpWidget):
    """
    A widget for translating selected USD primitives.
    
        This widget allows users to manipulate the translation of selected USD primitives in the scene. It provides an interface for editing the translation values directly or applying incremental changes.
    
            Args:
                prim_paths (List[Sdf.Path]): The paths to the USD primitives being manipulated.
                collapsable_frame (ui.Frame): The UI frame that should be collapsible.
                stage (Usd.Stage): The USD stage where the primitives exist.
                attr_path (Sdf.Path): The path to the translation attribute.
                op_name (str): The name of the translate operation.
                is_valid_op (bool): Indicates if the operation is valid.
                op_order_attr_path (Sdf.Path): The path to the attribute that defines the order of operations.
                op_order_index (int): The index of the operation in the operations order list.
                label_kwargs (Optional[dict]): Additional keyword arguments for custom label options.
    """
    @classmethod
    def display_name(cls, attr_name: str) -> str:
        """
        Generates a label for the translate operation based on the attribute name.
        
                Args:
                    attr_name (str): Name of the attribute associated with the translate operation.
        
                Returns:
                    str: A label for the translate operation.
        """
    def rebuild(self):
        """
        Reconstructs the widget for the translate operation.
        
                This method builds the widget interface for the translate operation of a USD primitive. It checks if the attribute name starts with 'xformOp:translate' and, if not, logs a warning. The method also handles inverse operations and suffixes, and creates UI components based on the attribute's metadata.
                
        """
class USDXformOpWidget:
    """
    A widget for manipulating USD transform operations on selected primitives.
    
        This widget includes UI components for translating, rotating, scaling, and applying other
        transform operations such as orient and transform to the selected USD primitives. It supports
        interactions such as mouse dragging and direct text input for precise control over the
        transform operations.
    
            Args:
                prim_paths (List[Sdf.Path]): Paths to the USD primitives being manipulated.
                collapsable_frame (ui.Frame): The UI frame that can be collapsed or expanded.
                stage (Usd.Stage): The USD stage where the primitives reside.
                attr_path (Sdf.Path): Path to the USD attribute representing the transform operation.
                op_name (str): Name of the transform operation (e.g., 'xformOp:translate').
                is_valid_op (bool): Indicates whether the operation is valid and should be processed.
                op_order_attr_path (Sdf.Path): Path to the 'xformOpOrder' attribute if it exists.
                op_order_index (int): Index of the operation within the 'xformOpOrder' attribute.
                label_kwargs (dict, optional): Additional keyword arguments for UI label customization.
    """
    def __del__(self):
        ...
    def __init__(self, prim_paths, collapsable_frame, stage, attr_path, op_name, is_valid_op, op_order_attr_path, op_order_index, label_kwargs = None):
        """
        Initializer for the USDXformOpWidget class.
        """
    def _add_non_op_attribute_to_op(self):
        ...
    def _create_inverse_widgets(self):
        ...
    def _create_multi_float_drag_matrix_with_labels(self, model, comp_count, _min, _max, step, labels):
        ...
    def _delete_non_op_attribute(self):
        ...
    def _delete_op_and_attribute(self):
        ...
    def _delete_op_only(self):
        ...
    def _inverse_op(self):
        ...
    def _on_display_orient_as_rotate(self):
        ...
    def _on_orient_button_clicked(self, mouse_button, widget):
        ...
    def _show_right_click_menu(self, button):
        ...
    def _toggle_orient_button_style(self, button):
        ...
    def on_display_orient_as_rotate(self):
        ...
    def rebuild(self):
        ...
    def toggle_orient_button_style(self, button):
        ...
    def update_fabric_value_only(self, vec_value):
        """
        Updates the widget with a new value without affecting the USD attribute.
        
                Args:
                    vec_value (Gf.Vec3d): The new vector value to be used for the update.
        """
ICON_PATH: pathlib.PosixPath  # value = PosixPath('/home/chris/isaacsim/extscache/omni.kit.property.transform-1.5.10+d02c707b/data/icons')
LABEL_PADDING: int = 128
TRANSFORM_MODE_GLOBAL: str = 'global'
TRANSFORM_MODE_LOCAL: str = 'local'
TRANSFORM_MOVE_MODE_SETTING: str = '/app/transform/moveMode'
TRANSFORM_OP_MOVE: str = 'move'
TRANSFORM_OP_ROTATE: str = 'rotate'
TRANSFORM_OP_SCALE: str = 'scale'
TRANSFORM_OP_SETTING: str = '/app/transform/operation'
TRANSFORM_ROTATE_MODE_SETTING: str = '/app/transform/rotateMode'
euler_view_button_style: dict  # value = {'Button:hovered': {'background_color': 4280492319}, 'Button': {'background_color': 4280492319, 'padding': 0, 'stack_direction': <Direction.RIGHT_TO_LEFT: 1>}, 'Button.Label': {'color': 4288707919, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'Button.Tooltip': {'color': 4288585374}, 'Button.Image': {'color': 4294954137, 'alignment': <Alignment.CENTER: 72>}}
quat_view_button_style: dict  # value = {'Button:hovered': {'background_color': 4283914071}, 'Button': {'background_color': 4281545523, 'padding': 0, 'stack_direction': <Direction.RIGHT_TO_LEFT: 1>}, 'Button.Label': {'color': 4288585374, 'alignment': <Alignment.LEFT_CENTER: 66>}, 'Button.Tooltip': {'color': 4288585374}, 'Button.Image': {'color': 4294954137, 'alignment': <Alignment.CENTER: 72>}}
