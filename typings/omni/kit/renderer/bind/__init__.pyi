from __future__ import annotations
from omni.kit.renderer.bind._renderer import IRenderer
from omni.kit.renderer.bind._renderer import acquire_renderer_interface
from omni.kit.renderer.bind._renderer import release_renderer_interface
from . import _renderer
__all__ = ['IRenderer', 'acquire_renderer_interface', 'get_renderer_interface', 'release_renderer_interface']
def get_renderer_interface() -> _renderer.IRenderer:
    """
    Returns cached :class:`omni.kit.renderer.IRenderer` interface
    """
