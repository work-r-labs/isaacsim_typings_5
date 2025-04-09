from __future__ import annotations
from omni.kit.imgui_renderer._imgui_renderer import IImGuiRenderer
from omni.kit.imgui_renderer._imgui_renderer import acquire_imgui_renderer_interface
from omni.kit.imgui_renderer._imgui_renderer import release_imgui_renderer_interface
from . import _imgui_renderer
__all__ = ['IImGuiRenderer', 'acquire_imgui_renderer_interface', 'get_imgui_renderer_interface', 'release_imgui_renderer_interface']
def get_imgui_renderer_interface() -> _imgui_renderer.IImGuiRenderer:
    """
    Returns cached :class:`omni.kit.renderer.IImGuiRenderer` interface
    """
