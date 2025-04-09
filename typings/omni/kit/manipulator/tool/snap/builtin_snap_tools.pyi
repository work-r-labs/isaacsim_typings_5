from __future__ import annotations
import carb as carb
import omni as omni
from omni.kit.manipulator.tool.snap.provider import SnapProvider
from omni.kit.viewport.utility import get_ground_plane_info
from omni.ui import scene as sc
from pxr import Sdf
from pxr import UsdGeom
import typing
__all__: list = ['PrimSnap', 'DepthBufferBasedSnap', 'GridSnap', 'PRIM_SNAP_NAME', 'SURFACE_SNAP_NAME', 'GRID_SNAP_NAME']
class DepthBufferBasedSnap(omni.kit.manipulator.tool.snap.provider.SnapProvider):
    """
    A snap provider assists in snapping objects within a 3D viewport.
    
        This snap provider utilizes raycasting or viewport picking queries to determine the snap location based on the depth buffer information. It is designed to work with viewport APIs that support 'rtx' engine or similar technologies for precise snapping to surfaces within the viewport.
    
        Args:
            viewport_api: The API used to interact with the viewport, enabling operations such as raycasting.
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def can_orient() -> bool:
        """
        Indicates if this snap provider can orient objects.
        
                Returns:
                    bool: True if the provider can orient objects, False otherwise.
        """
    @staticmethod
    def get_name() -> str:
        """
        Returns the unique name of this snap provider.
        
                Returns:
                    str: The name of the provider.
        """
    @staticmethod
    def get_order() -> float:
        """
        Returns the order value for this snap provider, which can affect the priority of snapping operations.
        
                Returns:
                    float: The order value, which is -1.0 indicating a high priority.
        """
    @staticmethod
    def require_viewport_api() -> bool:
        """
        Indicates if this snap provider requires the viewport API to function.
        
                Returns:
                    bool: False, as this provider does not require the viewport API.
        """
    @classmethod
    def get_display_name(cls) -> str:
        """
        Returns the display name of this snap provider.
        
                Returns:
                    str: The display name of the provider.
        """
    def _DepthBufferBasedSnap__can_provide_result(self, enabled_providers: typing.List[omni.kit.manipulator.tool.snap.provider.SnapProvider]) -> bool:
        """
        Determines if this snap provider can provide a result based on previous hits.
        
                Args:
                    enabled_providers (List[SnapProvider]): A list of currently enabled snap providers.
        
                Returns:
                    bool: True if this provider can provide a snap result, False otherwise.
        """
    def __init__(self, viewport_api):
        """
        Initializes the DepthBufferBasedSnap snap provider.
        
                Args:
                    viewport_api: The API used to interact with the viewport, enabling operations such as raycasting.
        """
    def _snap_by_picking_query(self, xform: Gf.Matrix4d, ndc_location: typing.Sequence[float], want_keep_spacing: bool, on_snapped: typing.Callable, enabled_providers: typing.List[omni.kit.manipulator.tool.snap.provider.SnapProvider]) -> bool:
        """
        Performs the snap operation using a viewport picking query.
        
                Args:
                    xform (Gf.Matrix4d): The current transform of the object being snapped.
                    ndc_location (Sequence[float]): The location in normalized device coordinates where the snap is initiated.
                    want_keep_spacing (bool): When multiple objects are selected, indicates if the original spacing between them should be maintained.
                    on_snapped (Callable): The callback function to be called once the snap result is available.
                    enabled_providers (List[SnapProvider]): A list of enabled snap providers.
        
                Returns:
                    bool: True if the snap can potentially provide a result, False otherwise.
        """
    def _snap_by_raycast_query(self, xform: Gf.Matrix4d, ndc_location: typing.Sequence[float], want_orient: bool, want_keep_spacing: bool, on_snapped: typing.Callable, conform_up_axis: str, enabled_providers: typing.List[omni.kit.manipulator.tool.snap.provider.SnapProvider]):
        """
        Performs the snap operation using a raycast query when the viewport API is using the 'rtx' engine.
        
                Args:
                    xform (Gf.Matrix4d): The current transform of the object being snapped.
                    ndc_location (Sequence[float]): The location in normalized device coordinates where the snap is initiated.
                    want_orient (bool): Indicates if the object needs to be oriented based on the snap result.
                    want_keep_spacing (bool): When multiple objects are selected, indicates if the original spacing between them should be maintained.
                    on_snapped (Callable): The callback function to be called once the snap result is available.
                    conform_up_axis (str): The axis to which the object should conform when oriented.
                    enabled_providers (List[SnapProvider]): A list of enabled snap providers.
        """
    def on_began(self, excluded_paths: typing.List[typing.Union[pxr.Sdf.Path, str]], **kwargs):
        """
        Called when the snap operation begins by setting up the excluded paths and preparing the USD context.
        
                Args:
                    excluded_paths (List[Union[str, Sdf.Path]]): The list of paths to be excluded from picking.
        """
    def on_ended(self, **kwargs):
        """
        Called when the snap operation ends by resetting the previous hit prim path and restoring pickability to the previously excluded paths.
        """
    def on_snap(self, xform: Gf.Matrix4d, ndc_location: typing.Sequence[float], scene_view: omni.ui_scene._scene.SceneView, want_orient: bool, want_keep_spacing: bool, on_snapped: typing.Callable, conform_up_axis: str, enabled_providers: typing.List[omni.kit.manipulator.tool.snap.provider.SnapProvider], *args, **kwargs) -> bool:
        """
        Attempts to snap an object to a surface within the viewport using either raycast or picking queries.
        
                Args:
                    xform (Gf.Matrix4d): The current transform of the object being snapped.
                    ndc_location (Sequence[float]): The location in normalized device coordinates where the snap is initiated.
                    scene_view (sc.SceneView): The scene view in which the snap is occurring.
                    want_orient (bool): Indicates if the object needs to be oriented based on the snap result.
                    want_keep_spacing (bool): When multiple objects are selected, indicates if the original spacing between them should be maintained.
                    on_snapped (Callable): The callback function to be called once the snap result is available.
                    conform_up_axis (str): The axis to which the object should conform when oriented.
                    enabled_providers (List[SnapProvider]): A list of enabled snap providers.
        
                Returns:
                    bool: True if the snap can potentially provide a result, False otherwise.
        """
class GridSnap(omni.kit.manipulator.tool.snap.provider.SnapProvider):
    """
    A snap provider for snapping objects to grid intersections in a 3D scene.
    
        This class is used to align objects to a virtual grid within the scene. It calculates the closest grid intersection point to the desired snapping location and moves the object to that point. Grid snapping does not orient the object; it only affects its position.
    
        Args:
            *args: Variable length argument list which will be forwarded to execute.
            **kwargs: Arbitrary keyword arguments that will be forwarded to execute.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def can_enable_menu(object: dict) -> bool:
        """
        Determines if the snap to grid option should be available in the menu.
        
                Args:
                    object (dict): The object to be considered for snapping.
        
                Returns:
                    bool: True if the grid is enabled and snap to grid should be available, False otherwise.
        """
    @staticmethod
    def can_orient() -> bool:
        """
        Indicates if the GridSnap provider can orient objects.
        
                Returns:
                    bool: False, as the GridSnap provider does not orient objects.
        """
    @staticmethod
    def get_name() -> str:
        """
        Returns the unique name of the GridSnap provider.
        
                Returns:
                    str: The name of the provider.
        """
    @staticmethod
    def get_order() -> float:
        """
        Returns the order value for the GridSnap provider, affecting the priority in snapping operations.
        
                Returns:
                    float: The order value which is 1.0.
        """
    def __init__(self, *args, **kwargs):
        """
        Initializes the GridSnap provider.
                Args:
                    *args: Variable length argument list which will be forwarded to execute.
                    **kwargs: Arbitrary keyword arguments that will be forwarded to execute.
                
        """
    def on_snap(self, xform: Gf.Matrix4d, ndc_location: typing.Sequence[float], scene_view: omni.ui_scene._scene.SceneView, want_orient: bool, want_keep_spacing: bool, on_snapped: typing.Callable, *args, **kwargs) -> bool:
        """
        Attempts to snap an object to the closest grid intersection point.
        
                Args:
                    xform (Gf.Matrix4d): The current transform of the object being snapped.
                    ndc_location (Sequence[float]): The location in normalized device coordinates where the snap is initiated.
                    scene_view (sc.SceneView): The scene view in which the snap is occurring.
                    want_orient (bool): Indicates if the object needs to be oriented based on the snap result.
                    want_keep_spacing (bool): When multiple objects are selected, indicates if the original spacing between them should be maintained.
                    on_snapped (Callable): The callback function to be called once the snap result is available.
        
                Returns:
                    bool: True if a snap point is found, False otherwise.
        """
