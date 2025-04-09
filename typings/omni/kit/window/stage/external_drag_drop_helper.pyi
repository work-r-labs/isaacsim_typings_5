from __future__ import annotations
import omni.kit.window.drop_support.drop_support
from omni import ui
import omni.ui._ui
from pxr import Sdf
__all__ = ['Sdf', 'destroy_external_drag_drop', 'external_drag_drop', 'setup_external_drag_drop', 'ui']
def _on_ext_drag_drop(edd, payload: typing.List[str], model: omni.ui._ui.AbstractItemModel):
    ...
def destroy_external_drag_drop():
    ...
def setup_external_drag_drop(window_name: str, stage_widget):
    ...
external_drag_drop: omni.kit.window.drop_support.drop_support.ExternalDragDrop  # value = <omni.kit.window.drop_support.drop_support.ExternalDragDrop object>
