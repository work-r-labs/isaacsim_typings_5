from __future__ import annotations
import carb._carb
__all__: list[str] = ['set_scale', 'set_transform']
def set_scale(arg0: int, arg1: str, arg2: carb._carb.Float3) -> None:
    """
                    Set scale for an object in the stage
    
                    Args:
    
                        stageId (:obj:`int`): Stage ID
                        
                        primPath (:obj:`str`): Path to the prim
                        
                        scale (:obj:`carb.Float3`): Scale vector
    """
def set_transform(arg0: int, arg1: str, arg2: carb._carb.Float3, arg3: carb._carb.Float4) -> None:
    """
                    Set transform for an object in the stage, handles physics objects if simulation is running using dynamic control
    
                    Args:
    
                        stageId (:obj:`int`): Stage ID
                        
                        primPath (:obj:`str`): Path to the prim
                        
                        translation (:obj:`carb.Float3`): Translation vector
                        
                        rotation (:obj:`carb.Float4`): Rotation quaternion
    """
