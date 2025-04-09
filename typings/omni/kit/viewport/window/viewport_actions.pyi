from __future__ import annotations
import omni as omni
__all__ = ['deregister_actions', 'omni', 'register_actions']
def deregister_actions(extension_id: str, action_name: str) -> None:
    ...
def register_actions(extension_id: str, index: int, show_fn: typing.Callable, visible_fn: typing.Callable) -> typing.Optional[str]:
    ...
