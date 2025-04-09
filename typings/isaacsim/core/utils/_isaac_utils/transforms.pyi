from __future__ import annotations
import carb._carb
__all__ = ['set_scale', 'set_transform']
def set_scale(arg0: int, arg1: str, arg2: carb._carb.Float3) -> None:
    """
                    Set scale for an object in the stage
    
                    Args:
    
                        arg0 (:obj:`omni.isaac.dynamic_control._dynamic_control`): handle to dynamic control api
    
                        arg1 (:obj:`int`): Stage ID
    
                        arg2 (:obj:`carb::Float3`): scale
    """
def set_transform(arg0: int, arg1: str, arg2: carb._carb.Float3, arg3: carb._carb.Float4) -> None:
    """
                    Set transform for an object in the stage, handles physics objects if simulation is running using dynamic control
    
                    Args:
    
                        arg0 (:obj:`omni.isaac.dynamic_control._dynamic_control`): handle to dynamic control api
    
                        arg1 (:obj:`int`): Stage ID
    
                        arg2 (:obj:`carb::Float3`): translation
                        arg2 (:obj:`carb::Float4`): rotation
    """
