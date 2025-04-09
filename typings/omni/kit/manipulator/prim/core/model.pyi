"""
This module defines the PrimTransformModel for transforming USD prims in a viewport and handling related manipulations and gestures.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
import concurrent as concurrent
import enum
from enum import Enum
from enum import Flag
from enum import IntEnum
from enum import auto
import math as math
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.manipulator.prim.core.prim_data_accessor_selector import PrimDataAccessorSelector
from omni.kit.manipulator.prim.core.settings_constants import Constants as prim_c
from omni.kit.manipulator.prim.core.utils import compose_transform_ops_to_matrix
from omni.kit.manipulator.prim.core.utils import construct_transform_matrix_from_SRT
from omni.kit.manipulator.prim.core.utils import find_best_euler_angles
from omni.kit.manipulator.prim.core.utils import flatten
from omni.kit.manipulator.prim.core.utils import generate_compatible_euler_angles
from omni.kit.manipulator.prim.core.utils import repeat
from omni.kit.manipulator.tool.snap.manager import SnapProviderManager
from omni.kit.manipulator.tool.snap import settings_constants as snap_c
from omni.kit.manipulator.transform.model import AbstractTransformManipulatorModel
from omni.kit.manipulator.transform.settings_constants import Constants as transform_c
from omni.kit.manipulator.transform.settings_listener import OpSettingsListener
from omni.kit.manipulator.transform.settings_listener import SnapSettingsListener
from omni.kit.manipulator.transform.types import Operation
from omni.kit.viewport.manipulator.transform.gestures import ViewportRotateChangedGesture
from omni.kit.viewport.manipulator.transform.gestures import ViewportScaleChangedGesture
from omni.kit.viewport.manipulator.transform.gestures import ViewportTranslateChangedGesture
from omni.kit.viewport.manipulator.transform.model import ManipulationMode
from omni.kit.viewport.manipulator.transform.model import ViewportTransformModel
from omni.ui import scene as sc
import pxr as pxr
from pxr import Gf
from pxr import Usd
from pxr import UsdGeom
import traceback as traceback
import typing
import usdrt as usdrt
__all__ = ['AbstractTransformManipulatorModel', 'Enum', 'Flag', 'Gf', 'IntEnum', 'ManipulationMode', 'OpFlag', 'OpSettingsListener', 'Operation', 'PRINT_PERF_DATA', 'Placement', 'PrimDataAccessorSelector', 'PrimRotateChangedGesture', 'PrimScaleChangedGesture', 'PrimTransformModel', 'PrimTranslateChangedGesture', 'SnapProviderManager', 'SnapSettingsListener', 'TRANSFORM_GIZMO_CUSTOM_MANIPULATOR_ENABLED', 'TRANSFORM_GIZMO_CUSTOM_MANIPULATOR_PRIMS', 'TRANSFORM_GIZMO_IS_USING', 'TRANSFORM_GIZMO_PIVOT_WORLD_POSITION', 'TRANSFORM_GIZMO_ROTATE_DELTA_XYZW', 'TRANSFORM_GIZMO_SCALE_DELTA_XYZ', 'TRANSFORM_GIZMO_TRANSLATE_DELTA_XYZ', 'TRANSLATE_DELAY_FRAME_SETTING', 'Usd', 'UsdGeom', 'ViewportRotateChangedGesture', 'ViewportScaleChangedGesture', 'ViewportTransformModel', 'ViewportTranslateChangedGesture', 'asyncio', 'auto', 'carb', 'compose_transform_ops_to_matrix', 'concurrent', 'construct_transform_matrix_from_SRT', 'find_best_euler_angles', 'flatten', 'generate_compatible_euler_angles', 'math', 'omni', 'prim_c', 'pxr', 'repeat', 'run_coroutine', 'sc', 'snap_c', 'traceback', 'transform_c', 'usdrt']
class OpFlag(enum.Flag):
    """
    An enumeration defining operation flags for transformation.
    
        This enumeration subclass represents different types of transformation operations that can be applied to objects in a scene, such as translation, rotation, and scaling. Each member of this enumeration represents a distinct operation and can be combined using bitwise operations to represent multiple transformations simultaneously.
        
    """
    ROTATE: typing.ClassVar[OpFlag]  # value = <OpFlag.ROTATE: 2>
    SCALE: typing.ClassVar[OpFlag]  # value = <OpFlag.SCALE: 4>
    TRANSLATE: typing.ClassVar[OpFlag]  # value = <OpFlag.TRANSLATE: 1>
class Placement(enum.Enum):
    """
    An enumeration representing the various placement options for the transform manipulator.
    
        This enum defines where the pivot of the transform manipulator will be placed in relation to the selected primitives.
    
        Attributes:
            LAST_PRIM_PIVOT: The pivot is at the last selected primitive.
            SELECTION_CENTER: The pivot is centered among all selected primitives.
            BBOX_CENTER: The pivot is at the bounding box center of the selection.
            REF_PRIM: The pivot is at a referenced primitive.
            BBOX_BASE: The pivot is at the base of the bounding box of the selection.
    """
    BBOX_BASE: typing.ClassVar[Placement]  # value = <Placement.BBOX_BASE: 5>
    BBOX_CENTER: typing.ClassVar[Placement]  # value = <Placement.BBOX_CENTER: 3>
    LAST_PRIM_PIVOT: typing.ClassVar[Placement]  # value = <Placement.LAST_PRIM_PIVOT: 1>
    REF_PRIM: typing.ClassVar[Placement]  # value = <Placement.REF_PRIM: 4>
    SELECTION_CENTER: typing.ClassVar[Placement]  # value = <Placement.SELECTION_CENTER: 2>
class PrimRotateChangedGesture(omni.kit.viewport.manipulator.transform.gestures.ViewportRotateChangedGesture):
    """
    A derived gesture class to handle rotation changes for prims.
    
        This class extends the functionality of ViewportRotateChangedGesture by providing additional
        handling specific to rotation changes in the context of prims within a scene. It captures
        the changes in rotation initiated through the viewport manipulators and applies them to the
        relevant prims.
    """
class PrimScaleChangedGesture(omni.kit.viewport.manipulator.transform.gestures.ViewportScaleChangedGesture):
    """
    A gesture class that handles scaling changes for primitive objects in a viewport.
    
        This class responds to scaling manipulation gestures performed on USD primitive objects within a viewport. It extends the default viewport scaling gesture functionality with additional logic specific to primitive object scaling. The class is designed to work in conjunction with tools that manipulate the scale of USD prims visually, providing a means to capture and respond to user input related to scaling operations.
        
    """
class PrimTransformModel(omni.kit.viewport.manipulator.transform.model.ViewportTransformModel):
    """
    A model for transforming USD prims in a viewport.
    
        This model extends the functionality of the ViewportTransformModel to specifically handle the transformation
        of USD prims. It supports various operations such as translation, rotation, and scaling of prims
        within the USD scene. The model is capable of handling selections of multiple prims, applying
        transformations in different modes (e.g., global, local), and integrates with snapping and
        other viewport manipulation tools.
    
        The model also manages a selection of prims and updates their transformations based on user
        interactions in the viewport. It supports custom manipulators and can be extended to handle
        specific use cases in USD scene manipulation.
    
        Args:
            usd_context_name (str): The name of the USD context to operate within.
            viewport_api: The viewport API instance to interact with for viewport transformations.
    """
    @staticmethod
    def _path_may_affect_transform(*args, **kwds) -> bool:
        ...
    @staticmethod
    def _transform_all_selected_prims_to_manipulator_pivot(*args, **kwds):
        ...
    @staticmethod
    def _transform_selected_prims(*args, **kwds):
        ...
    @staticmethod
    def _update_transform_from_prims(*args, **kwds):
        ...
    @staticmethod
    def _update_transform_from_prims_async(*args, **kwargs):
        ...
    @staticmethod
    def _update_xform_data_from_dirty_paths(*args, **kwds):
        ...
    @staticmethod
    def on_objects_changed(*args, **kwds):
        """
        Called when objects in the stage have changed.
        
                Args:
                    args (List): A list of changed objects.
        
                Keyword Args:
                    kwds (Dict): Additional keyword arguments with details about the changes.
        """
    def __del__(self):
        ...
    def __init__(self, usd_context_name: str = '', viewport_api = None):
        """
        Initializes a new instance of PrimTransformModel, setting up the necessary properties and subscriptions for transforming USD prims in a viewport.
        """
    def _alert_if_selection_has_instance_proxies(self):
        ...
    def _calculate_transform_from_prim(self):
        ...
    def _check_update_selected_instance_proxy_list(self, path: self._data_accessor_selector.Sdf.Path, resynced):
        ...
    def _clear_temp_pivot_position_setting(self):
        ...
    def _delay_dirty(self, transform, id):
        ...
    def _get_transform_mode_for_current_op(self) -> str:
        ...
    def _on_op_listener_changed(self, type: OpSettingsListener.CallbackType, value: str):
        ...
    def _on_placement_setting_changed(self, item, event_type):
        ...
    def _on_stage_closing(self):
        ...
    def _on_stage_event(self, event: carb.events.IEvent):
        ...
    def _on_stage_opened(self):
        ...
    def _on_timeline_event(self, e: carb.events.IEvent):
        ...
    def _set_default_settings(self):
        ...
    def _should_keep_manipulator_orientation_unchanged(self, mode: str) -> bool:
        ...
    def _should_keep_manipulator_translation_unchanged(self, mode: str) -> bool:
        ...
    def _should_skip_custom_manipulator_path(self, path: str) -> bool:
        ...
    def _update_placement(self, placement_str: str):
        ...
    def _update_temp_pivot_world_position(self):
        ...
    def decompose_to_eulers(self, q: usdrt.Gf.Quatd, ro: usdrt.Gf.Vec3i) -> usdrt.Gf.Vec3d:
        """
        Decomposes a quaternion into Euler angles based on a rotation order.
        
                Args:
                    q (:obj:`usdrt.Gf.Quatd`): The quaternion to decompose.
                    ro (:obj:`usdrt.Gf.Vec3i`): The rotation order as a vector of 3 integers.
        
                Returns:
                    :obj:`usdrt.Gf.Vec3d`: The decomposed Euler angles.
        """
    def destroy(self):
        """
        Cleans up resources and subscriptions when the model is destroyed.
        """
    def get_as_floats(self, item: sc.AbstractManipulatorItem):
        """
        Gets the float values associated with a manipulator item.
        
                Args:
                    item (:obj:`sc.AbstractManipulatorItem`): The manipulator item whose values are to be retrieved.
        
                Returns:
                    Sequence[float]: The float values associated with the item.
        """
    def get_as_ints(self, item: sc.AbstractManipulatorItem):
        """
        Gets the integer values associated with a manipulator item.
        
                Args:
                    item (:obj:`sc.AbstractManipulatorItem`): The manipulator item whose values are to be retrieved.
        
                Returns:
                    Sequence[int]: The integer values associated with the item.
        """
    def get_da(self):
        """
        Retrieves the data accessor selector associated with the model.
        
                Returns:
                    :obj:`PrimDataAccessorSelector`: The data accessor selector.
        """
    def get_operation(self) -> Operation:
        """
        Gets the current operation of the model.
        
                Returns:
                    Operation: The current operation.
        """
    def get_pivot_prim_path(self) -> self._data_accessor_selector.Sdf.Path:
        """
        Gets the current pivot prim path.
        
                Returns:
                    :obj:`pxr.Sdf.Path`: The current pivot prim path.
        """
    def get_snap(self, item: AbstractTransformManipulatorModel.OperationItem):
        """
        Gets the snap settings for a manipulator item.
        
                Args:
                    item (:obj:`AbstractTransformManipulatorModel.OperationItem`): The manipulator item to get snap settings for.
        
                Returns:
                    Union[None, Sequence[float]]: The snap settings for the item.
        """
    def on_began(self, payload):
        """
        Handles the beginning of a transformation event.
        
                Args:
                    payload (Dict): The payload associated with the transform event.
        """
    def on_canceled(self, payload):
        """
        Handles the cancellation of a transformation event.
        
                Args:
                    payload (Dict): The payload associated with the transform event.
        """
    def on_changed(self, payload):
        """
        Handles changes during a transformation event.
        
                Args:
                    payload (Dict): The payload associated with the transform event.
        """
    def on_ended(self, payload):
        """
        Handles the end of a transformation event.
        
                Args:
                    payload (Dict): The payload associated with the transform event.
        """
    def on_selection_changed(self, selection: list[pxr.Sdf.Path]):
        """
        Handles updates to the selection of prims within the model.
        
                Args:
                    selection (List[:obj:`pxr.Sdf.Path`]): The new selection of Sdf Paths.
        """
    def set_floats(self, item: sc.AbstractManipulatorItem, value: typing.Sequence[float]):
        """
        Sets the float values for a given manipulator item.
        
                Args:
                    item (:obj:`sc.AbstractManipulatorItem`): The manipulator item to be updated.
                    value (Sequence[float]): The new float values to be set for the item.
        """
    def set_ints(self, item: sc.AbstractManipulatorItem, value: typing.Sequence[int]):
        """
        Sets the integer values for a given manipulator item.
        
                Args:
                    item (:obj:`sc.AbstractManipulatorItem`): The manipulator item to be updated.
                    value (Sequence[int]): The new integer values to be set for the item.
        """
    def set_pivot_prim_path(self, path0: self._data_accessor_selector.Sdf.Path) -> bool:
        """
        Sets the pivot prim path based on the provided path.
        
                Args:
                    path0 (:obj:`pxr.Sdf.Path`): The new pivot prim path.
        
                Returns:
                    bool: True if the pivot prim path was successfully set.
        """
    def update_selection(self):
        """
        Updates the selection state of the model.
        """
    def widget_disabled(self):
        """
        Notifies the model that a widget has been disabled.
        """
    def widget_enabled(self):
        """
        Notifies the model that a widget has been enabled.
        """
    @property
    def custom_manipulator_enabled(self):
        """
        Gets whether a custom manipulator is enabled.
        
                Returns:
                    bool: True if a custom manipulator is enabled, False otherwise.
        """
    @property
    def op_settings_listener(self):
        """
        Gets the operation settings listener instance.
        
                Returns:
                    :obj:`OpSettingsListener`: The operation settings listener object.
        """
    @property
    def snap_settings_listener(self):
        """
        Gets the snap settings listener instance.
        
                Returns:
                    :obj:`SnapSettingsListener`: The snap settings listener object.
        """
    @property
    def usd_context(self) -> omni.usd.UsdContext:
        """
        Gets the USD context for the prim transform model.
        
                Returns:
                    :obj:`UsdContext`: The USD context associated with the model.
        """
    @property
    def xformable_prim_paths(self) -> list[self._data_accessor_selector.Sdf.Path]:
        """
        Gets the list of transformable prim paths.
        
                Returns:
                    List[:obj:`Sdf.Path`]: The list of xformable prim paths.
        """
class PrimTranslateChangedGesture(omni.kit.viewport.manipulator.transform.gestures.ViewportTranslateChangedGesture):
    """
    A class that represents the gesture of translation change for a primitive in the viewport.
    
        This class extends the `ViewportTranslateChangedGesture` and is responsible for handling the translation change events
        when a primitive is manipulated in the viewport. It ensures the translation changes are properly reflected in the
        model representing the primitive's transform.
    """
    def _get_model(self, payload_type) -> PrimTransformModel:
        ...
PRINT_PERF_DATA: bool = True
TRANSFORM_GIZMO_CUSTOM_MANIPULATOR_ENABLED: str = '/app/transform/gizmoCustomManipulatorEnabled'
TRANSFORM_GIZMO_CUSTOM_MANIPULATOR_PRIMS: str = '/app/transform/gizmoCustomManipulatorPrims'
TRANSFORM_GIZMO_IS_USING: str = '/app/transform/gizmoIsUsing'
TRANSFORM_GIZMO_PIVOT_WORLD_POSITION: str = '/app/transform/tempPivotWorldPosition'
TRANSFORM_GIZMO_ROTATE_DELTA_XYZW: str = '/app/transform/gizmoRotateDeltaXYZW'
TRANSFORM_GIZMO_SCALE_DELTA_XYZ: str = '/app/transform/gizmoScaleDeltaXYZ'
TRANSFORM_GIZMO_TRANSLATE_DELTA_XYZ: str = '/app/transform/gizmoTranslateDeltaXYZ'
TRANSLATE_DELAY_FRAME_SETTING: str = '/exts/omni.kit.manipulator.prim.core/visual/delayFrame'
