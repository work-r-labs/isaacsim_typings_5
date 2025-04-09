from __future__ import annotations
import carb as carb
import collections
from collections import defaultdict
import copy as copy
import dataclasses
from dataclasses import dataclass
from functools import lru_cache
import math as math
import numpy as np
from omni.kit.manipulator.transform.settings_constants import Constants as CONSTANTS
import omni.ui.color_utils
from omni.ui import scene as sc
import omni.ui_scene._scene
import typing
__all__ = ['CONSTANTS', 'DummyClickGesture', 'DummyGesture', 'HighlightControl', 'HighlightGesture', 'HoverDepthTest', 'PreventOthers', 'RotateChangedGesture', 'RotateDragGesturePayload', 'RotationGesture', 'ScaleChangedGesture', 'ScaleDragGesturePayload', 'ScaleGesture', 'TransformChangedGesture', 'TransformDragGesturePayload', 'TransformGesture', 'TranslateChangedGesture', 'TranslateDragGesturePayload', 'TranslateGesture', 'carb', 'cl', 'copy', 'dataclass', 'defaultdict', 'lru_cache', 'math', 'np', 'sc']
class DummyClickGesture(omni.ui_scene._scene.ClickGesture):
    """
    A gesture used to prevent viewport click interactions.
    
        This gesture is used to block other gestures in the viewport, such as right-clicking on a manipulator toolbar to prevent triggering the viewport context menu.
    
        Args:
            mouse_button: int
                The mouse button associated with the click gesture.
    """
    def __init__(self, mouse_button: int):
        """
        Initializes the DummyClickGesture with a specified mouse button.
        """
    @property
    def order(self):
        """
        The order property of the DummyClickGesture.
        
                Returns:
                    int: The priority order of the gesture.
        """
class DummyGesture(TransformGesture):
    """
    A gesture used internally to prevent viewport interactions.
    
        This gesture is not associated with any visual manipulator elements; its primary function is to emit TransformChangedGesture events to disable selection rectangles in the viewport and prevent other gestures from being recognized when certain manipulator-related conditions are met.
    
        Args:
            manipulator (TransformManipulator): The manipulator associated with the gesture.
        
    """
    def __init__(self, manipulator: TransformManipulator):
        """
        Initializes the DummyGesture with a given manipulator.
        """
    def _on_began(self):
        """
        Handler called when the dummy gesture begins. Processes a TransformChangedGesture to prevent viewport interaction.
        """
    def _on_canceled(self):
        """
        Handler called when the dummy gesture is canceled. Behaves like the end handler.
        """
    def _on_changed(self):
        """
        Handler for when the dummy gesture state changes. No implementation required.
        """
    def _on_ended(self):
        """
        Handler called when the dummy gesture ends. Processes a TransformChangedGesture to resume viewport interaction.
        """
class HighlightControl:
    """
    A control for highlighting manipulator widgets during interaction.
    
        When an interaction with a manipulator widget begins, the HighlightControl is responsible for changing the color of the widget to indicate its highlighted state. Once the interaction ends, the original color is restored. This class supports highlighting the same widget from multiple triggers simultaneously.
    
        Args:
            items: List[sc.AbstractManipulatorItem], optional
                A list of manipulator items to track highlighting for.
            color: cl.Color, optional
                The color used for highlighting.
    """
    _HighlightControl__original_colors: typing.ClassVar[dict] = {}
    _HighlightControl__status_tracker: typing.ClassVar[collections.defaultdict]  # value = defaultdict(<class 'int'>, {})
    def __init__(self, items = None, color = None):
        """
        Initializes a HighlightControl instance. 
        """
    def _dehighlight(self, item):
        """
        Restores the original color of the specified item.
        
                Args:
                    item (sc.AbstractManipulatorItem): The item to restore the original color to.
        """
    def _highlight(self, item):
        """
        Applies the highlight color to the specified item.
        
                Args:
                    item (sc.AbstractManipulatorItem): The item to apply the highlight color to.
        """
    def dehighlight(self, sender):
        """
        Removes the highlight from the given sender or all items managed by this control.
        
                Args:
                    sender (sc.AbstractManipulatorItem): The item to dehighlight.
        """
    def highlight(self, sender):
        """
        Highlights the given sender or all items managed by this control.
        
                Args:
                    sender (sc.AbstractManipulatorItem): The item to highlight.
        """
