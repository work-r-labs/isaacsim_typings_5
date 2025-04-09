from __future__ import annotations
import asyncio as asyncio
import carb as carb
import importlib as importlib
import omni as omni
from omni.kit.widget.material_preview.relevant_stage import RelevantStage
from omni.kit.widget.material_preview.stage_duplicate_utils import copy_prim
from omni.kit.widget.material_preview.swatch_utils import get_default_camera
from omni.kit.widget.material_preview.swatch_utils import get_swatch_layer
from omni.kit.widget.material_preview.usd_baked_preview import UsdBakedPreview
from pxr import Gf
from pxr import Sdf
import pxr.Sdf
from pxr import UsdGeom
import random as random
import string as string
__all__: list = ['class MaterialPreviewProducer']
class MaterialPreviewProducer:
    """
    
        This object creates a new USD context and Hydra texture. It watches the
        given shader and synchronizes it with the source context. The purpose of
        this class is to return the GPU ID of the viewport to use in
        ImageProvider.
        
    """
    class _Event(set):
        """
        
                A list of callable objects. Calling an instance of this will cause a
                call to each item in the list in ascending order by index.
                
        """
        def __call__(self, *args, **kwargs):
            """
            Called when the instance is “called” as a function
            """
        def __repr__(self):
            """
            
                        Called by the repr() built-in function to compute the “official”
                        string representation of an object.
                        
            """
    class _EventSubscription:
        """
        
                Event subscription.
        
                _Event has callback while this object exists.
                
        """
        def __del__(self):
            """
            Called by GC.
            """
        def __init__(self, event, fn):
            """
            
                        Save the function, the event, and add the function to the event.
                        
            """
    paused = ...
    resolution = ...
    def _MaterialPreviewProducer__bind_shader(self):
        """
        Bind the shader to the swatch
        """
    def _MaterialPreviewProducer__copy_shader(self):
        """
        Copy the shader from the source context to the swatch context
        """
    def _MaterialPreviewProducer__on_hydra_texture_drawable_changed(self, event: carb.events._events.IEvent):
        """
        Called by the hydra texture when the resolution is changed
        """
    def _MaterialPreviewProducer__on_material_changed(self, properties):
        """
        Called by RelevantStage when the root material is changed
        """
    def _MaterialPreviewProducer__schedule_captures(self):
        ...
    def _MaterialPreviewProducer__set_perspective(self):
        """
        Set the aspect ratio to match resolution
        """
    def __init__(self, source_context_name: str = '', shader_path: typing.Optional[pxr.Sdf.Path] = None, swatch_layer_path: typing.Optional[str] = None, camera_path: typing.Optional[pxr.Sdf.Path] = None, hydra_engine_name: str = 'rtx'):
        """
        
                The object is created unititialized. It will be automatically
                initialized when requesting GPU ID.
        
                ### Arguments:
        
                    `source_context_name : str`
                        The name of the USD context with the given shader
        
                    `shader_path : Optional[Sdf.Path]`
                        The path to the shader to synchtonize
        
                    `swatch_layer_path : Optional[str]`
                        The usd scene with the swatch
        
                    `camera_path : Optional[Sdf.Path]`
                        The path to the camera in the swatch scene.
                
        """
    def clear(self):
        """
        Clear the swatch stage
        """
    def destroy(self):
        ...
    def get_captured_raw_data(self) -> typing.Optional[typing.Tuple[typing.List[int], int, int]]:
        """
        Returns baked preview (data, width, height)
        """
    def get_raw_data_async(self) -> typing.Tuple[typing.List[int], int, int, int, int]:
        """
        
                Gets the framebuffer contents.
        
                It's async because the data becames available the next frame.
                
        """
    def initialize(self):
        """
        
                Initialize the object
                
        """
    def set_captured_data(self):
        """
        Captures the framebuffer and saves it to the current material
        """
    def set_captured_data_async(self):
        ...
    def set_listen_root(self, root: pxr.Sdf.Path):
        """
        Set path that is synchronized with the swatch stage
        """
    def set_material(self, shader_path: pxr.Sdf.Path):
        """
        The path to the shader to watch
        """
    def set_on_baked_preview_changed_fn(self, callback_fn):
        """
        
                Callback when any property of the material is changed.
                
        """
    def set_on_drawable_changed_fn(self, callback_fn):
        """
        
                Callback when the resolution is changed. When it happened, the
                user should recreate ui.ImageProvider.
                
        """
    def submit_camera(self, camera: pxr.Sdf.Path):
        """
        Set the camera
        """
    def submit_layer(self, delta_layer: pxr.Sdf.Layer):
        """
        Sent the given layer to the swatch stage
        """
    def submit_text(self, delta_text: str):
        """
        Sent the given layer as text to the swatch stage
        """
    @property
    def camera_prim(self):
        ...
    @property
    def gpu_reference(self):
        """
        Opaque GPU reference
        """
    @property
    def material_path(self):
        """
        The path to the shader to watch
        """
    @material_path.setter
    def material_path(self, path):
        """
        The path to the shader to watch
        """
    @property
    def ready_for_capture(self) -> bool:
        ...
