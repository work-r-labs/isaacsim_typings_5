from __future__ import annotations
import carb as carb
from collections import defaultdict
import omni as omni
from omni.kit.manipulator.transform.gestures import DummyClickGesture
from omni.kit.manipulator.transform.gestures import DummyGesture
from omni.kit.manipulator.transform.gestures import HighlightControl
from omni.kit.manipulator.transform.gestures import HighlightGesture
from omni.kit.manipulator.transform.gestures import RotationGesture
from omni.kit.manipulator.transform.gestures import ScaleGesture
from omni.kit.manipulator.transform.gestures import TranslateGesture
from omni.kit.manipulator.transform.settings_constants import Constants as c
from omni.kit.manipulator.transform.simple_transform_model import SimpleTransformModel
from omni.kit.manipulator.transform.style import abgr_to_color
from omni.kit.manipulator.transform.style import get_default_style
from omni.kit.manipulator.transform.style import get_default_toolbar_style
from omni.kit.manipulator.transform.style import update_style
from omni.kit.manipulator.transform.types import Axis
from omni.kit.manipulator.transform.types import Operation
from omni import ui
from omni.ui import scene as sc
from pathlib import Path
import typing
import weakref as weakref
from weakref import ProxyType
__all__ = ['ARROW_HEIGHT', 'ARROW_P', 'ARROW_VC', 'ARROW_VI', 'ARROW_WIDTH', 'Axis', 'DummyClickGesture', 'DummyGesture', 'HighlightControl', 'HighlightGesture', 'LINE_THICKNESS', 'Operation', 'Path', 'ProxyType', 'RotationGesture', 'ScaleGesture', 'SimpleTransformModel', 'TOOLBAR_WIDGET_HEIGHT', 'TransformManipulator', 'TranslateGesture', 'abgr_to_color', 'c', 'carb', 'cl', 'defaultdict', 'get_default_style', 'get_default_toolbar_style', 'omni', 'sc', 'ui', 'update_style', 'weakref']
class TransformManipulator(omni.ui_scene._scene.Manipulator):
    """
    A manipulator for transforming objects in 3D space.
    
        This manipulator is used to interactively translate, rotate, and scale objects within a 3D scene
        using various gizmos and widgets. It can be customized with different models, styles, and gestures.
    
        Args:
            size (float): The initial size of the manipulator, affecting its visual representation.
            enabled (bool): If False, the manipulator will be created but disabled (invisible).
            axes (Axis): Specifies which axes to enable for the manipulator. Use this to create 2D or 1D manipulators.
            model (AbstractTransformManipulatorModel): The model for the manipulator. If None, a default SimpleTransformModel will be created.
            style (Dict): Overrides the default style of the manipulator.
            gestures (List[sc.ManipulatorGesture]): The list of gestures associated with the manipulator.
            tool_registry (ToolbarRegistry): The registry holding the toolbar tools associated with the manipulator.
            tool_button_additional_payload (Dict[str, Any]): Additional payload to be passed into the toolbar's context menu.
            tools_default_collapsed (bool | None): Determines whether the toolbar should be collapsed by default.
    """
    def __del__(self):
        """
        Releases all resources and subscriptions of the TransformManipulator on deletion.
        """
    def __init__(self, size: float = 1.0, enabled: bool = True, axes: Axis = ..., model: AbstractTransformManipulatorModel = None, style: dict = {}, gestures: list[sc.ManipulatorGesture] = list(), tool_registry: ToolbarRegistry = None, tool_button_additional_payload: dict[str, typing.Any] = {}, tools_default_collapsed: bool | None = None):
        """
        Initializes a new instance of the TransformManipulator.
        """
    def _build_tools_widgets(self, root: sc.Transform):
        """
        Internally builds the tools widgets for the TransformManipulator.
        """
    def _create_rotation_manipulator(self):
        """
        Internally creates the rotation manipulator components within the TransformManipulator's structure.
        """
    def _create_scale_manipulator(self):
        """
        Internally creates the scale manipulator components within the TransformManipulator's structure.
        """
    def _create_toolbar(self):
        """
        Internally creates the toolbar components within the TransformManipulator's structure.
        """
    def _create_translate_manipulator(self):
        """
        Internally creates the translation manipulator components within the TransformManipulator's structure
        """
    def _get_final_size(self):
        """
        Calculates the final size of the TransformManipulator based on its scale setting.
        
                Returns:
                    float: The calculated final size of the TransformManipulator.
        """
    def _get_toolbar_height_offset(self):
        """
        Calculates the height offset for the toolbar based on the current size of the TransformManipulator.
        
                Returns:
                    float: The calculated height offset for the toolbar.
        """
    def _on_free_rotation_enabled_changed(self, item, event_type):
        """
        Callback for when the free rotation setting for the TransformManipulator changes.
        """
    def _on_intersection_thickness_changed(self, item, event_type):
        """
        Callback for when the intersection thickness setting for the TransformManipulator changes.
        """
    def _on_scale_changed(self, item, event_type):
        """
        Callback for when the scale setting for the TransformManipulator changes.
        """
    def _on_toolbar_changed(self):
        """
        Callback for when the ToolbarRegistry associated with the TransformManipulator changes.
        """
    def _update_axes_visibility(self):
        """
        Updates the visibility of various axes components based on the axes settings for the TransformManipulator.
        """
    def _update_from_model(self):
        """
        Updates the TransformManipulator's visual representation based on its model.
        """
    def _update_manipulator_final_size(self):
        """
        Updates the visual size of the TransformManipulator based on its scale setting.
        """
    def destroy(self):
        """
        Cleanly destroys the TransformManipulator, unsubscribing from all settings and destroying tools.
        """
    def on_build(self):
        """
        Builds the TransformManipulator's structure representation. Should be called within a SceneView.scene scope if build_items_on_init is set to False.
        """
    def on_model_updated(self, item):
        """
        Callback for when the model associated with the TransformManipulator is updated.
        """
    def refresh_toolbar(self):
        """
        Refreshes the toolbar, forcing it to redraw.
        """
    @property
    def axes(self) -> float:
        """
        Gets the enabled axes for the TransformManipulator.
        
                Returns:
                    Axis: The enabled axes of the TransformManipulator.
        """
    @axes.setter
    def axes(self, value: float):
        """
        Sets the enabled axes for the TransformManipulator.
        """
    @property
    def enabled(self) -> bool:
        """
        Gets the enabled state of the TransformManipulator.
        
                Returns:
                    bool: The enabled state of the TransformManipulator.
        """
    @enabled.setter
    def enabled(self, value: bool):
        """
        Sets the enabled state of the TransformManipulator.
        """
    @property
    def model(self) -> AbstractManipulatorModel:
        """
        Returns the current model.
        """
    @model.setter
    def model(self, model):
        ...
    @property
    def size(self) -> float:
        """
        Gets the size of the TransformManipulator.
        
                Returns:
                    float: The current size of the TransformManipulator.
        """
    @size.setter
    def size(self, value: float):
        """
        Sets the size of the TransformManipulator.
        """
    @property
    def style(self) -> dict:
        """
        Gets the style dictionary for the TransformManipulator.
        
                Returns:
                    Dict: The current style settings of the TransformManipulator.
        """
    @style.setter
    def style(self, value: dict):
        """
        Sets the style dictionary for the TransformManipulator.
        """
    @property
    def tool_registry(self) -> ToolbarRegistry:
        """
        Gets the ToolbarRegistry associated with the TransformManipulator.
        
                Returns:
                    ToolbarRegistry: The current ToolbarRegistry associated with the TransformManipulator.
        """
    @tool_registry.setter
    def tool_registry(self, value: ToolbarRegistry):
        """
        Sets the ToolbarRegistry associated with the TransformManipulator.
        """
    @property
    def toolbar_visible(self) -> bool:
        """
        Gets the visibility state of the TransformManipulator's toolbar.
        
                Returns:
                    bool: Whether the toolbar is currently visible.
        """
    @toolbar_visible.setter
    def toolbar_visible(self, value: bool):
        """
        Sets the visibility state of the TransformManipulator's toolbar.
        """
ARROW_HEIGHT: int = 14
ARROW_P: list = [[4, 4, 0], [-4, 4, 0], [0, 0, 14], [4, -4, 0], [-4, -4, 0], [0, 0, 14], [4, 4, 0], [4, -4, 0], [0, 0, 14], [-4, 4, 0], [-4, -4, 0], [0, 0, 14], [4, 4, 0], [-4, 4, 0], [-4, -4, 0], [4, -4, 0]]
ARROW_VC: list = [3, 3, 3, 3, 4]
ARROW_VI: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
ARROW_WIDTH: int = 4
LINE_THICKNESS: int = 2
TOOLBAR_WIDGET_HEIGHT: int = 114
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
