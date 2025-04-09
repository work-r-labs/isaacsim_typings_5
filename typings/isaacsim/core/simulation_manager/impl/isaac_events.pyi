from __future__ import annotations
import carb as carb
import enum
from enum import Enum
import typing
__all__ = ['Enum', 'IsaacEvents', 'carb']
class IsaacEvents(enum.Enum):
    """
    An enumeration.
    """
    PHYSICS_READY: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.PHYSICS_READY: 8855912688812884631>
    PHYSICS_STEP: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.PHYSICS_STEP: 11304719185241152482>
    PHYSICS_WARMUP: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.PHYSICS_WARMUP: 11550560088903247360>
    POST_RESET: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.POST_RESET: 1951629742519522160>
    PRIM_DELETION: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.PRIM_DELETION: 16876951981091094425>
    SIMULATION_VIEW_CREATED: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.SIMULATION_VIEW_CREATED: 12810109171162007924>
    TIMELINE_STOP: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.TIMELINE_STOP: 11695240339852159470>
