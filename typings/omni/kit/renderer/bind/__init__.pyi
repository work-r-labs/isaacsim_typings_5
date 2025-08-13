from __future__ import annotations
import carb as carb
from omni.kit.renderer.bind._renderer import IRenderer
from omni.kit.renderer.bind._renderer import RendererEventType
from omni.kit.renderer.bind._renderer import acquire_renderer_interface
from omni.kit.renderer.bind._renderer import get_renderer_event_name
from omni.kit.renderer.bind._renderer import get_renderer_event_type
from omni.kit.renderer.bind._renderer import release_renderer_interface
from . import _renderer
__all__: list[str] = ['IRenderer', 'RendererEventType', 'acquire_renderer_interface', 'carb', 'get_renderer_event_name', 'get_renderer_event_type', 'get_renderer_interface', 'release_renderer_interface']
def get_renderer_interface() -> _renderer.IRenderer:
    """
    Returns cached :class:`omni.kit.renderer.IRenderer` interface
    """
