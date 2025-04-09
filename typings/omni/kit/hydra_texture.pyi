from __future__ import annotations
import omni as omni
from omni.hydratexture._hydra_texture import IHydraTexture
from omni.hydratexture._hydra_texture import IHydraTextureFactory
from omni.hydratexture._hydra_texture import acquire_hydra_texture_factory_interface as _acquire_hydra_texture_factory_interface
from omni.kit.app._impl import deprecated as _deprecated
import typing
__all__: list = ['create_hydra_texture', 'IHydraTexture', 'EVENT_TYPE_DRAWABLE_CHANGED', 'EVENT_TYPE_HYDRA_ENGINE_CHANGED', 'EVENT_TYPE_RENDER_SETTINGS_CHANGED']
class Extension(omni.ext._extensions.IExt):
    _Extension__iface: typing.ClassVar[omni.hydratexture._hydra_texture.IHydraTextureFactory]  # value = <omni.hydratexture._hydra_texture.IHydraTextureFactory object>
    def on_shutdown(self):
        ...
    def on_startup(self):
        ...
def create_hydra_texture(name: str, width: int, height: int, usd_context_name: str = '', usd_camera_path: str = '/OmniverseKit_Persp', hydra_engine_name: str = 'rtx', is_async: bool = True, is_async_low_latency: bool = False, hydra_tick_rate: int = 0, engine_creation_flags: int = 0, device_mask: int = 0, *args, **kwargs):
    ...
EVENT_TYPE_DRAWABLE_CHANGED: int = 11183105052706112355
EVENT_TYPE_HYDRA_ENGINE_CHANGED: int = 13015938697279081123
EVENT_TYPE_RENDER_SETTINGS_CHANGED: int = 5475677776228743414
