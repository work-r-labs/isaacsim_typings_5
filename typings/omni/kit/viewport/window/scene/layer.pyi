from __future__ import annotations
import carb as carb
from omni.kit.viewport.window.events import add_event_delegation
from omni.kit.viewport.window.events import remove_event_delegation
from omni.kit.viewport.window.scene.scenes import _flatten_matrix
from omni import ui
from omni.ui import scene as sc
import traceback as traceback
import weakref as weakref
__all__: list = ['ViewportSceneLayer']
class ViewportSceneLayer:
    """
    Viewport Scene Overlay
    """
    def _ViewportSceneLayer___scene_type_added(self, factory):
        ...
    def _ViewportSceneLayer___scene_type_notification(self, factory, loading):
        ...
    def _ViewportSceneLayer___scene_type_removed(self, factory):
        ...
    def _ViewportSceneLayer__view_changed(self, viewport_api):
        ...
    def __del__(self):
        ...
    def __init__(self, factory_args, *args, **kwargs):
        ...
    def destroy(self):
        ...
    @property
    def layers(self):
        ...
class _SceneItem:
    visible: bool
    def __init__(self, transform, instance, factory):
        ...
    def __repr__(self) -> str:
        ...
    def destroy(self):
        ...
    @property
    def categories(self) -> typing.Sequence:
        ...
    @property
    def layer(self) -> typing.Sequence:
        ...
    @property
    def layers(self) -> typing.Sequence:
        ...
    @property
    def name(self) -> str:
        ...
