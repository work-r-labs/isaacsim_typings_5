from __future__ import annotations
import pxr.Usd
from pxr import Usd
__all__ = ['ALWAYS_PICK_MODEL', 'DISPLAY_NAME', 'HIDE_IN_STAGE_WINDOW', 'HIDE_IN_UI', 'NO_DELETE', 'Usd', 'get_display_name', 'is_always_pick_model', 'is_hide_in_stage_window', 'is_hide_in_ui', 'is_no_delete', 'set_always_pick_model', 'set_display_name', 'set_hide_in_stage_window', 'set_hide_in_ui', 'set_no_delete']
def get_display_name(prim) -> str:
    """
    Gets display name from the metadata of the prim.
    """
def is_always_pick_model(prim: pxr.Usd.Prim) -> bool:
    """
    Whether selecting this prim should always pick the enclosing prim with kind:model or not.
    """
def is_hide_in_stage_window(prim: pxr.Usd.Prim) -> bool:
    """
    Whether the prim should be hidden in the stage window or not.
    """
def is_hide_in_ui(prim: pxr.Usd.Prim) -> bool:
    """
    Whether the prim should be hidden or not.
    """
def is_no_delete(prim: pxr.Usd.Prim) -> bool:
    """
    Whether the prim should be removed or not.
    """
def set_always_pick_model(prim: pxr.Usd.Prim, pick_model: bool):
    """
    Sets metadata for prim to instruct selection whether it should always pick the enclosing prim with kind:model or not.
    """
def set_display_name(prim: pxr.Usd.Prim, name: str):
    """
    Sets an user readable name for the prim to instruct UI to display it.
    """
def set_hide_in_stage_window(prim: pxr.Usd.Prim, hide: bool):
    """
    Sets metadata for prim to instruct stage window to display/hide the prim.
    """
def set_hide_in_ui(prim: pxr.Usd.Prim, value: bool):
    """
    Sets metadata for the prim to instruct UI whether it should be hidden in the UI or not.
    """
def set_no_delete(prim: pxr.Usd.Prim, no_delete: bool):
    """
    Sets metadata for prim to instruct UI whether the prim can be removed or not.
    """
ALWAYS_PICK_MODEL: str = 'always_pick_model'
DISPLAY_NAME: str = 'displayName'
HIDE_IN_STAGE_WINDOW: str = 'hide_in_stage_window'
HIDE_IN_UI: str = 'omni:kit:hideInUI'
NO_DELETE: str = 'no_delete'
