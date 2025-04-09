from __future__ import annotations
import carb as carb
import contextlib as contextlib
import omni as omni
from omni.kit.viewport.window.dragdrop.audio_file_drop_delegate import AudioFileDropDelegate
from omni.kit.viewport.window.dragdrop.material_file_drop_delegate import MaterialFileDropDelegate
from omni.kit.viewport.window.dragdrop.usd_file_drop_delegate import UsdFileDropDelegate
from omni.kit.viewport.window.dragdrop.usd_prim_drop_delegate import UsdShadeDropDelegate
from omni.kit.viewport.window.menu_entry import create_viewport_window_menu
__all__: list = ['ViewportWindowExtension']
class ViewportWindowExtension(omni.ext._extensions.IExt):
    """
    The Entry Point for Viewport Window
    """
    def _ViewportWindowExtension__register_ext_dependent_scene(self, ext_name: str, loaded_exts: typing.List[typing.Dict], ext_manager: omni.ext._extensions.ExtensionManager, factory_dict: typing.Dict, other_factories: typing.Optional[typing.Dict] = None):
        ...
    def _ViewportWindowExtension__register_scenes(self):
        ...
    def _ViewportWindowExtension__unregister_scenes(self, registered):
        ...
    def __init__(self, *args, **kwargs):
        ...
    def on_shutdown(self):
        ...
    def on_startup(self, extension_id: str):
        ...
