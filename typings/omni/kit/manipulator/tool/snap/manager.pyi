from __future__ import annotations
import carb as carb
from omni.kit.manipulator.tool.snap.provider import SnapProvider
from omni.kit.manipulator.tool.snap.registry import SnapProviderRegistry
from omni.ui import scene as sc
import omni.ui_scene._scene
import pxr.Gf
from pxr import Gf
from pxr import Sdf
__all__ = ['CONFORM_TO_TARGET_SETTING_PATH', 'CONFORM_UP_AXIS_SETTING_PATH', 'Gf', 'KEEP_SPACING_SETTING_PATH', 'SNAP_PROVIDER_NAME_SETTING_PATH', 'Sdf', 'SnapProvider', 'SnapProviderManager', 'SnapProviderRegistry', 'carb', 'sc']
class SnapProviderManager:
    """
    A manager that handles enabling, disabling, and updating snap functionality for providers in a viewport.
    
        This class manages a collection of snap providers, which are responsible for providing snapping behavior in the context of a 3D viewport. It subscribes to registry and settings changes to update the enabled providers accordingly.
    
        Args:
            viewport_api: The API object for interacting with the viewport.
        
    """
    def __del__(self):
        """
        Cleans up the manager and unsubscribes from registry changes.
        """
    def __init__(self, viewport_api):
        """
        Initializes the manager for snap providers.
        
                Args:
                    viewport_api: The API object for interacting with the viewport.
        """
    def _on_enabled_providers_changed(self, tree_item, changed_item, event_type):
        ...
    def _on_registry_changed(self):
        ...
    def _update_enabled_providers(self):
        ...
    def destroy(self):
        """
        Unsubscribes from registry and settings events, and cleans up the providers.
        """
    def get_snap_pos(self, xform: pxr.Gf.Matrix4d, ndc_location: typing.Sequence[float], scene_view: omni.ui_scene._scene.SceneView, on_snapped: typing.Callable) -> bool:
        """
        Iterates through enabled providers to find a snap position based on the provided transformation and location.
        
                Args:
                    xform (Gf.Matrix4d): The transformation matrix of the object to snap.
                    ndc_location (Sequence[float]): The location in normalized device coordinates where the snap is being requested.
                    scene_view (sc.SceneView): The SceneView object where the snap is occurring.
                    on_snapped (Callable): A callback function that is called when a snap occurs.
        
                Returns:
                    bool: True if a snap position was found and handled by a provider, False otherwise.
        """
    def on_began(self, excluded_paths: typing.List[typing.Union[pxr.Sdf.Path, str]], **kwargs):
        """
        Notifies enabled snap providers that a snap operation has begun.
        
                Args:
                    excluded_paths (List[Union[str, Sdf.Path]]): The list of paths to exclude from snapping.
                    **kwargs: Additional keyword arguments that may be required by the providers.
        """
    def on_ended(self, **kwargs):
        """
        Notifies enabled snap providers that a snap operation has ended.
        
                Args:
                    **kwargs: Additional keyword arguments that may be required by the providers.
        """
CONFORM_TO_TARGET_SETTING_PATH: str = '/persistent/exts/omni.kit.manipulator.tool.snap/conformToTarget'
CONFORM_UP_AXIS_SETTING_PATH: str = '/persistent/exts/omni.kit.manipulator.tool.snap/conformUpAxis'
KEEP_SPACING_SETTING_PATH: str = '/persistent/exts/omni.kit.manipulator.tool.snap/keepSpacing'
SNAP_PROVIDER_NAME_SETTING_PATH: str = '/exts/omni.kit.manipulator.tool.snap/providerNames'
