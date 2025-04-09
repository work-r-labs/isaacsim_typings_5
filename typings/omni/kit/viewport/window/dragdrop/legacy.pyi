from __future__ import annotations
import omni.kit.viewport.window.dragdrop.delegate
from omni.kit.viewport.window.dragdrop.delegate import DragDropDelegate
__all__: list = ['create_drop_helper']
class _LegacyDragDropObject(omni.kit.viewport.window.dragdrop.delegate.DragDropDelegate):
    def __init__(self, add_outline: bool, test_accepted_fn: typing.Callable, drop_fn: typing.Callable, pick_complete: typing.Callable):
        ...
    def accepted(self, drop_data: dict):
        ...
    def dropped(self, drop_data: dict):
        ...
    @property
    def add_outline(self):
        ...
def create_drop_helper(pickable: bool = False, add_outline: bool = True, on_drop_accepted_fn: typing.Callable = None, on_drop_fn: typing.Callable = None, on_pick_fn: typing.Callable = None):
    """
    Add a viewport drop handler.
    
        Args:
            pickable (bool): Deprecated, use on_pick_fn to signal you want picking.
            add_outline (False): True to add outline to picked prim when dropping.
            on_drop_accepted_fn (Callable): Callback function to check if drop helper could handle the dragging payload.
                                            Return True if payload accepted by this drop helper and will handle dropping later.
        Args:
            url (str): url in the payload.
            on_drop_fn (Callable): Callback function to handle dropping. Return a payload that evaluates to True in order to block other drop handlers.
        Args:
            url (str): url in the payload.
            target (str): picked prim path to drop.
            viewport_name (str): name of viewport window.
            usd_context_name (str): name of dropping usd context.
            on_pick_fn (Callable): Callback function to handle pick.
        Args:
            payload (Any): Return value from from on_drop_fn.
            target (str): picked prim path.
            usd_context_name (str): name of picked usd context.
        
    """