class PrimSnap(omni.kit.manipulator.tool.snap.provider.SnapProvider):
    """
    A snap provider that allows snapping objects to the closest primitive based on provided NDC position.
    
        This provider is initialized with an optional list of excluded paths that should not be considered during the snapping process. It uses previous snap results to determine if a valid snap result can be provided, introducing a delay but solving multi-snap conflicts.
    
        Args:
            *args: Variable length argument list which will be forwarded to execute.
            **kwargs: Arbitrary keyword arguments that will be forwarded to execute.
        
    """
    __abstractmethods__: typing.ClassVar[frozenset]  # value = frozenset()
    _abc_impl: typing.ClassVar[_abc._abc_data]  # value = <_abc._abc_data object>
    @staticmethod
    def can_orient() -> bool:
        """
        Indicates if this snap provider can orient objects.
        
                Returns:
                    bool: True if the provider can orient objects, False otherwise.
                
        """
    @staticmethod
    def get_name() -> str:
        """
        Returns the unique name of this snap provider.
        
                Returns:
                    str: The name of the provider.
                
        """
    @classmethod
    def get_display_name(cls) -> str:
        """
        Returns the display name of this snap provider.
        
                Returns:
                    str: The display name of the provider.
                
        """
    def _PrimSnap__can_provide_result(self, enabled_providers: typing.List[omni.kit.manipulator.tool.snap.provider.SnapProvider]) -> bool:
        """
        Determines if this snap provider can provide a result based on previous hits.
        
                Args:
                    enabled_providers (List[SnapProvider]): A list of currently enabled snap providers.
        
                Returns:
                    bool: True if this provider can provide a snap result, False otherwise.
                
        """
    def __init__(self, *args, **kwargs):
        """
        Initializes the PrimSnap provider.
                Args:
                    *args: Variable length argument list which will be forwarded to execute.
                    **kwargs: Arbitrary keyword arguments that will be forwarded to execute.
                
        """
    def on_began(self, excluded_paths: typing.List[typing.Union[pxr.Sdf.Path, str]], **kwargs):
        """
        Called when the snap operation begins.
        
                Args:
                    excluded_paths (List[Union[str, Sdf.Path]]): The list of paths to be excluded from picking.
                
        """
    def on_ended(self, **kwargs):
        """
        Called when the snap operation ends.
        """
    def on_snap(self, xform: Gf.Matrix4d, ndc_location: typing.Sequence[float], scene_view: omni.ui_scene._scene.SceneView, want_orient: bool, want_keep_spacing: bool, on_snapped: typing.Callable, enabled_providers: typing.List[omni.kit.manipulator.tool.snap.provider.SnapProvider], *args, **kwargs) -> bool:
        """
        Attempts to snap to the closest prim based on the framebuffer.
        
                Args:
                    xform (Gf.Matrix4d): The current transform of the object being snapped.
                    ndc_location (Sequence[float]): The location in normalized device coordinates where the snap is being queried.
                    scene_view (sc.SceneView): The scene view in which the snap is occurring.
                    want_orient (bool): Indicates if the object needs to be oriented based on the snap result.
                    want_keep_spacing (bool): When multiple objects are selected, indicates if the original spacing between them should be maintained.
                    on_snapped (Callable): The callback function to be called once the snap result is available.
                    enabled_providers (List[SnapProvider]): A list of enabled snap providers.
        
                Returns:
                    bool: True if the snap can potentially provide a result, False otherwise.
                
        """
GRID_ENABLED_SETTING_PATH: str = '/app/viewport/grid/enabled'
GRID_SNAP_NAME: str = 'Grid'
PRIM_SNAP_DISPLAY_NAME: str = 'Prim'
PRIM_SNAP_NAME: str = 'Prim (Framebuffer Based)'
SURFACE_SNAP_DISPLAY_NAME: str = 'Surface'
SURFACE_SNAP_NAME: str = 'Surface (Framebuffer Based)'
