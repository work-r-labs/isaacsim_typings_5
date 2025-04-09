from __future__ import annotations
import abc
from abc import ABC
from abc import abstractmethod
from omni.ui import scene as sc
import omni.ui_scene._scene
import pxr.Gf
from pxr import Gf
from pxr import Sdf
import typing
__all__ = ['ABC', 'Gf', 'Sdf', 'SnapProvider', 'abstractmethod', 'sc']
class SnapProvider(abc.ABC):
    """
    An abstract base class for snap providers in a manipulator tool.
    
        This class defines the interface for snap operations in manipulators. Implementors should provide functionality for snapping objects in 3D space based on the given parameters.
    
        Args:
            viewport_api: The API for interacting with the viewport in which snapping occurs.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset({'can_orient', 'get_name', 'on_snap'})
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def can_enable_menu(object: dict) -> bool:
        """
        Returns if the provider can be enabled on the menu.
        
                Args:
                    object: A dictionary containing context information about the object.
        
                Returns:
                    bool: True if the provider can be enabled, False otherwise.
        """
    @staticmethod
    def can_orient() -> bool:
        """
        Returns if the provider may change the orientation of the object during a snap.
        
                Returns:
                    bool: True if the snap provider can change orientation, False otherwise.
        """
    @staticmethod
    def get_name() -> str:
        """
        Returns the name/id of the provider. This is the internal name used for the snap manager.
        
                Returns:
                    str: The name/id of the snap provider.
        """
    @staticmethod
    def get_order() -> float:
        """
        Returns the priority order of the snap provider. If more than one provider is enabled at the same time and both
                are able to provide snap results, the one with the lower order wins.
        
                Returns:
                    float: The priority order of the provider.
        """
    @staticmethod
    def require_viewport_api() -> bool:
        """
        Returns if the provider requires viewport_api to work.
        
                Returns:
                    bool: True if viewport_api is required, False otherwise.
        """
    @classmethod
    def can_show_menu(cls, object: dict) -> bool:
        """
        Returns if the provider can appear in the menu list of all providers.
        
                Args:
                    object: A dictionary containing context information about the object.
        
                Returns:
                    bool: True if the provider can be shown in the menu, False otherwise.
        """
    @classmethod
    def get_display_name(cls) -> str:
        """
        Returns the display name of the provider. It will be used on the menu. If not overridden, it falls back to get_name() instead.
        
                Returns:
                    str: The display name of the snap provider.
        """
    def __del__(self):
        ...
    def __init__(self, viewport_api):
        """
        Initializes the SnapProvider with the given viewport API.
        
                Args:
                    viewport_api: The API for interacting with the viewport in which snapping occurs.
        """
    def _generate_picking_ray(self, ndc_location: typing.Sequence[float]) -> typing.Tuple[pxr.Gf.Vec3d, pxr.Gf.Vec3d, float]:
        """
        
                A helper function to generate picking ray from ndc cursor location.
                Only call it if self._viewport_api is not None.
                
        """
    def _get_gf_type(self, xform: Gf.Matrix4d) -> typing.Type:
        ...
    def _get_ndc_to_screen_matrix(self, scene_view: omni.ui_scene._scene.SceneView) -> pxr.Gf.Matrix4d:
        ...
    def destroy(self):
        """
        Cleans up any resources or state held by the provider.
        """
    def on_began(self, excluded_paths: typing.List[typing.Union[pxr.Sdf.Path, str]], **kwargs):
        """
        Initializes the snap operation with a list of paths to exclude from snapping.
        
                Args:
                    excluded_paths: A list of paths that should be excluded from snapping calculations.
        """
    def on_ended(self, **kwargs):
        """
        Resets the state of the provider when the snap operation ends.
        """
    def on_snap(self, xform: pxr.Gf.Matrix4d, ndc_location: typing.Sequence[float], scene_view: omni.ui_scene._scene.SceneView, want_orient: bool, want_keep_spacing: bool, on_snapped: typing.Callable, conform_up_axis: str, enabled_providers: typing.List[ForwardRef('SnapProvider')], *args, **kwargs) -> bool:
        """
        Called when manipulator wants to perform a snap operation. Only the current selected snap provider will be called.
        
                Args:
                    xform: Transformation of the current manipulator object.
                    ndc_location: Location of the cursor in NDC space.
                    scene_view: SceneView of the manipulator that triggers this snap request.
                    want_orient: If the snap provider can change the orientation of the object to be snapped (e.g., conform to normal),
                                 it should supply 'orient' to 'on_snapped' when 'want_orient' is True.
                    want_keep_spacing: When multiple objects are selected, indicates if the original spacing between them should be maintained.
                    on_snapped: A callback function receiving '**kwargs'. Depending on if the snap is successful and settings,
                                'position', 'path', 'orient' may be provided to it.
                    conform_up_axis: The up axis to be used to conform to the target orientation.
                    enabled_providers: All enabled providers for hint purposes. Do NOT modify the content.
        
                Returns:
                    bool: True if the snap is successful. If the snap is an asynchronous operation, return True if the request of snapping is successful.
                          False if the snap failed or cannot be requested.
        """
