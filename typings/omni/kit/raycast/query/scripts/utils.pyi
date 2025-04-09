from __future__ import annotations
from omni.kit.raycast import query as rq
__all__: list = ['raycast_from_mouse_ndc']
def raycast_from_mouse_ndc(mouse_ndc: typing.Sequence[float], viewport_api: ViewportAPI, on_complete_fn: typing.Callable):
    ...
