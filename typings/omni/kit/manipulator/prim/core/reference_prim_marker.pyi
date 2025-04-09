"""
This module defines classes for managing gestures and manipulators related to reference primitive markers in USD stages within the Omniverse Kit.
"""
from __future__ import annotations
import asyncio as asyncio
import carb as carb
from collections import defaultdict
import colorsys as colorsys
import concurrent as concurrent
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.manipulator.prim.core.model import PrimTransformModel
from omni.kit.manipulator.prim.core.settings_constants import Constants
from omni.kit.manipulator.prim.core.utils import flatten
from omni.kit.manipulator.transform.settings_constants import Constants as TrCon
from omni.kit.manipulator.transform.style import abgr_to_color
from omni.kit.viewport.manipulator.transform.model import Viewport1WindowState
from omni.ui import scene as sc
from pxr import Sdf
from pxr import Tf
from pxr import Usd
from pxr import UsdGeom
import weakref as weakref
from weakref import ProxyType
__all__ = ['COLOR_X', 'COLOR_Y', 'COLOR_Z', 'ClickMarkerGesture', 'Constants', 'LARGE_SELECTION_CAP', 'MarkerHoverGesture', 'PreventViewportOthers', 'PrimTransformModel', 'ProxyType', 'ReferencePrimMarker', 'Sdf', 'Tf', 'TrCon', 'Usd', 'UsdGeom', 'Viewport1WindowState', 'abgr_to_color', 'asyncio', 'carb', 'cl', 'colorsys', 'concurrent', 'defaultdict', 'flatten', 'omni', 'run_coroutine', 'sc', 'weakref']
class ClickMarkerGesture(omni.ui_scene._scene.DragGesture):
    """
    A gesture class for handling click-to-mark operations on 3D markers in a viewport.
    
        This class extends the sc.DragGesture class to implement specific behavior for clicking on 3D markers that represent points of interest in a scene. It is typically used in the context of a 3D editing application to allow users to select or manipulate reference points on 3D primitives.
    
        Args:
            prim_path (:obj:`Sdf.Path`): The USD path to the primitive associated with the marker.
            marker (ProxyType[:obj:`ReferencePrimMarker`]): A weak proxy reference to the associated ReferencePrimMarker instance.
        
    """
    def __init__(self, prim_path: Sdf.Path, marker: ProxyType[ReferencePrimMarker]):
        """
        Initializes a ClickMarkerGesture instance.
        """
    def _viewport_on_began(self):
        ...
    def _viewport_on_ended(self):
        ...
    def on_began(self):
        """
        Called when the gesture begins.
        """
    def on_canceled(self):
        """
        Called when the gesture is canceled.
        """
    def on_ended(self):
        """
        Called when the gesture ends.
        """
class MarkerHoverGesture(omni.ui_scene._scene.HoverGesture):
    """
    A class representing a hover gesture over markers in a 3D viewport.
    
        This class manages hover interactions with visual markers, such as lines and arcs, making them brighter when hovered over. It tracks the beginning and ending of hover gestures, adjusting the visual representation of items to indicate active hover states.
    
        Args:
            args: Variable length argument list.
    
        Keyword Args:
            Any additional keyword arguments.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor method for MarkerHoverGesture.
        
                This method does not need a detailed description.
        """
    def _make_brighter(self, color):
        ...
    def on_began(self):
        """
        Callback for when the hover gesture begins with no additional interactions.
        """
    def on_ended(self):
        """
        Callback for when the hover gesture ends with no additional interactions.
        """
