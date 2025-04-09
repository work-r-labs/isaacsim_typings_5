from __future__ import annotations
__all__ = ['subscribe_on_change', 'unsubscribe_on_change']
def _dispatch_changed():
    ...
def subscribe_on_change(on_change):
    """
    Subscribe to module change events. Triggered when commands added, executed.
    """
def unsubscribe_on_change(on_change):
    """
    Unsubscribe to module change events.
    """
_on_change: set = set()
