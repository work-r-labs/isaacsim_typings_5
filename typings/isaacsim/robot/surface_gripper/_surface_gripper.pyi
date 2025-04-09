"""
 

        Surface Grippers
        -----------------

        This submodule provides a Helper to create a breakable joint using a PhysxD6Joint. 
        The surface gripper is useful to approximate suction style grippers.
        
        Example:
            To create a surface gripper you need to import this submodule, create a Surface_Gripper_Properties, and then create a Surface Gripper:

            .. code-block:: python

                from isaacsim.robot.surface_gripper._surface_gripper import Surface_Gripper
                from isaacsim.robot.surface_gripper._surface_gripper import Surface_Gripper_Properties
                import numpy as np

                # Create surface gripper
                surface_gripper = Surface_Gripper()
                sgp = Surface_Gripper_Properties()

                # Configure the Gripper Properties here (Example configuration below)
                sgp.d6JointPath = ""
                sgp.parentPath = "/GripperCone"
                sgp.offset = _dc.Transform()
                sgp.offset.p.x = 0
                sgp.offset.p.z = -30.01
                sgp.offset.r = [0, 0.7171, 0, 0.7171]  # Rotate to point gripper in Z direction
                sgp.gripThreshold = 2
                sgp.forceLimit = 1.0e4
                sgp.torqueLimit = 1.0e5
                sgp.bendAngle = np.pi / 4
                sgp.stiffness = 1.0e4
                sgp.damping = 1.0e3

                # Initialize the gripper with the properties
                surface_gripper.initialize(sgp)


        Then, on every simulation step, the gripper must be updated to check if the joint has been broken due to external forces, and update its status, by calling the ``gripper.update()`` method.

        In order to grip an object, the user should call ``gripper.close()``, which will return whether it was successful at gripping something.

        If you want to check if the gripper is holding an object, you can use the method ``gripper.is_closed()``, which returns its status.

        To release the gripped object, call ``gripper.release()``
        
        
"""
from __future__ import annotations
import omni.physics.tensors.bindings._physicsTensors
__all__ = ['Surface_Gripper', 'Surface_Gripper_Properties']
class Surface_Gripper:
    def __init__(self) -> None:
        """
                        Creates a Surface Gripper, that connects two rigid bodies when it's actuated in close proximity
        """
    def close(self) -> bool:
        """
                        Attempts to close the gripper.
        
                        Returns:
        
                            `True` if any object is within the gripper threshold and it closes, `False` otherwise.
        """
    def initialize(self, arg0: Surface_Gripper_Properties) -> bool:
        """
                        Initializes the surface gripper object, setting the given properties
        
                        Args:
                            arg0: surface gripper properties
        
                        Returns:
        
                            `True` if initialization is succesful, `False` otherwise.
        """
    def is_attempting_close(self) -> bool:
        """
                        Returns:
        
                            `True` if gripper is attempting to close, `False` otherwise.
        """
    def is_closed(self) -> bool:
        """
                        Returns:
        
                            `True` if gripper is closed, `False` otherwise.
        """
    def open(self) -> bool:
        """
                        Attempts to open the gripper.
        
                        Returns:
        
                            `True` if gripper was closed and it was succesfully open, `False` otherwise.
        """
    def update(self) -> None:
        """
        Updates the internal status of the gripper. This must be called on every step the gripper is closed to verify the gripper did not break contact with the gripped object.
        """
class Surface_Gripper_Properties:
    """
    Properties for the Surface Gripper
    """
    def __getstate__(self) -> tuple:
        ...
    def __init__(self) -> None:
        ...
    def __setstate__(self, arg0: tuple) -> None:
        ...
    @property
    def bendAngle(self) -> float:
        """
        maximum bend angle for the gripper(:obj:`float`)
        """
    @bendAngle.setter
    def bendAngle(self, arg0: float) -> None:
        ...
    @property
    def d6JointPath(self) -> str:
        """
        USD path to joint (:obj:`str`)
        """
    @d6JointPath.setter
    def d6JointPath(self, arg0: str) -> None:
        ...
    @property
    def damping(self) -> float:
        """
        Gripper Damping(:obj:`float`)
        """
    @damping.setter
    def damping(self, arg0: float) -> None:
        ...
    @property
    def disableGravity(self) -> bool:
        """
        Flag to disable gravity on selected object to compensate for its mass(:obj:`bool`)
        """
    @disableGravity.setter
    def disableGravity(self, arg0: bool) -> None:
        ...
    @property
    def forceLimit(self) -> float:
        """
        Force Breaking limit (:obj:`float`)
        """
    @forceLimit.setter
    def forceLimit(self, arg0: float) -> None:
        ...
    @property
    def gripThreshold(self) -> float:
        """
        Threshold distance the gripper will respond to closing (:obj:`float`)
        """
    @gripThreshold.setter
    def gripThreshold(self, arg0: float) -> None:
        ...
    @property
    def offset(self) -> omni.physics.tensors.bindings._physicsTensors.Transform:
        """
        Transform from parent body to joint (:obj:`omni.physics.tensors.Transform`)
        """
    @offset.setter
    def offset(self, arg0: omni.physics.tensors.bindings._physicsTensors.Transform) -> None:
        ...
    @property
    def parentPath(self) -> str:
        """
        USD Path to parent body (:obj:`str`)
        """
    @parentPath.setter
    def parentPath(self, arg0: str) -> None:
        ...
    @property
    def retryClose(self) -> bool:
        """
        Flag to indicate if gripper should keep attempting to close until it grips some object(:obj:`bool`)
        """
    @retryClose.setter
    def retryClose(self, arg0: bool) -> None:
        ...
    @property
    def stiffness(self) -> float:
        """
        Gripper Stiffness(:obj:`float`)
        """
    @stiffness.setter
    def stiffness(self, arg0: float) -> None:
        ...
    @property
    def torqueLimit(self) -> float:
        """
        Torque Breaking limit (:obj:`float`)
        """
    @torqueLimit.setter
    def torqueLimit(self, arg0: float) -> None:
        ...
