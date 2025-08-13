from __future__ import annotations
import enum
from enum import Enum
import typing
__all__: list[str] = ['Enum', 'IsaacEvents']
class IsaacEvents(enum.Enum):
    PHYSICS_READY: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.PHYSICS_READY: 'isaac.physics_ready'>
    PHYSICS_WARMUP: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.PHYSICS_WARMUP: 'isaac.physics_warmup'>
    POST_PHYSICS_STEP: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.POST_PHYSICS_STEP: 'isaac.post_physics_step'>
    POST_RESET: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.POST_RESET: 'isaac.post_reset'>
    PRE_PHYSICS_STEP: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.PRE_PHYSICS_STEP: 'isaac.pre_physics_step'>
    PRIM_DELETION: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.PRIM_DELETION: 'isaac.prim_deletion'>
    SIMULATION_VIEW_CREATED: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.SIMULATION_VIEW_CREATED: 'isaac.simulation_view_created'>
    TIMELINE_STOP: typing.ClassVar[IsaacEvents]  # value = <IsaacEvents.TIMELINE_STOP: 'isaac.timeline_stop'>