class HighlightGesture(omni.ui_scene._scene.HoverGesture):
    """
    A gesture for highlighting UI elements during interaction.
    
        This gesture is responsible for changing the appearance of UI elements, such as manipulator widgets,
        to visually signify that they are being interacted with. It uses a HighlightControl instance to manage
        the highlight state and ensures the correct visual feedback is provided to the user based on the gesture's life cycle.
    
        Args:
            HighlightControl: HighlightControl
                The control responsible for managing highlights.
            order: int
                The priority order of the gesture, used for conflict resolution. Defaults to 0.
        
    """
    def __init__(self, highlight_ctrl: HighlightControl, order: int = 0):
        """
        Initializes the HighlightGesture with a given HighlightControl and optional order. 
        """
    def _on_began(self):
        """
        Handles the initiation of the gesture, causing the associated manipulator widget to be highlighted.
        """
    def _on_canceled(self):
        """
        Handles the cancellation of the gesture, removing the highlight if it had been applied.
        """
    def _on_changed(self):
        """
        Handles changes to the gesture state.
        """
    def _on_ended(self):
        """
        Handles the end of the gesture, removing the highlight from the associated manipulator widget.
        """
    def _on_prevented(self):
        """
        Handles the gesture being prevented, removing the highlight if it had been applied.
        """
    def process(self):
        """
        Processes the gesture, updating its state and handling highlighting based on interaction.
        """
    @property
    def order(self) -> int:
        """
        The order property of the HighlightGesture.
        
                Returns:
                    int: The priority order of the gesture.
        """
class HoverDepthTest(omni.ui_scene._scene.GestureManager):
    """
    A manager that performs a depth test for hover gestures.
    
        The hover gesture with the smaller order is given priority. If they have same order, gesture with smaller ray distance (closer to the camera) is given priority.
        
    """
    def can_be_prevented(self, gesture):
        """
        Determines if a hover gesture can be prevented based on its type.
        
                Args:
                    gesture (sc.AbstractGesture): The gesture to be evaluated.
        
                Returns:
                    bool: True if the gesture is an instance of HighlightGesture, otherwise False.
        """
    def should_prevent(self, gesture, preventer):
        """
        Decides if a hover gesture should be prevented based on its state, type, and depth.
        
                Args:
                    gesture (sc.AbstractGesture): The gesture that may be prevented.
                    preventer (sc.AbstractGesture): The gesture attempting to prevent the other gesture.
        
                Returns:
                    bool: True if the gesture should be prevented, otherwise False.
        """
class PreventOthers(omni.ui_scene._scene.GestureManager):
    """
    A gesture manager that makes TransformGesture the priority gesture over others.
    
        This manager ensures that TransformGesture takes precedence, preventing other gestures
        from being recognized when TransformGesture is active and certain conditions are met.
    """
    def can_be_prevented(self, gesture):
        """
        Determines if a gesture can be prevented.
        
                Args:
                    gesture (sc.AbstractGesture): The gesture to be evaluated.
        
                Returns:
                    bool: True if the gesture can be prevented, otherwise False.
        """
    def should_prevent(self, gesture, preventer):
        """
        Decides if a gesture should be prevented based on its state and type.
        
                Args:
                    gesture (sc.AbstractGesture): The gesture that may be prevented.
                    preventer (sc.AbstractGesture): The gesture attempting to prevent the other gesture.
        
                Returns:
                    bool: True if the gesture should be prevented, otherwise False.
        """
class RotateChangedGesture(TransformChangedGesture):
    """
    A gesture representing a change in rotation during an interaction with a manipulator.
    
        This gesture is used internally to handle manipulator interactions in a omni.ui.scene.SceneView for rotation operations. It is part of the gesture system that responds to the beginning, modification, ending, or canceling of a rotation action and is responsible for updating the state of the transformation and optionally blocking other omni.ui.scene.SceneView interactions while active.
        
    """