class PreventViewportOthers(omni.ui_scene._scene.GestureManager):
    """
    A class that provides gesture management capabilities to prevent viewport interactions from being blocked by other gestures.
    
        This class is designed to work within a viewport context, determining if certain gestures should be prevented based on the state and type of other gestures that are currently active. It primarily focuses on enhancing user interaction with the viewport by ensuring that more critical gestures take precedence and are not hindered by others. The class achieves this through its methods `can_be_prevented` and `should_prevent`, which assess and decide whether a gesture should be allowed to continue or be prevented in favor of another.
    
        The class inherits from `sc.GestureManager`, leveraging its capabilities to manage and prioritize gestures within the viewport.
        
    """
    def can_be_prevented(self, gesture):
        """
        Determines if the gesture can be prevented.
        
                Args:
                    gesture (:obj:`sc.Gesture`): The gesture to be evaluated for prevention.
        
                Returns:
                    bool: True if the gesture can be prevented, otherwise False.
        """
    def should_prevent(self, gesture, preventer):
        """
        Decides if an ongoing gesture should be prevented by another gesture.
        
                Args:
                    gesture (:obj:`sc.Gesture`): The ongoing gesture to be evaluated.
                    preventer (:obj:`sc.Gesture`): The gesture that might prevent the ongoing one.
        
                Returns:
                    bool: True if the ongoing gesture should be prevented, otherwise False.
        """
class ReferencePrimMarker(omni.ui_scene._scene.Manipulator):
    """
    A class representing a manipulator for reference primitive markers in USD stages.
    
        This manipulator visually represents selectable primitives in a 3D scene and allows users to pick a reference primitive as a pivot for transformations using a custom gesture. It is a subclass of `sc.Manipulator` and provides a custom user interface in the viewport.
    
        Args:
            usd_context_name (str): The name of the USD context to operate within. An empty string will use the default context.
            manipulator_model (Optional[:obj:`ProxyType[PrimTransformModel]`]): The data model used by the manipulator for transformations. If `None`, no model is used.
            legacy (bool): A flag indicating whether to use legacy behavior. Defaults to `False`.
    
        The manipulator listens to USD stage events, timeline changes, and selection changes to update its state and appearance in the viewport. It also handles custom gestures for user interaction with the viewport markers.
        
    """
    @staticmethod
    def _on_objects_changed(*args, **kwds):
        ...
    @staticmethod
    def _process_pending_change(*args, **kwargs):
        ...
    def __init__(self, usd_context_name: str = '', manipulator_model: ProxyType[PrimTransformModel] = None, legacy: bool = False):
        """
        Initializes a new instance of the ReferencePrimMarker.
        """
    def _get_current_time_code(self):
        ...
    def _on_op_changed(self, item, event_type):
        ...
    def _on_placement_changed(self, item, event_type):
        ...
    def _on_selection_changed(self):
        ...
    def _on_stage_event(self, event: carb.events.IEvent):
        ...
    def _on_timeline_event(self, e: carb.events.IEvent):
        ...
    def destroy(self):
        """
        Cleans up resources and subscriptions.
        """
    def on_build(self):
        """
        Builds or rebuilds the ReferencePrimMarker.
        """
    def on_pivot_marker_picked(self, path: Sdf.Path):
        """
        Handles the event when a pivot marker is picked.
        
                Args:
                    path (:obj:`Sdf.Path`): The path of the picked pivot marker.
        """
    @property
    def legacy(self) -> bool:
        """
        Gets the legacy mode state.
        
                Returns:
                    bool: True if legacy mode is enabled, false otherwise.
        """
    @legacy.setter
    def legacy(self, value):
        """
        Sets the legacy mode.
        
                Args:
                    value (bool): If true, enables legacy mode.
        """
    @property
    def manipulator_model(self) -> ProxyType[PrimTransformModel]:
        """
        Gets the manipulator model.
        
                Returns:
                    :obj:`ProxyType[PrimTransformModel]`: The current manipulator model.
        """
    @manipulator_model.setter
    def manipulator_model(self, value):
        """
        Sets the manipulator model.
        
                Args:
                    value (:obj:`ProxyType[PrimTransformModel]`): The manipulator model.
        """
    @property
    def usd_context_name(self) -> str:
        """
        Gets the USD context name.
        
                Returns:
                    str: The current USD context name.
        """
    @usd_context_name.setter
    def usd_context_name(self, value: str):
        """
        Sets the USD context name.
        
                Args:
                    value (str): The name of the USD context.
        """
COLOR_X: int = 4284506282
COLOR_Y: int = 4285965169
COLOR_Z: int = 4288707919
LARGE_SELECTION_CAP: int = 20
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
