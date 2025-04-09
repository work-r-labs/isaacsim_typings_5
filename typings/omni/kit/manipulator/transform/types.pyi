"""
Type Classes needed for transformation manipulation
"""
from __future__ import annotations
import enum
from enum import Enum
from enum import Flag
from enum import auto
import typing
__all__: list = ['Axis', 'Operation']
class Axis(enum.Flag):
    """
    An enumeration to represent different axes and their combinations for transformations.
    
        This Flag Enum is used to define axes for translation, rotation, and scaling operations in a 3D space. It allows combining multiple axes to define a plane or space.
        
    """
    ALL: typing.ClassVar[Axis]  # value = <Axis.ALL: 15>
    SCREEN: typing.ClassVar[Axis]  # value = <Axis.SCREEN: 8>
    X: typing.ClassVar[Axis]  # value = <Axis.X: 1>
    Y: typing.ClassVar[Axis]  # value = <Axis.Y: 2>
    Z: typing.ClassVar[Axis]  # value = <Axis.Z: 4>
class Operation(enum.Enum):
    """
    An enumeration to represent different types of manipulator operations.
    
        This Enum is used for specifying the type of operation that a manipulator should perform, such as translation, rotation, or scaling, including their delta variants.
        
    """
    NONE: typing.ClassVar[Operation]  # value = <Operation.NONE: 4>
    ROTATE: typing.ClassVar[Operation]  # value = <Operation.ROTATE: 2>
    ROTATE_DELTA: typing.ClassVar[Operation]  # value = <Operation.ROTATE_DELTA: 6>
    SCALE: typing.ClassVar[Operation]  # value = <Operation.SCALE: 3>
    SCALE_DELTA: typing.ClassVar[Operation]  # value = <Operation.SCALE_DELTA: 7>
    TRANSLATE: typing.ClassVar[Operation]  # value = <Operation.TRANSLATE: 1>
    TRANSLATE_DELTA: typing.ClassVar[Operation]  # value = <Operation.TRANSLATE_DELTA: 5>
