from __future__ import annotations
import carb as carb
from omni.kit.widget.stage.abstract_stage_column_delegate import AbstractStageColumnDelegate
import omni.kit.widget.stage.event
from omni.kit.widget.stage.event import Event
from omni.kit.widget.stage.event import EventSubscription
from omni.kit.widget.stage.singleton import Singleton
__all__: list = ['StageColumnDelegateRegistry']
class StageColumnDelegateRegistryBase:
    """
    Base class for delegate registry
    """
    def _StageColumnDelegateRegistryBase__delegate_changed(self):
        ...
    def __init__(self):
        ...
    def get_column_delegate(self, name: str) -> typing.Optional[typing.Callable[[], omni.kit.widget.stage.abstract_stage_column_delegate.AbstractStageColumnDelegate]]:
        """
        Returns the type of derived from AbstractColumnDelegate for the given name
        """
    def get_column_delegate_names(self) -> typing.List[str]:
        """
        Returns all the column delegate names
        """
    def register_column_delegate(self, name: str, delegate: typing.Callable[[], omni.kit.widget.stage.abstract_stage_column_delegate.AbstractStageColumnDelegate]):
        ...
    def subscribe_delegate_changed(self, fn: typing.Callable[[], NoneType]) -> omni.kit.widget.stage.event.EventSubscription:
        """
        
                Return the object that will automatically unsubscribe when destroyed.
                
        """
