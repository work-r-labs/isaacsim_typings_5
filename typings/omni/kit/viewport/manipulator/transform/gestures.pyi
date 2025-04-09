from __future__ import annotations
import asyncio as asyncio
import carb as carb
import concurrent as concurrent
from enum import Enum
from enum import Flag
from enum import IntEnum
from enum import auto
import math as math
import omni as omni
from omni.kit.async_engine.async_engine import run_coroutine
from omni.kit.manipulator.tool.snap.manager import SnapProviderManager
from omni.kit.manipulator.transform.gestures import RotateChangedGesture
from omni.kit.manipulator.transform.gestures import RotateDragGesturePayload
from omni.kit.manipulator.transform.gestures import ScaleChangedGesture
from omni.kit.manipulator.transform.gestures import ScaleDragGesturePayload
from omni.kit.manipulator.transform.gestures import TransformDragGesturePayload
from omni.kit.manipulator.transform.gestures import TranslateChangedGesture
from omni.kit.manipulator.transform.gestures import TranslateDragGesturePayload
from omni.kit.manipulator.transform.settings_constants import Constants as transform_c
from omni.kit.manipulator.transform.types import Operation
from omni.kit.viewport.manipulator.transform.model import ManipulationMode
from omni.kit.viewport.manipulator.transform.model import Viewport1WindowState
from omni.kit.viewport.manipulator.transform.model import ViewportTransformModel
from omni.kit.viewport.manipulator.transform.utils import flatten
from omni.ui import scene as sc
import traceback as traceback
from usdrt import Gf
__all__: list = ['ViewportTransformChangedGestureBase', 'ViewportTranslateChangedGesture', 'ViewportRotateChangedGesture', 'ViewportScaleChangedGesture']
class ViewportRotateChangedGesture(omni.kit.manipulator.transform.gestures.RotateChangedGesture, ViewportTransformChangedGestureBase):
    """
    A class for handling rotation change gestures within a viewport.
    
        This class is responsible for managing the beginning, ongoing changes, and ending of rotation gestures applied to objects in the viewport. It extends the functionality of RotateChangedGesture and ViewportTransformChangedGestureBase.
    
        Keyword Args:
            usd_context_name (str): The name of the USD context.
            viewport_api: The API for the viewport.
        
    """
    @staticmethod
    def on_changed(*args, **kwds):
        """
        Handle changes during the rotation gesture.
        
                Args:
                    args: Arguments for the rotation gesture.
        
                Keyword Args:
                    payload_type (type): The type of the payload for the gesture.
                    axis (list): The axis of rotation.
                    angle (float): The angle of rotation.
                    angle_delta (float): The change in angle.
                    screen_space (bool): Whether the rotation is in screen space.
                    free_rotation (bool): Whether the rotation is free-form.
                
        """
    def __init__(self, **kwargs):
        """
        Initialize the ViewportRotateChangedGesture instance.
        """
    def on_began(self):
        """
        Handle the beginning of the rotation gesture.
        """
    def on_canceled(self):
        """
        Handle the cancellation of the rotation gesture.
        """
    def on_ended(self):
        """
        Handle the end of the rotation gesture.
        """
class ViewportScaleChangedGesture(omni.kit.manipulator.transform.gestures.ScaleChangedGesture, ViewportTransformChangedGestureBase):
    """
    A class for handling viewport scale change gestures.
    
        This class manages the initiation, updates, and termination of scale change gestures in the viewport. It integrates with the ViewportTransformChangedGestureBase class and the ScaleChangedGesture class to provide comprehensive gesture handling for scaling operations.
    
        Keyword Args:
            usd_context_name (str): The name of the USD context.
            viewport_api (object): The viewport API instance.
        
    """
    @staticmethod
    def on_changed(*args, **kwds):
        """
        Handles changes during the scale change gesture.
        
                Args:
                    args (list): List of arguments.
        
                Keyword Args:
                    payload_type (type): The type of the gesture payload.
                
        """
    def __init__(self, **kwargs):
        """
        Initializes the ViewportScaleChangedGesture.
        """
    def on_began(self):
        """
        Handles the beginning of the scale change gesture.
        """
    def on_canceled(self):
        """
        Handles the cancellation of the scale change gesture.
        """
    def on_ended(self):
        """
        Handles the ending of the scale change gesture.
        """
class ViewportTransformChangedGestureBase:
    """
    A base class for viewport transform changed gestures.
    
        This class provides the foundational functionality for handling changes in viewport transforms, including translating, rotating, and scaling gestures. It interacts with the USD context and viewport API to manage transformation operations and update the viewport accordingly.
    
        Args:
            usd_context_name (str): The name of the USD context to be used for the transformations.
            viewport_api: The API of the viewport to be manipulated.
        
    """
    def _ViewportTransformChangedGestureBase__set_viewport_manipulating(self, value: int):
        ...
    def __init__(self, usd_context_name: str = '', viewport_api = None):
        """
        Initializes the ViewportTransformChangedGestureBase class.
        """
    def _publish_delta(self, operation: Operation, delta: list[float]):
        ...
    def _viewport_on_began(self):
        ...
    def _viewport_on_ended(self):
        ...
    def on_began(self, payload_type = omni.kit.manipulator.transform.gestures.TransformDragGesturePayload):
        """
        Handles the beginning of a gesture.
        
                Args:
                    payload_type (type): Type of the payload for the gesture.
                
        """
    def on_canceled(self, payload_type = omni.kit.manipulator.transform.gestures.TransformDragGesturePayload):
        """
        Handles the cancellation of a gesture.
        
                Args:
                    payload_type (type): Type of the payload for the gesture.
                
        """
    def on_changed(self, payload_type = omni.kit.manipulator.transform.gestures.TransformDragGesturePayload):
        """
        Handles changes during a gesture.
        
                Args:
                    payload_type (type): Type of the payload for the gesture.
                
        """
    def on_ended(self, payload_type = omni.kit.manipulator.transform.gestures.TransformDragGesturePayload):
        """
        Handles the end of a gesture.
        
                Args:
                    payload_type (type): Type of the payload for the gesture.
                
        """
class ViewportTranslateChangedGesture(omni.kit.manipulator.transform.gestures.TranslateChangedGesture, ViewportTransformChangedGestureBase):
    """
    A class for handling translation gestures in a viewport.
    
        This class extends the TranslateChangedGesture and ViewportTransformChangedGestureBase classes to provide
        functionality for handling translation gestures within a viewport environment. It supports snapping and
        delta publications for translation operations.
    
        Args:
            snap_manager (SnapProviderManager): Manages snapping behavior during translation.
    
        Keyword Args:
            usd_context_name (str): Name of the USD context.
            viewport_api: API for interacting with the viewport.
        
    """
    @staticmethod
    def on_changed(*args, **kwds):
        """
        Handles changes during a translate gesture.
        
                Args:
                    args: Arguments for the gesture change event.
        
                Keyword Args:
                    key1 (type): Description of key1.
                    key2 (type): Description of key2.
                
        """
    def __init__(self, snap_manager: SnapProviderManager, **kwargs):
        """
        Initializes the ViewportTranslateChangedGesture class.
        """
    def _can_snap(self, model: ViewportTransformModel):
        ...
    def _get_model(self, payload_type) -> ViewportTransformModel:
        ...
    def on_began(self):
        """
        Handles the beginning of a translate gesture.
        """
    def on_canceled(self):
        """
        Handles the cancellation of a translate gesture.
        """
    def on_ended(self):
        """
        Handles the end of a translate gesture.
        """
