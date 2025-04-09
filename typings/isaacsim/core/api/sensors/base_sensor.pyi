from __future__ import annotations
import isaacsim.core.prims.impl.single_xform_prim
from isaacsim.core.prims.impl.single_xform_prim import SingleXFormPrim
__all__ = ['BaseSensor', 'SingleXFormPrim']
class BaseSensor(isaacsim.core.prims.impl.single_xform_prim.SingleXFormPrim):
    """
    Provides a common properties and methods to deal with prims as a sensor
    
        .. note::
    
            This class, which inherits from ``SingleXFormPrim``, does not currently add any new property/method to it.
            Its definition is oriented to future implementations.
    
        Args:
            prim_path (str): prim path of the Prim to encapsulate or create.
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "base_sensor".
            position (Optional[Sequence[float]], optional): position in the world frame of the prim. shape is (3, ).
                                                        Defaults to None, which means left unchanged.
            translation (Optional[Sequence[float]], optional): translation in the local frame of the prim
                                                            (with respect to its parent prim). shape is (3, ).
                                                            Defaults to None, which means left unchanged.
            orientation (Optional[Sequence[float]], optional): quaternion orientation in the world/ local frame of the prim
                                                            (depends if translation or position is specified).
                                                            quaternion is scalar-first (w, x, y, z). shape is (4, ).
                                                            Defaults to None, which means left unchanged.
            scale (Optional[Sequence[float]], optional): local scale to be applied to the prim's dimensions. shape is (3, ).
                                                    Defaults to None, which means left unchanged.
            visible (bool, optional): set to false for an invisible prim in the stage while rendering. Defaults to True.
    
        Raises:
            Exception: if translation and position defined at the same time
        
    """
    def __init__(self, prim_path: str, name: str = 'base_sensor', position: typing.Optional[typing.Sequence[float]] = None, translation: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None, scale: typing.Optional[typing.Sequence[float]] = None, visible: typing.Optional[bool] = None) -> None:
        ...
    def initialize(self, physics_sim_view = None) -> None:
        """
        Create a physics simulation view if not passed and using PhysX tensor API
        
                .. note::
        
                    If the prim has been added to the world scene (e.g., ``world.scene.add(prim)``),
                    it will be automatically initialized when the world is reset (e.g., ``world.reset()``).
        
                Args:
                    physics_sim_view (omni.physics.tensors.SimulationView, optional): current physics simulation view. Defaults to None.
        
                Example:
        
                .. code-block:: python
        
                    >>> prim.initialize()
                
        """
    def post_reset(self) -> None:
        ...
