"""
This module defines the StageIconsExtension class to manage icon registration for primitives in the stage window.
"""
from __future__ import annotations
import carb as carb
import omni as omni
from pathlib import Path
import typing
__all__: list = list()
class StageIconsExtension(omni.ext._extensions.IExt):
    """
    This class extension adds icons for some primitive types in the state window.
    """
    _icons_registered: typing.ClassVar[list] = ['PhysicsDistanceJoint', 'FlowEmitterSphere', 'Listener', 'SkelAnimationAnnotation', 'PhysicsPrismaticJoint', 'FlowEmitterPoint', 'OmniGeneralSensor', 'BehaviorScript', 'Prim', 'Inherited', 'Class', 'FlowEmitterMesh', 'Material', 'Sound', 'BehaviorMotionAbility', 'Skeleton', 'Face', 'Xform', 'BehaviorMotionLibrary', 'PhysicsRevoluteJoint', 'PhysicsJoint', 'OmniRadar', 'FlowEmitterBox', 'Shader', 'SkelJoint', 'FlowEmitterTexture', 'NavMeshVolume', 'SkelRoot', 'SkelAnimation', 'Reference', 'Instance', 'PhysicsSphericalJoint', 'GeomSubset', 'FlowEmitterNanoVdb', 'OmniLidar', 'BasisCurves', 'PhysxPhysicsGearJoint', 'OmniJoint', 'OmniUltrasonic', 'Scope', 'Camera', 'Specialized', 'PhysicsFixedJoint', 'Payload', 'NavPath', 'PhysxPhysicsRackAndPinionJoint', 'Light']
    @staticmethod
    def get_registered_icons():
        """
        Returns the list of registered icons.
        
                Returns:
                    list: The list of registered icons or None if no icons have been registered.
        """
    def on_shutdown(self):
        """
        Extension shutdown callback function. This is called automatically when the Python side of this extension unloads.
        """
    def on_startup(self, ext_id):
        """
        Extension startup callback function. This is called automatically when the Python side of this extension loads.
        """
    def register_icons(self):
        """
        Registers icons based on the SVG files found in the icons directory.
        """
