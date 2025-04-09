from __future__ import annotations
import carb as carb
from functools import partial
import omni as omni
from pxr import Sdf
from pxr import UsdGeom
__all__: list = ['register_actions', 'deregister_actions']
def _get_toggle_types(settings, setting_path: str) -> typing.List[str]:
    ...
def _get_viewport_argument(viewport_api, action: str):
    ...
def _get_visible(visible: typing.Union[bool, typing.Sequence[bool]], index: int):
    """
    Utility function to get visibilty as a bool or from a bool or a list with index
    """
def _stage_opened(usd_context_name: str, stage):
    ...
def _toggle_legacy_display_visibility(viewport_api, visible: typing.Union[bool, typing.Sequence[bool]], setting_keys: typing.Sequence[str], reduce_sequence: bool) -> typing.List[str]:
    ...
def _toggle_setting(setting_name: str, viewport_api: typing.Optional[ForwardRef('ViewportAPI')] = None, visible: bool | None = None):
    ...
def _toggle_viewport_visibility(viewport_api, visible: typing.Union[bool, typing.Sequence[bool], NoneType], setting_keys: typing.Sequence[str], action: str, reduce_sequence: bool = True) -> typing.Union[typing.List[str], str, NoneType]:
    ...
def deregister_actions(extension_id):
    ...
def register_actions(extension_id: str):
    ...
def set_camera(camera_str: str, viewport_api = None) -> bool:
    """
    Switch the camera in the active viewport based on the camera path.
    
        Args:
            camera_str (str): Camera Path in string form.  ie "/OmniverseKit_Persp"
            viewport_api (viewport): Optional viewport in order to set the camera
                                     in a specific viewport.
        Returns:
            bool: True if successful, False if not.
        
    """
def set_renderer(engine_name, render_mode, viewport_api = None) -> bool:
    ...
def set_viewport_resolution(resolution, viewport_api = None):
    ...
def toggle_audio_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> str | None:
    ...
def toggle_axis_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> str | None:
    ...
def toggle_bounding_box_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> str | None:
    ...
def toggle_camera_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> str | None:
    ...
def toggle_category_settings(*setting_names):
    ...
def toggle_global_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> typing.List[str]:
    ...
def toggle_grid_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> str | None:
    ...
def toggle_hud_memory_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None, process: bool = True, device: bool = True, host: bool = True) -> str | None:
    ...
def toggle_hud_visibility(viewport_api = None, visible: bool | None = None, use_setting: bool = False):
    ...
def toggle_light_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> str | None:
    ...
def toggle_mesh_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> str | None:
    ...
def toggle_rtx_rendermode(viewport_api = None) -> bool:
    ...
def toggle_selection_hilight_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> str | None:
    ...
def toggle_show_by_type_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> typing.List[str]:
    ...
def toggle_skeleton_visibility(viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> str | None:
    ...
def toggle_viewport_visibility(keys: typing.Sequence[str], viewport_api = None, visible: typing.Union[bool, typing.Sequence[bool], NoneType] = None) -> typing.List[str]:
    ...
def toggle_wireframe() -> str:
    ...
DISPLAY_GUIDE_SETTING: str = '/persistent/app/hydra/displayPurpose/guide'
DISPLAY_PROXY_SETTING: str = '/persistent/app/hydra/displayPurpose/proxy'
DISPLAY_RENDER_SETTING: str = '/persistent/app/hydra/displayPurpose/render'
FILL_VIEWPORT_SETTING: str = '/persistent/app/viewport/{viewport_api_id}/fillViewport'
FILL_VIEWPORT_TOGGLE: str = 'toggle_fill_viewport'
FRONT_CAM: str = 'front_camera'
INERTIA_ENABLE_SETTING: str = '/persistent/app/viewport/camInertiaEnabled'
INERTIA_TOGGLE: str = 'toggle_camera_inertia_enabled'
PERSISTENT_SETTINGS_PREFIX: str = '/persistent'
PERSP_CAM: str = 'perspective_camera'
RENDERER_IRAY: str = 'set_renderer_iray'
RENDERER_PXR_STORM: str = 'set_renderer_pxr_storm'
RENDERER_RTX_PT: str = 'set_renderer_rtx_pathtracing'
RENDERER_RTX_REALTIME: str = 'set_renderer_rtx_realtime'
RENDERER_RTX_TOGGLE: str = 'toggle_rtx_rendermode'
RENDERER_WIREFRAME: str = 'toggle_wireframe'
RIGHT_CAM: str = 'right_camera'
SECTION_VISIBILE_SETTING: str = '/persistent/app/viewport/{viewport_api_id}/{section}/visible'
SHADING_MODE_SETTING: str = '/exts/omni.kit.viewport.menubar.render/shadingMode'
SHOW_ALL_PURPOSE: str = 'toggle_show_by_purpose_all'
SHOW_GUIDE: str = 'toggle_show_by_purpose_guide'
SHOW_PROXY: str = 'toggle_show_by_purpose_proxy'
SHOW_RENDER: str = 'toggle_show_by_purpose_render'
TOP_CAM: str = 'top_camera'
_k_setting_to_prim_type: dict = {'scene/cameras': {'Camera'}, 'scene/skeletons': {'Skeleton'}, 'scene/audio': {'Sound', 'Listener'}, 'scene/meshes': {'Sphere', 'Cone', 'Cube', 'Cylinder', 'Mesh', 'Capsule'}}
workspace_data: list = list()
