"""
This module provides the PrimTransformManipulator class for interactive transformation of USD prims in a viewport.
"""
from __future__ import annotations
import carb as carb
import copy as copy
import omni as omni
from omni.kit.manipulator.prim.core.model import PrimRotateChangedGesture
from omni.kit.manipulator.prim.core.model import PrimScaleChangedGesture
from omni.kit.manipulator.prim.core.model import PrimTransformModel
from omni.kit.manipulator.prim.core.model import PrimTranslateChangedGesture
from omni.kit.manipulator.prim.core.toolbar_registry import get_toolbar_registry
from omni.kit.manipulator.selector.manipulator_base import ManipulatorBase
from omni.kit.manipulator.tool.snap.manager import SnapProviderManager
from omni.kit.manipulator.tool.snap import settings_constants as snap_c
from omni.kit.manipulator.transform.manipulator import TransformManipulator
from omni.kit.manipulator.transform.settings_constants import Constants as transform_c
from omni.kit.manipulator.transform.settings_listener import OpSettingsListener
from omni.kit.manipulator.transform.settings_listener import SnapSettingsListener
from omni.kit.manipulator.transform.style import get_default_style
from pxr import Sdf
from pxr import Usd
import pxr.Usd
from pxr import UsdGeom
import typing
__all__ = ['ManipulatorBase', 'OpSettingsListener', 'PrimRotateChangedGesture', 'PrimScaleChangedGesture', 'PrimTransformManipulator', 'PrimTransformModel', 'PrimTranslateChangedGesture', 'Sdf', 'SnapProviderManager', 'SnapSettingsListener', 'TRANSFORM_GIZMO_HIDDEN_OVERRIDE', 'TransformManipulator', 'Usd', 'UsdGeom', 'carb', 'copy', 'get_default_style', 'get_toolbar_registry', 'omni', 'snap_c', 'transform_c']
class PrimTransformManipulator(omni.kit.manipulator.selector.manipulator_base.ManipulatorBase):
    """
    A class responsible for creating and managing a transform manipulator for USD prims.
    
        This manipulator allows for the interactive transformation of prims within a USD stage via a viewport. It supports translation, rotation, and scaling operations both globally and locally. It also integrates with snapping tools for precise control over the transformations.
    
        Args:
            usd_context_name (str): The name of the USD context in which the manipulator will operate.
            viewport_api: The API for the viewport that the manipulator will interact with. If None, it indicates legacy mode.
            name (str): The name identifier for the manipulator instance.
            model (Optional[:obj:`PrimTransformModel`]): The data model that the manipulator will use to apply transformations. If None, a new model is created.
            size (float): The scale factor for the manipulator's visual representation in the viewport.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    def __del__(self):
        ...
    def __init__(self, usd_context_name: str = '', viewport_api = None, name = 'omni.kit.manipulator.prim.core', model: omni.kit.manipulator.prim.core.model.PrimTransformModel = None, size: float = 1.0):
        """
        Constructor for the PrimTransformManipulator class.
        """
    def _create_local_global_styles(self):
        ...
    def _on_op_listener_changed(self, type: omni.kit.manipulator.transform.settings_listener.OpSettingsListener.CallbackType, value: str):
        ...
    def _on_snap_listener_changed(self, setting_val_name: str, value: str):
        ...
    def _set_default_settings(self):
        ...
    def _set_style(self) -> None:
        ...
    def _update_manipulator_enable(self) -> None:
        ...
    def destroy(self):
        """
        Cleans up resources and internal data.
        """
    def on_selection_changed(self, stage: pxr.Usd.Stage, selection: typing.Optional[typing.List[pxr.Sdf.Path]], *args, **kwargs) -> bool:
        """
        Handles selection changes in the scene.
        
                Args:
                    stage (:obj:`Usd.Stage`): The stage where selection changed.
                    selection (Union[List[:obj:`Sdf.Path`], None]): The new selection list.
                    args: Variable length argument list.
        
                Keyword Args:
                    time (float): The timestamp of the selection event.
                    reason (str): The reason for the selection change.
        
                Returns:
                    bool: Whether selection change was handled.
        """
    @property
    def enabled(self):
        """
        Gets the current enabled state of the manipulator.
        
                Returns:
                    bool: The current enabled state.
        """
    @enabled.setter
    def enabled(self, value: bool):
        """
        Sets the enabled state of the manipulator.
        
                Args:
                    value (bool): The new enabled state to set.
        """
    @property
    def model(self) -> omni.kit.manipulator.prim.core.model.PrimTransformModel:
        """
        Gets the PrimTransformModel associated with this manipulator.
        
                Returns:
                    :obj:`PrimTransformModel`: The model used by the manipulator.
        """
    @property
    def snap_manager(self) -> omni.kit.manipulator.tool.snap.manager.SnapProviderManager:
        """
        Gets the SnapProviderManager for this manipulator.
        
                Returns:
                    :obj:`SnapProviderManager`: The snap manager used by the manipulator.
        """
TRANSFORM_GIZMO_HIDDEN_OVERRIDE: str = '/app/transform/gizmoHiddenOverride'
