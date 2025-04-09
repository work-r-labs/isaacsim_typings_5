from __future__ import annotations
import carb as carb
__all__ = ['USE_RAYCAST_SETTING', 'carb', 'perform_raycast_query']
def perform_raycast_query(viewport_api: ViewportAPI, mouse_ndc: typing.Sequence[float], mouse_pixel: typing.Sequence[float], on_complete_fn: typing.Callable, query_name: str = ''):
    ...
USE_RAYCAST_SETTING: str = '/exts/omni.kit.viewport.window/useRaycastQuery'