class RotateDragGesturePayload(TransformDragGesturePayload):
    """
    A payload class used for rotation drag gestures within the Transform manipulator.
    
        This class encapsulates the properties of a rotation operation as it is being performed, such as the rotation axis, the incremental angle change, and the total angle rotated.
        
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'axis': Field(name='axis',type='Sequence[float]',default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'angle_delta': Field(name='angle_delta',type='float',default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'angle': Field(name='angle',type='float',default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'screen_space': Field(name='screen_space',type='bool',default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'free_rotation': Field(name='free_rotation',type='bool',default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=False,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('axis', 'angle_delta', 'angle', 'screen_space', 'free_rotation')
    def __eq__(self, other):
        ...
    def __repr__(self):
        ...
class RotationGesture(TransformGesture):
    """
    A gesture class used for rotating objects in a 3D scene around a specified axis or freely without constraints.
    
        This class handles input related to object rotation and interacts with a manipulator and highlight control to provide visual feedback and manage the rotation behavior.
    
        Attributes:
            manipulator: TransformManipulator
                The manipulator associated with this gesture.
            axis: Sequence[int] | None
                The axis around which the object is rotated, or None for free rotation.
            viz_arc: sc.Arc
                The visual representation of the rotation arc.
            highlight_ctrl: HighlightControl
                The control responsible for managing highlights.
            order: int
                The priority order of the gesture, used for conflict resolution.
    """
    def __init__(self, manipulator: TransformManipulator, axis: typing.Sequence[int] | None, viz_arc: sc.Arc, highlight_ctrl: HighlightControl, order: int = 0):
        """
        Initializes the RotationGesture with a given manipulator, rotation axis, visualization arc, highlight control, order, and additional arguments.
        """
    def _handle_free_rotation(self) -> tuple[list[float], float]:
        """
        Handles the free rotation mode when the user interacts with the center of the rotation manipulator. Computes the axis and angle of rotation based on the current mouse position and manipulator orientation.
        
                Returns:
                    Tuple[List[float], float]: A tuple containing the rotation axis and the angle delta for the rotation gesture.
                
        """
    def _on_began(self):
        """
        Handler called when the rotation gesture begins. Sets up the necessary state for the rotation operation.
        """
    def _on_canceled(self):
        """
        Handler called when the rotation gesture is canceled. Reverts any changes made during the rotation.
        """
    def _on_changed(self):
        """
        Handler called when the rotation gesture state changes. Computes and applies the rotation delta.
        """
    def _on_ended(self):
        """
        Handler called when the rotation gesture ends. Finalizes the rotation and restores states.
        """
    def _sphere_intersect(self) -> tuple[list[float], bool]:
        """
        Computes the intersection point of a ray with a sphere representing the rotation manipulator, or the nearest point on the ray to the sphere if no intersection occurs.
        
                Returns:
                    Tuple[List[float], bool]: A tuple containing the intersection or nearest point in world coordinates, and a boolean indicating whether the ray intersected the sphere.
                
        """
    def process(self):
        """
        Processes the rotation gesture, taking into account the state of the arc and whether it's culled based on its orientation.
        """
class ScaleChangedGesture(TransformChangedGesture):
    """
    A gesture representing a change in scaling during an interaction with a manipulator.
    
        This gesture is used internally to handle manipulator interactions in a omni.ui.scene.SceneView for scaling operations. It is part of the gesture system that responds to the beginning, modification, ending, or canceling of a scaling action and is responsible for updating the state of the transformation and optionally blocking other omni.ui.scene.SceneView interactions while active.
        
    """
class ScaleDragGesturePayload(TransformDragGesturePayload):
    """
    A payload class used for drag gestures related to scaling operations.
    
        This class contains information about the scaling factors and the axis along which objects are being scaled during drag gestures.
        
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'axis': Field(name='axis',type='Sequence[float]',default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'scale': Field(name='scale',type='Sequence[float]',default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=False,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('axis', 'scale')
    def __eq__(self, other):
        ...
    def __repr__(self):
        ...
class ScaleGesture(TransformGesture):
    """
    A gesture class used for scaling objects in a 3D scene.
    
        This class handles input related to resizing objects along specific axes or uniformly from the center in the scene. It integrates with a manipulator and a highlight control to provide interactive feedback and manage the scaling transformation.
    
        Attributes:
            manipulator: TransformManipulator
                The manipulator associated with this gesture.
            axis: Sequence[int]
                The axis along which the object is being scaled.
            highlight_ctrl: HighlightControl
                The control responsible for managing highlights.
            handle_lines: List[sc.Line], optional
                Lines representing the scaling handles.
            handle_dots: List[sc.Arc], optional
                Dots representing the scaling points.
            order: int
                The priority order of the gesture, used for conflict resolution.
    """
    def __init__(self, manipulator: TransformManipulator, axis: typing.Sequence[int], highlight_ctrl: HighlightControl, handle_lines: list[sc.Line] = None, handle_dots: list[sc.Arc] = None, order: int = 0):
        """
        Initializes the ScaleGesture with a given manipulator, scaling axis, highlight control, optional handle lines, optional handle dots, and order. 
        """
    def _get_dir_and_length_from_origin(self, point):
        ...
    def _on_began(self):
        """
        Handler called when the scaling gesture begins. Sets up the necessary state for the scaling operation.
        """
    def _on_canceled(self):
        """
        Handler called when the scaling gesture is canceled. Reverts any changes made during the scaling.
        """
    def _on_changed(self):
        """
        Handler called when the scaling gesture state changes. Computes and applies the scaling factor.
        """
    def _on_ended(self):
        """
        Handler called when the scaling gesture ends. Finalizes the scaling and restores states.
        """
class TransformChangedGesture(omni.ui_scene._scene.ManipulatorGesture):
    """
    A gesture representing a change in a transformation, such as translation, rotation, or scaling.
    
        This gesture is part of the mechanism for handling transformation manipulations in a omni.ui.scene.SceneView. It is triggered when a transformation action begins, changes, ends, or is canceled. It is responsible for updating the transformation state and potentially preventing other omni.ui.scene.SceneView interactions while a transformation is active.
    
        Args:
            **kwargs: Variable length keyword arguments.
        
    """
    def __init__(self, **kwargs):
        """
        Initializes the TransformChangedGesture.
        """
    def on_began(self):
        """
        Handler for the beginning state of the gesture.
        """
    def on_canceled(self):
        """
        Handler for the canceled state of the gesture.
        """
    def on_changed(self):
        """
        Handler for the changed state of the gesture.
        """
    def on_ended(self):
        """
        Handler for the ended state of the gesture.
        """
    def process(self):
        """
        Processes the gesture and determines the appropriate action based on its state.
        """
class TransformDragGesturePayload(omni.ui_scene._scene.AbstractGesture.GesturePayload):
    """
    A payload class used for drag gestures related to transformation operations.
    
        This class contains information about the items being manipulated during transform drag gestures.
    
        Args:
            base: sc.AbstractGesture.GesturePayload
                The base gesture payload.
            changing_item: sc.AbstractManipulatorItem
                The manipulator item that is being changed during the drag operation.
        Attributes:
            changing_item: sc.AbstractManipulatorItem
                The manipulator item that is being changed during the drag operation.
        
    """
    def __init__(self, base: sc.AbstractGesture.GesturePayload, changing_item: sc.AbstractManipulatorItem):
        """
        Initializes a new instance of the TransformDragGesturePayload.
        """
class TransformGesture(omni.ui_scene._scene.DragGesture):
    """
    A gesture class used to manage transformation operations within a 3D scene. It is the base class to inherit from if you want to register custom gestures to manipulator.
    
        This class is responsible for processing gesture inputs related to translating, rotating, and scaling objects in the scene. It works in conjunction with a manipulator and a highlight control to provide visual feedback and ensure correct interaction behavior.
        Args:
            manipulator (TransformManipulator): The manipulator associated with the gesture.
            highlight_ctrl (HighlightControl): The highlight control used to manage highlighting of manipulator widgets.
            order (int): The priority order of the gesture.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        
    """
    def __init__(self, manipulator: TransformManipulator, highlight_ctrl: HighlightControl, order: int = 0, *args, **kwargs):
        """
        Initializes the TransformGesture with a given manipulator, highlight control, order, and additional arguments.
        """
    def _on_began(self):
        """
        Handler called when the gesture begins. Sets up necessary state for the transformation.
        """
    def _on_canceled(self):
        """
        Handler called when the gesture is canceled. Rolls back any changes if necessary.
        """
    def _on_changed(self):
        """
        Handler called when the gesture state changes. Typically used to perform the transformation.
        """
    def _on_ended(self):
        """
        Handler called when the gesture ends. Performs cleanup and state restoration.
        """
    def _on_prevented(self):
        """
        Handler called when the gesture is prevented from continuing, often due to other gestures taking precedence.
        """
    def process(self):
        """
        Processes the gesture, handling its state changes and invoking the appropriate methods based on the current state.
        """
    @property
    def order(self) -> int:
        ...
class TranslateChangedGesture(TransformChangedGesture):
    """
    A gesture representing a change in a translation during an interaction with a manipulator.
    
        This gesture is used internally to handle manipulator interactions in a omni.ui.scene.SceneView for translation operations. It is part of the gesture system that responds to the beginning, modification, ending, or canceling of a translation action and is responsible for updating the state of the transformation and optionally blocking other omni.ui.scene.SceneView interactions while active.
        
    """
class TranslateDragGesturePayload(TransformDragGesturePayload):
    """
    A payload for drag gestures used during translation operations.
    
        This class holds details about the translation operation such as the axis of translation, the delta movement since the last change, and the total movement since the drag started.
        
    """
    __dataclass_fields__: typing.ClassVar[dict]  # value = {'axis': Field(name='axis',type='Sequence[float]',default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'moved_delta': Field(name='moved_delta',type='Sequence[float]',default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD), 'moved': Field(name='moved',type='Sequence[float]',default=<dataclasses._MISSING_TYPE object>,default_factory=<dataclasses._MISSING_TYPE object>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),kw_only=False,_field_type=_FIELD)}
    __dataclass_params__: typing.ClassVar[dataclasses._DataclassParams]  # value = _DataclassParams(init=False,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False)
    __hash__: typing.ClassVar[None] = None
    __match_args__: typing.ClassVar[tuple] = ('axis', 'moved_delta', 'moved')
    def __eq__(self, other):
        ...
    def __repr__(self):
        ...
class TranslateGesture(TransformGesture):
    """
    A gesture class used for translating objects in a 3D scene.
    
        This class processes input related to moving objects along specific axes in the scene. It integrates with a manipulator and a highlight control to provide interactive feedback and manage the transformation.
    
        Args:
            manipulator (TransformManipulator): The manipulator associated with the gesture.
            axis (Sequence[int]): The axis along which translation occurs.
            highlight_ctrl (HighlightControl): The highlight control used to manage highlighting of manipulator widgets.
            order (int): The priority order of the gesture.
    """
    def __init__(self, manipulator: TransformManipulator, axis: typing.Sequence[int], highlight_ctrl: HighlightControl, order: int = 0):
        """
        Initializes the TranslateGesture with a given manipulator, translation axis, highlight control, and order.
        """
    def _on_began(self):
        """
        Handler called when the translation gesture begins. Sets up the necessary state for the translation operation.
        """
    def _on_canceled(self):
        """
        Handler called when the translation gesture is canceled. Reverts any changes made during the translation.
        """
    def _on_changed(self):
        """
        Handler called when the translation gesture state changes. Computes and applies the translation delta.
        """
    def _on_ended(self):
        """
        Handler called when the translation gesture ends. Finalizes the translation and restores states.
        """
def __get_input(*args, **kwargs):
    ...
def _is_alt_down() -> bool:
    ...
cl: omni.ui.color_utils.ColorShade  # value = <omni.ui.color_utils.ColorShade object>
