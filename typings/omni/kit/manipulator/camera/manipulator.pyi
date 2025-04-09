from __future__ import annotations
from omni.kit.manipulator.camera.gestures import build_gestures
import omni.kit.manipulator.camera.model
from omni.kit.manipulator.camera.model import CameraManipulatorModel
from omni.kit.manipulator.camera.model import _flatten_matrix
from omni.kit.manipulator.camera.model import _optional_bool
from omni.ui import scene as sc
import omni.ui_scene._scene
import pxr.Gf
from pxr import Gf
__all__: list = ['CameraManipulatorBase', 'adjust_center_of_interest']
class CameraManipulatorBase(omni.ui_scene._scene.Manipulator):
    """
     Base class, resposible for building up the gestures. 
    """
    def __init__(self, bindings: dict = None, model: omni.ui_scene._scene.AbstractManipulatorModel = None, *args, **kwargs):
        """
        
                Constructor
        
                Args:
                    bindings (dict): Set up the bindings for the manipulator.
                    model (omni.ui.scene.AbstractManipulatorModel): Set the model of the manipulator.
                
        """
    def _on_began(self, model: omni.kit.manipulator.camera.model.CameraManipulatorModel, *args, **kwargs):
        ...
    def destroy(self):
        """
        Destroys the manipulator instance.
        """
    def on_build(self):
        """
         Called when the manipulator is build. 
        """
    @property
    def gamepad_enabled(self) -> bool:
        """
        
                Get whether or not the gamepad is enabled.
        
                Returns:
                    bool
                
        """
    @gamepad_enabled.setter
    def gamepad_enabled(self, value: bool):
        """
        
                Enable or disable the gamepad controller.
        
                Args:
                    value (bool): Set whether or not the gamepad is enabled.
                
        """
class SceneViewCameraManipulator(CameraManipulatorBase):
    """
    A simple camera manipulator for controlling the camera's center of interest to omni.ui.scene view.
    """
    def __init__(self, center_of_interest, *args, **kwargs):
        """
        
                Constructor.
        
                Args:
                    center_of_interest (Gf.Vec3d): Set the center of interest for the camera
                
        """
    def _on_began(self, model: omni.kit.manipulator.camera.model.CameraManipulatorModel, mouse):
        ...
    def on_model_updated(self, item):
        """
        
                Called whenever the model changes.
        
                Args:
                    item (omni.ui.scene.AbstractManipulatorItem): Identify which item in the model has changed.
                
        """
def adjust_center_of_interest(model: omni.kit.manipulator.camera.model.CameraManipulatorModel, initial_transform: pxr.Gf.Matrix4d, final_transform: pxr.Gf.Matrix4d):
    """
    
        Adjust the center-of-interest if requested.
    
        Args
            model (CameraManipulatorModel): Camera manipulator model.
            initial_transform (Gf.Matrix4d): The initial position of the camera.
            final_transform (Gf.Matrix4d): The final transform of the camera.
    
        Returns:
            Tuple[[Gf.Vec3d], [Gf.Vec3d]]: Start and end of center of interest.
        
    """
