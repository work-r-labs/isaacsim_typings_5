from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.viewport.window.legacy import _resolve_viewport_setting
from omni.kit.widget.viewport.api import ViewportAPI
from omni.kit.widget.viewport.widget import ViewportWidget
from omni import ui
from pxr import Sdf
import pxr.Sdf
import pxr.Usd
from pxr import Usd
import traceback as traceback
import weakref as weakref
__all__: list = ['ViewportLayers']
class ViewportLayers:
    """
    The Viewport Layers Widget
           Holds a single viewport and manages the order of layers within a ui.ZStack
        
    """
    def _ViewportLayers__on_timeline_event(self, e: carb.events._events.IEvent):
        ...
    def _ViewportLayers__viewport_layer_event(self, loaded_factory, loading):
        ...
    def _ViewportLayers__viewport_updated(self, camera_path: pxr.Sdf.Path, stage: pxr.Usd.Stage):
        ...
    def __del__(self):
        ...
    def __init__(self, viewport_id: str, usd_context_name: str = '', get_frame_parent: typing.Optional[typing.Callable] = None, hydra_engine_options: typing.Optional[dict] = None, **ui_kwargs):
        ...
    def destroy(self):
        ...
    def get_frame(self, name: str) -> None:
        ...
    @property
    def layers(self) -> typing.Sequence:
        ...
    @property
    def viewport_api(self) -> ViewportAPI:
        ...
    @property
    def viewport_widget(self) -> ViewportAPI:
        ...
class _ViewportLayerItem:
    visible: bool
    def __init__(self, viewport):
        ...
    def destroy(self):
        ...
    @property
    def categories(self) -> typing.Sequence:
        ...
    @property
    def layers(self) -> typing.Sequence:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def viewport_api(self):
        ...
DEFAULT_LAYER_ORDER: list = ['omni.kit.viewport.window.ViewportLayer', 'omni.kit.viewport.window.SceneLayer', 'omni.kit.viewport.menubar.MenuBarLayer']
