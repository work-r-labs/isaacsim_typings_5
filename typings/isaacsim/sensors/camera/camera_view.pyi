from __future__ import annotations
import isaacsim.core.prims.impl.xform_prim
from isaacsim.core.prims.impl.xform_prim import XFormPrim
from isaacsim.core.utils.carb import get_carb_setting
import numpy as np
import numpy
from omni.replicator import core as rep
from pxr import Usd
from pxr import Vt
import torch as torch
import warp as wp
import warp.context
import warp.types
__all__ = ['ANNOTATOR_SPEC', 'CameraView', 'R_U_TRANSFORM', 'U_R_TRANSFORM', 'U_W_TRANSFORM', 'Usd', 'Vt', 'W_U_TRANSFORM', 'XFormPrim', 'get_carb_setting', 'np', 'rep', 'reshape_tiled_image', 'torch', 'wp']
class CameraView(isaacsim.core.prims.impl.xform_prim.XFormPrim):
    """
    Provides high level functions to deal tiled/batched data from cameras
    
        .. list-table::
            :header-rows: 1
    
            * - Annotator type
                - Channels
                - Dtype
            * - ``"rgb"``
                - 3
                - ``uint8``
            * - ``"rgba"``
                - 4
                - ``uint8``
            * - ``"depth"`` / ``"distance_to_image_plane"``
                - 1
                - ``float32``
            * - ``"distance_to_camera"``
                - 1
                - ``float32``
            * - ``"normals"``
                - 4
                - ``float32``
            * - ``"motion_vectors"``
                - 4
                - ``float32``
            * - ``"semantic_segmentation"``
                - 1
                - ``uint32``
            * - ``"instance_segmentation_fast"``
                - 1
                - ``int32``
            * - ``"instance_id_segmentation_fast"``
                - 1
                - ``int32``
    
        Args:
            prim_paths_expr: Prim paths regex to encapsulate all prims that match it. E.g.: "/World/Env[1-5]/Camera" will match
                             /World/Env1/Camera, /World/Env2/Camera..etc. Additionally a list of regex can be provided.
            camera_resolution: Resolution of each sensor (width, height).
            output_annotators: Annotator/sensor types to configure.
            name (str, optional): Shortname to be used as a key by Scene class.
                                  Note: needs to be unique if the object is added to the Scene.
            positions Default positions in the world frame of the prim. Shape is (N, 3).
                      Defaults to None, which means left unchanged.
            translations: Default translations in the local frame of the prims (with respect to its parent prims). shape is (N, 3).
                          Defaults to None, which means left unchanged.
            orientations: Default quaternion orientations in the world/ local frame of the prim (depends if translation
                          or position is specified). Quaternion is scalar-first (w, x, y, z). Shape is (N, 4).
                          Defaults to None, which means left unchanged.
            scales: Local scales to be applied to the prim's dimensions. Shape is (N, 3).
                    Defaults to None, which means left unchanged.
            visibilities: Set to False for an invisible prim in the stage while rendering.
                          Shape is (N,). Defaults to None.
            reset_xform_properties: True if the prims don't have the right set of xform properties (i.e: translate,
                                    orient and scale) ONLY and in that order. Set this parameter to False if the object
                                    were cloned using using the cloner api in isaacsim.core.cloner. Defaults to True.
    
        Raises:
            Exception: if translations and positions defined at the same time.
            Exception: No prim was matched using the prim_paths_expr provided.
        
    """
    def __del__(self):
        ...
    def __init__(self, prim_paths_expr: str = None, name: str = 'camera_prim_view', camera_resolution: typing.Tuple[int, int] = (256, 256), output_annotators: typing.Optional[typing.List[str]] = ['rgb', 'depth'], positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, translations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, scales: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, visibilities: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, reset_xform_properties: bool = True):
        ...
    def _clean_up_tiled_sensor(self):
        """
        Clean up the sensor by detaching annotators and destroying render products, and removing related prims.
        """
    def _convert_camera_axes(self, orientations, transform_matrix):
        """
        Convert orientations using the specified transformation matrix.
        
                Args:
                    orientations (Union[np.ndarray, torch.Tensor, wp.array]): Input orientations.
                    transform_matrix (np.ndarray): The transformation matrix to apply.
        
                Returns:
                    The converted orientations.
                
        """
    def _get_tiled_resolution(self, num_cameras, resolution) -> typing.Tuple[int, int]:
        """
        Calculate the resolution for the tiled sensor based on the number of cameras and individual camera resolution.
        
                Args:
                    num_cameras (int): Total number of cameras.
                    resolution (Tuple[int, int]): Resolution of each individual camera.
        
                Returns:
                    Tuple[int, int]: The total resolution for the tiled sensor layout.
                
        """
    def _setup_tiled_sensor(self):
        """
        Set up the tiled sensor, compute resolutions, attach annotators, and initiate the render process.
        """
    def get_aspect_ratios(self) -> float:
        """
        Calculate the aspect ratio of the cameras based on current resolution settings.
        
                Returns:
                    float: The aspect ratio, defined as width divided by height.
                
        """
    def get_data(self, annotator_type: str, *, tiled: bool = False, out: typing.Optional[warp.types.array] = None) -> typing.Tuple[warp.types.array, dict[str, typing.Any]]:
        """
        Fetch the specified annotator/sensor data for all cameras as a batch of images or as a single tiled image.
        
                Args:
                    annotator_type: Annotator/sensor type from which fetch the data.
                    tiled: Whether to get annotator/sensor data as a single tiled image.
                    out: Pre-allocated array to fill with the fetched data.
        
                Returns:
                    2-items tuple. The first item is an array containing the fetched data (if ``out`` is defined,
                    its instance will be returned). The second item is a dictionary containing additional information according
                    to the requested annotator/sensor type.
        
                Raises:
                    ValueError: If the specified annotator type is not supported.
                    ValueError: If the specified annotator type is not configured when instantiating the object.
                
        """
    def get_depth(self, out = None) -> torch.Tensor:
        """
        Get the depth data for all cameras as a batch of images (num_cameras, height, width, 1).
        
                Returns:
                    torch.Tensor: containing the depth data for each camera.
                    Shape is (num_cameras, height, width, 1) with type torch.float32.
                
        """
    def get_depth_tiled(self, out = None, device = 'cpu') -> numpy.ndarray | torch.Tensor:
        """
        Fetch the depth data for all cameras as a single tiled image.
        
                Args:
                    device (str, optional): The device to return the data on ("cpu" or "cuda"). Defaults to "cpu".
                    out (np.ndarray | torch.Tensor, optional): Pre-allocated array or tensor to fill with the depth data.
        
                Returns:
                    np.ndarray | torch.Tensor: containing the depth data for each camera.
                
        """
    def get_focal_lengths(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.List[float]:
        """
        Get the focal length for all cameras
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
        
                Returns:
                    list[float]: list containing the focal lengths of the cameras.
                
        """
    def get_focus_distances(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.List[float]:
        """
        Get the focus distances for cameras specific in indices. If indices is None, get for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
        
                Returns:
                    list[float]: list containing the focal distances of the cameras.
                
        """
    def get_horizontal_apertures(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.List[float]:
        """
        Get the horizontal apertures for cameras specific in indices. If indices is None, get for all cameras.
        
                Emulates sensor/film width on a camera.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
        
                Returns:
                    list[float]: list containing the focal distances of the cameras.
                
        """
    def get_lens_apertures(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.List[float]:
        """
        Get the lens apertures for cameras specific in indices. If indices is None, get for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
        
                Returns:
                    list[float]: list containing the focal distances of the cameras.
                
        """
    def get_local_poses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, camera_axes: str = 'world') -> typing.Union[typing.Tuple[numpy.ndarray, numpy.ndarray], typing.Tuple[torch.Tensor, torch.Tensor], typing.Tuple[warp.types.indexedarray, warp.types.indexedarray]]:
        """
        Get prim poses in the view with respect to the local frame (the prim's parent frame)
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]: first index is positions in the local frame of the prims. shape is (M, 3).
                                                                                             second index is quaternion orientations in the local frame of the prims.
                                                                                             quaternion is scalar-first (w, x, y, z). shape is (M, 4).
        
                Example:
        
                
        """
    def get_projection_modes(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.List[str]:
        """
        Get the projection modes for cameras specific in indices. If indices is None, get for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
        
                Returns:
                    list[str]: list of projection modes (perspective, orthographic)
                
        """
    def get_projection_types(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.List[str]:
        """
        Get the projection types for cameras specific in indices. If indices is None, get for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
        
                Returns:
                    list[str]: list of projection types (pinhole, fisheyeOrthographic, fisheyeEquidistant, fisheyeEquisolid, fisheyePolynomial or fisheyeSpherical)
                
        """
    def get_render_product_path(self) -> str:
        """
        Retrieve the file path of the render product associated with the tiled sensor.
        
                Returns:
                    str: The path to the render product, or None if not available.
                
        """
    def get_resolutions(self) -> typing.Tuple[int, int]:
        """
        Retrieve the current resolution setting for all cameras.
        
                Returns:
                    Tuple[int, int]: The resolution of the cameras.
                
        """
    def get_rgb(self, out = None) -> torch.Tensor:
        """
        Get the RGB data for all cameras as a batch of images (num_cameras, height, width, 3).
        
                Returns:
                    torch.Tensor: containing the RGB data for each camera.
                    Shape is (num_cameras, height, width, 3) with type torch.float32.
                
        """
    def get_rgb_tiled(self, out = None, device = 'cpu') -> numpy.ndarray | torch.Tensor:
        """
        Fetch the RGB data for all cameras as a single tiled image.
        
                Args:
                    device (str, optional): The device to return the data on ("cpu" or "cuda"). Defaults to "cpu".
                    out (np.ndarray | torch.Tensor, optional): Pre-allocated array or tensor to fill with the RGBA data.
        
                Returns:
                    np.ndarray | torch.Tensor: containing the RGBA data for each camera. Depth channel is excluded if present.
                
        """
    def get_shutter_properties(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.List[typing.Tuple[float, float]]:
        """
        Get the (delay_open, delay_close) of shutter for cameras specific in indices. If indices is None, get for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
        
                Returns:
                    list[Tuple[float, float]]: list of tuple (delay_open, delay_close)
                
        """
    def get_stereo_roles(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.List[str]:
        """
        Get the stereo roles for cameras specific in indices. If indices is None, get for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
        
                Returns:
                    list[str]: list of stereo roles (mono, left, right)
                
        """
    def get_vertical_apertures(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> typing.List[float]:
        """
        Get the vertical apertures for cameras specific in indices. If indices is None, get for all cameras.
        
                Emulates sensor/film height on a camera.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
        
                Returns:
                    list[float]: list containing the focal distances of the cameras.
                
        """
    def get_world_poses(self, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, camera_axes: str = 'world', usd: bool = True) -> typing.Union[typing.Tuple[numpy.ndarray, numpy.ndarray], typing.Tuple[torch.Tensor, torch.Tensor], typing.Tuple[warp.types.indexedarray, warp.types.indexedarray]]:
        """
        Get the poses of the prims in the view with respect to the world's frame
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                         to query. Shape (M,).
                                                                                         Where M <= size of the encapsulated prims in the view.
                                                                                         Defaults to None (i.e: all prims in the view).
                    usd (bool, optional): True to query from usd. Otherwise False to query from Fabric data. Defaults to True.
        
                Returns:
                    Union[Tuple[np.ndarray, np.ndarray], Tuple[torch.Tensor, torch.Tensor], Tuple[wp.indexedarray, wp.indexedarray]]: first index is positions in the world frame of the prims. shape is (M, 3).
                                                                                             second index is quaternion orientations in the world frame of the prims.
                                                                                             quaternion is scalar-first (w, x, y, z). shape is (M, 4).
        
                Example:
        
                
        """
    def set_focal_lengths(self, values: typing.List[float], indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the focal length for cameras specific in indices. If indices is None, set for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to query. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
                    values (List[float]): list containing the focal lengths to set for the cameras.
                        Length of values must match length of indices.
                
        """
    def set_focus_distances(self, values: typing.List[float], indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the focus distance for cameras specific in indices. If indices is None, set for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to set. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
                    values (List[float]): list containing the focus distances to set for the cameras.
                        Length of values must match length of indices.
                
        """
    def set_horizontal_apertures(self, values: typing.List[float], indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the horizontal apertures for cameras specific in indices. If indices is None, set for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to set. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
                    values (List[float]): list containing the horizontal apertures to set for the cameras.
                        Length of values must match length of indices.
                
        """
    def set_lens_apertures(self, values: typing.List[float], indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the lens apertures for cameras specific in indices. If indices is None, set for all cameras.
        
                Controls Distance Blurring. Lower Numbers decrease focus range, larger numbers increase it.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to set. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
                    values (List[float]): list containing the lens apertures to set for the cameras.
                        Length of values must match length of indices.
                
        """
    def set_local_poses(self, positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, camera_axes: str = 'world') -> None:
        """
        Set the local poses for all cameras, adjusting their positions and orientations based on specified indices and coordinate system.
        
                Args:
                    positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): New positions for the cameras.
                    orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): New orientations for the cameras.
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]]): Specific cameras to update.
                    camera_axes (str): The coordinate system to use ('world', 'ros', 'usd').
        
                Raises:
                    Exception: If the provided camera_axes is not supported.
                
        """
    def set_projection_modes(self, values: typing.List[str], indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the projection modes for cameras specific in indices. If indices is None, set for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to set. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
                    values (List[str]): list of projection modes (perspective, orthographic)
                        Length of values must match length of indices.
                
        """
    def set_projection_types(self, values: typing.List[str], indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the projection types for cameras specific in indices. If indices is None, set for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to set. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
                    values (List[str]): list of projection types (pinhole, fisheyeOrthographic, fisheyeEquidistant, fisheyeEquisolid, fisheyePolynomial or fisheyeSpherical)
                        Length of values must match length of indices.
                
        """
    def set_resolutions(self, resolution: typing.Tuple[int, int]) -> None:
        """
        Set the resolutions for all cameras, updating the tiled sensor configuration if changed.
        
                Args:
                    resolution (Tuple[int, int]): The new resolution to apply to all cameras.
                
        """
    def set_shutter_properties(self, values: typing.List[typing.Tuple[float, float]], indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the (delay_open, delay_close) of shutter for cameras specific in indices. If indices is None, set for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to set. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
                    values (List[Tuple[float, float]]): list of tuple (delay_open, delay_close)
                        Length of values must match length of indices.
                
        """
    def set_stereo_roles(self, values: typing.List[str], indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the stereo roles for cameras specific in indices. If indices is None, set for all cameras.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to set. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
                    values (List[str]): list of stereo roles (mono, left, right)
                        Length of values must match length of indices.
                
        """
    def set_vertical_apertures(self, values: typing.List[float], indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None) -> None:
        """
        Set the vertical apertures for cameras specific in indices. If indices is None, set for all cameras.
        
                Emulates sensor/film height on a camera.
        
                Args:
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]], optional): indices to specify which prims
                                                                                            to set. Shape (M,).
                                                                                            Where M <= size of the encapsulated prims in the view.
                                                                                            Defaults to None (i.e: all prims in the view).
                    values (List[float]): list containing the vertical apertures to set for the cameras.
                        Length of values must match length of indices.
                
        """
    def set_world_poses(self, positions: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, orientations: typing.Union[numpy.ndarray, torch.Tensor, warp.types.array, NoneType] = None, indices: typing.Union[numpy.ndarray, list, torch.Tensor, warp.types.array, NoneType] = None, camera_axes: str = 'world', usd: bool = True) -> None:
        """
        Set the world poses for all cameras, adjusting their positions and orientations based on specified indices and coordinate system.
        
                Args:
                    positions (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): New positions for the cameras.
                    orientations (Optional[Union[np.ndarray, torch.Tensor, wp.array]]): New orientations for the cameras.
                    indices (Optional[Union[np.ndarray, list, torch.Tensor, wp.array]]): Specific cameras to update.
                    camera_axes (str): The coordinate system to use ('world', 'ros', 'usd').
                    usd (bool, optional): True to query from usd. Otherwise False to query from Fabric data. Defaults to True.
        
                Raises:
                    Exception: If the provided camera_axes is not supported.
                
        """
ANNOTATOR_SPEC: dict = {'rgb': {'name': 'rgba', 'channels': 4, 'dtype': warp.types.uint8}, 'rgba': {'name': 'rgba', 'channels': 4, 'dtype': warp.types.uint8}, 'depth': {'name': 'distance_to_image_plane', 'channels': 1, 'dtype': warp.types.float32}, 'distance_to_image_plane': {'name': 'distance_to_image_plane', 'channels': 1, 'dtype': warp.types.float32}, 'distance_to_camera': {'name': 'distance_to_camera', 'channels': 1, 'dtype': warp.types.float32}, 'normals': {'name': 'normals', 'channels': 4, 'dtype': warp.types.float32}, 'motion_vectors': {'name': 'motion_vectors', 'channels': 4, 'dtype': warp.types.float32}, 'semantic_segmentation': {'name': 'semantic_segmentation', 'channels': 1, 'dtype': warp.types.uint32}, 'instance_segmentation_fast': {'name': 'instance_segmentation_fast', 'channels': 1, 'dtype': warp.types.uint32}, 'instance_id_segmentation_fast': {'name': 'instance_id_segmentation_fast', 'channels': 1, 'dtype': warp.types.uint32}}
R_U_TRANSFORM: numpy.ndarray  # value = array([[ 1,  0,  0,  0],...
U_R_TRANSFORM: numpy.ndarray  # value = array([[ 1,  0,  0,  0],...
U_W_TRANSFORM: numpy.ndarray  # value = array([[ 0, -1,  0,  0],...
W_U_TRANSFORM: numpy.ndarray  # value = array([[ 0,  0, -1,  0],...
reshape_tiled_image: warp.context.Kernel  # value = <warp.context.Kernel object>
