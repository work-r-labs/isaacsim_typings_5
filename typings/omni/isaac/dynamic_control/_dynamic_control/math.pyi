from __future__ import annotations
import omni.isaac.dynamic_control._dynamic_control
__all__: list[str] = ['inverse', 'lerp', 'mul', 'slerp', 'transform_inv']
def inverse(arg0: omni.isaac.dynamic_control._dynamic_control.Transform) -> omni.isaac.dynamic_control._dynamic_control.Transform:
    """
    Gets Inverse Transform
                 Args:
    
                     arg0 (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`): Transform
    
                 Returns:
    
                     :obj:`omni.isaac.dynamic_control._dynamic_control.Transform`: The inverse Inverse Transform
    """
def lerp(arg0: omni.isaac.dynamic_control._dynamic_control.Transform, arg1: omni.isaac.dynamic_control._dynamic_control.Transform, arg2: float) -> omni.isaac.dynamic_control._dynamic_control.Transform:
    """
                    Performs Linear interpolation between points arg0 and arg1
    
                    Args:
    
                        arg0 (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`): Transform
    
                        arg1 (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`): Transform
    
                        arg2 (:obj:`float`): distance from 0 to 1, where 0 is closest to arg0, and 1 is closest to arg1
    
                    Returns:
    
                        :obj:`omni.isaac.dynamic_control._dynamic_control.Transform`: Interpolated transform
    """
def mul(arg0: omni.isaac.dynamic_control._dynamic_control.Transform, arg1: omni.isaac.dynamic_control._dynamic_control.Transform) -> omni.isaac.dynamic_control._dynamic_control.Transform:
    """
     Performs a Forward Transform multiplication between the transforms
            
            Args:
                arg0 (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`): First Transform
    
                arg1 (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`): Second Transform
    
            Returns:
    
                :obj:`omni.isaac.dynamic_control._dynamic_control.Transform`: ``arg0 * arg1``
    """
def slerp(arg0: omni.isaac.dynamic_control._dynamic_control.Transform, arg1: omni.isaac.dynamic_control._dynamic_control.Transform, arg2: float) -> omni.isaac.dynamic_control._dynamic_control.Transform:
    """
                    Performs Spherical Linear interpolation between points arg0 and arg1
    
                    Args:
    
                        arg0 (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`): Transform
    
                        arg1 (:obj:`omni.isaac.dynamic_control._dynamic_control.Transform`): Transform
    
                        arg2 (:obj:`float`): distance from 0 to 1, where 0 is closest to arg0, and 1 is closest to arg1
    
                    Returns:
    
                        :obj:`omni.isaac.dynamic_control._dynamic_control.Transform`: Interpolated transform
    """
def transform_inv(arg0: omni.isaac.dynamic_control._dynamic_control.Transform, arg1: omni.isaac.dynamic_control._dynamic_control.Transform) -> omni.isaac.dynamic_control._dynamic_control.Transform:
    """
                    Computes local Transform of arg1 with respect to arg0: `inv(arg0)*arg1`
    
                    Args:
                    
                        arg0 (`omni.isaac.dynamic_control._dynamic_control.Transform`): origin Transform
    
                        arg1 (`omni.isaac.dynamic_control._dynamic_control.Transform`): Transform
    
                    Returns:
    
                        :obj:`omni.isaac.dynamic_control._dynamic_control.Transform`: resulting transform of ``inv(arg0)*arg1``
    """
