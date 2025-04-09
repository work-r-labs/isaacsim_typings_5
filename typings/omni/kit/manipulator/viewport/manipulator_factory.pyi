from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.manipulator.viewport.viewport_manipulator import ViewportManipulator
from omni import ui
from omni.ui import scene as sc
import typing
__all__ = ['DRAW_ON_VP1', 'ManipulatorFactory', 'ManipulatorPool', 'SUPPORT_MULTI_VP1', 'ViewportManipulator', 'carb', 'omni', 'sc', 'ui']
class ManipulatorFactory:
    _instance: typing.ClassVar[ManipulatorFactory]  # value = <omni.kit.manipulator.viewport.manipulator_factory.ManipulatorFactory object>
    @classmethod
    def create_manipulator(cls, manipulator_class: typing.Type, **kwargs):
        """
        
                Creates a ViewportManipulator object.
                Args: Arguments need to match manipulator_type's constructor
                
        """
    @classmethod
    def destroy_manipulator(cls, *args, **kwargs):
        """
        
                Destroys a ViewportManipulator object.
                Args @see `_destroy_manipulator`
                
        """
    def _create_manipulator(self, manipulator_class: typing.Type, **kwargs) -> omni.kit.manipulator.viewport.viewport_manipulator.ViewportManipulator:
        """
        
                This function creates a TransformManipulator object that has instances in ALL existing viewports and future created viewports.
        
                Args: Arguments need to match manipulator_type's constructor
        
                Return:
                    ViewportManipulator object.
                
        """
    def _create_vp1_scene_view(self, instance):
        ...
    def _destroy_manipulator(self, manipulator: omni.kit.manipulator.viewport.viewport_manipulator.ViewportManipulator):
        """
        
                Destroy the TransformManipulator and all its instances.
                
        """
    def _get_or_create_pools_for_manipulator_class(self, manipulator_class: typing.Type) -> typing.List[omni.kit.manipulator.viewport.manipulator_factory.ManipulatorPool]:
        ...
    def _on_update(self, e: carb.events._events.IEvent):
        ...
    def _on_vp_draw(self, event: carb.events._events.IEvent, vp_instance):
        ...
    def shutdown(self):
        ...
    def startup(self):
        ...
class ManipulatorPool:
    """
    
        A ManipulatorPool allows omni.ui.scene items in released Manipulator to be reused for a newly created Manipulator,
        instead having to rebuild them in the scene view.
        
    """
    def __init__(self, manipulator_class, scene_view: omni.ui_scene._scene.SceneView):
        ...
    def create(self):
        ...
    def release(self, manipulator):
        ...
class _ViewportWindowObject:
    def __del__(self):
        ...
    def __init__(self, ui_window, ui_scene_view, draw_sub):
        ...
DRAW_ON_VP1: bool = False
SUPPORT_MULTI_VP1: bool = False
