from __future__ import annotations
import carb as carb
import isaacsim.core.prims.impl._impl.single_prim_wrapper
from isaacsim.core.prims.impl._impl.single_prim_wrapper import _SinglePrimWrapper
from isaacsim.core.prims.impl.xform_prim import XFormPrim
from isaacsim.core.utils.prims import define_prim
from isaacsim.core.utils.prims import get_prim_at_path
from isaacsim.core.utils.prims import is_prim_path_valid
__all__ = ['SingleXFormPrim', 'XFormPrim', 'carb', 'define_prim', 'get_prim_at_path', 'is_prim_path_valid']
class SingleXFormPrim(isaacsim.core.prims.impl._impl.single_prim_wrapper._SinglePrimWrapper):
    """
    Provides high level functions to deal with an Xform prim (only one Xform prim) and its attributes/properties
    
        If there is an Xform prim present at the path, it will use it. Otherwise, a new XForm prim at
        the specified prim path will be created
    
        .. note::
    
            The prim will have ``xformOp:orient``, ``xformOp:translate`` and ``xformOp:scale`` only post-init,
            unless it is a non-root articulation link.
    
        Args:
            prim_path (str): prim path of the Prim to encapsulate or create.
            name (str, optional): shortname to be used as a key by Scene class.
                                    Note: needs to be unique if the object is added to the Scene.
                                    Defaults to "xform_prim".
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
    
        Example:
    
        .. code-block:: python
    
            >>> from isaacsim.core.prims import SingleXFormPrim
            >>>
            >>> # given the stage: /World. Get the Xform prim at /World
            >>> prim = SingleXFormPrim("/World")
            >>> prim
            <isaacsim.core.prims.single_xform_prim.SingleXFormPrim object at 0x7f52381547c0>
            >>>
            >>> # create a new Xform prim at path: /World/Objects
            >>> prim = SingleXFormPrim("/World/Objects", name="objects")
            >>> prim
            <isaacsim.core.prims.single_xform_prim.SingleXFormPrim object at 0x7f525c11d420>
        
    """
    def __init__(self, prim_path: str, name: str = 'xform_prim', position: typing.Optional[typing.Sequence[float]] = None, translation: typing.Optional[typing.Sequence[float]] = None, orientation: typing.Optional[typing.Sequence[float]] = None, scale: typing.Optional[typing.Sequence[float]] = None, visible: typing.Optional[bool] = None) -> None:
        ...
